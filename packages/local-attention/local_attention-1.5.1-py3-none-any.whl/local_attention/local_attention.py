import math
from operator import mul
from functools import reduce

import torch
from torch import nn, einsum
import torch.nn.functional as F

from local_attention.rotary import SinusoidalEmbeddings, apply_rotary_pos_emb

# constant

TOKEN_SELF_ATTN_VALUE = -5e4 # carefully set for half precision to work

# helper functions

def exists(val):
    return val is not None

def default(value, d):
    return d if not exists(value) else value

def to(t):
    return {'device': t.device, 'dtype': t.dtype}

def max_neg_value(tensor):
    return -torch.finfo(tensor.dtype).max

def merge_dims(ind_from, ind_to, tensor):
    shape = list(tensor.shape)
    arr_slice = slice(ind_from, ind_to + 1)
    shape[arr_slice] = [reduce(mul, shape[arr_slice])]
    return tensor.reshape(*shape)

def expand_dim(t, dim, k, unsqueeze=True):
    if unsqueeze:
        t = t.unsqueeze(dim)
    expand_shape = [-1] * len(t.shape)
    expand_shape[dim] = k
    return t.expand(*expand_shape)

def pad_to_multiple(tensor, multiple, dim=-1, value=0):
    seqlen = tensor.shape[dim]
    m = seqlen / multiple
    if m.is_integer():
        return tensor
    remainder = math.ceil(m) * multiple - seqlen
    pad_offset = (0,) * (-1 - dim) * 2
    return F.pad(tensor, (*pad_offset, 0, remainder), value = value)

def look_around(x, backward = 1, forward = 0, pad_value = -1, dim = 2):
    t = x.shape[1]
    dims = (len(x.shape) - dim) * (0, 0)
    padded_x = F.pad(x, (*dims, backward, forward), value = pad_value)
    tensors = [padded_x[:, ind:(ind + t), ...] for ind in range(forward + backward + 1)]
    return torch.cat(tensors, dim = dim)

# main class

class LocalAttention(nn.Module):
    def __init__(
        self,
        window_size,
        causal = False,
        look_backward = 1,
        look_forward = None,
        dropout = 0.,
        shared_qk = False,
        rel_pos_emb_config = None,
        dim = None,
        autopad = False,
        exact_windowsize = False
    ):
        super().__init__()
        look_forward = default(look_forward, 0 if causal else 1)
        assert not (causal and look_forward > 0), 'you cannot look forward if causal'

        self.window_size = window_size
        self.autopad = autopad
        self.exact_windowsize = exact_windowsize

        self.causal = causal

        self.look_backward = look_backward
        self.look_forward = look_forward

        self.dropout = nn.Dropout(dropout)

        self.shared_qk = shared_qk

        # relative positions

        self.rel_pos = None
        if exists(rel_pos_emb_config) or exists(dim):  # backwards compatible with old `rel_pos_emb_config` deprecated argument
            if exists(rel_pos_emb_config):
                dim = rel_pos_emb_config[0]
            self.rel_pos = SinusoidalEmbeddings(dim)

    def forward(self, q, k, v, input_mask = None):
        shape, autopad, pad_value = q.shape, self.autopad, -1

        merge_into_batch = lambda t: t.reshape(-1, *t.shape[-2:])
        q, k, v = map(merge_into_batch, (q, k, v))

        if exists(self.rel_pos):
            pos_emb = self.rel_pos(q)
            q, k = apply_rotary_pos_emb(q, k, pos_emb)

        if autopad:
            orig_t = q.shape[1]
            q, k, v = map(lambda t: pad_to_multiple(t, self.window_size, dim = -2), (q, k, v))

        window_size, causal, look_backward, look_forward, shared_qk = self.window_size, self.causal, self.look_backward, self.look_forward, self.shared_qk

        b, t, e, device, dtype = *q.shape, q.device, q.dtype
        scale = e ** -0.5

        assert (t % window_size) == 0, f'sequence length {t} must be divisible by window size {window_size} for local attention'

        windows = t // window_size

        if shared_qk:
            k = F.normalize(k, 2, dim=-1).type_as(q)

        ticker = torch.arange(t, device=device, dtype=torch.long)[None, :]
        b_t = ticker.reshape(1, windows, window_size)

        bucket_fn = lambda t: t.reshape(b, windows, window_size, -1)
        bq, bk, bv = map(bucket_fn, (q, k, v))

        look_around_kwargs = dict(
            backward =  look_backward,
            forward =  look_forward,
            pad_value = pad_value
        )

        bk = look_around(bk, **look_around_kwargs)
        bv = look_around(bv, **look_around_kwargs)

        bq_t = b_t
        bq_k = look_around(b_t, **look_around_kwargs)

        dots = einsum('b h i e, b h j e -> b h i j', bq, bk) * scale

        mask_value = max_neg_value(dots)

        if shared_qk:
            mask = bq_t[..., :, None] == bq_k[..., None, :]
            dots = dots.masked_fill(mask, TOKEN_SELF_ATTN_VALUE)
            del mask

        if causal:
            mask = bq_t[..., :, None] < bq_k[..., None, :]

            if self.exact_windowsize:
                max_causal_window_size = (self.window_size * self.look_backward)
                mask = mask | (bq_t[..., :, None] > (bq_k[..., None, :] + max_causal_window_size))

            dots = dots.masked_fill(mask, mask_value)
            del mask

        mask = bq_k[:, :, None, :] == pad_value
        dots = dots.masked_fill(mask, mask_value)
        del mask

        if exists(input_mask):
            h = b // input_mask.shape[0]
            if autopad:
                input_mask = pad_to_multiple(input_mask, window_size, dim = -1, value = False)
            input_mask = input_mask.reshape(-1, windows, window_size)
            mq = mk = input_mask
            mk = look_around(mk, **{**look_around_kwargs, 'pad_value': False})
            mask = mq[..., :, None] & mk[..., None, :]
            mask = merge_dims(0, 1, expand_dim(mask, 1, h))
            dots = dots.masked_fill(~mask, mask_value)
            del mask

        attn = dots.softmax(dim = -1)
        attn = self.dropout(attn)

        out = einsum('b h i j, b h j e -> b h i e', attn, bv)
        out = out.reshape(-1, t, e)

        if autopad:
            out = out[:, :orig_t, :]

        return out.reshape(*shape)

import torch.nn as nn
import torch
import torch.nn.functional as F
from torch import Tensor

class Swish(nn.Module):
	def __init__(self):
		super(Swish, self).__init__()

	def forward(self, x):
		return x * torch.sigmoid(x)

class Relu(nn.Module):
	def __init__(self):
		super().__init__()

	def forward(self, x):
		return torch.relu(x)
class SRelu(nn.Module):
	def __init__(self):
		super().__init__()

	def forward(self, x):
		return torch.square(torch.relu(x))

class Gelu(nn.Module):
	def __init__(self):
		super().__init__()

	def forward(self, x):
		return F.gelu(x)

class Lrelu(nn.Module):
	def __init__(self):
		super().__init__()

	def forward(self, x):
		return F.leaky_relu(x)

class Elu(nn.Module):
	def __init__(self):
		super().__init__()

	def forward(self, x):
		return F.elu(x)

class ReGLU(nn.Module):
    """
    References:
        Shazeer et al., "GLU Variants Improve Transformer," 2020.
        https://arxiv.org/abs/2002.05202
    """

    def reglu(self, x: Tensor) -> Tensor:
        assert x.shape[-1] % 2 == 0
        a, b = x.chunk(2, dim=-1)
        return a * F.relu(b)

    def forward(self, x: Tensor) -> Tensor:
        return self.reglu(x)


class GEGLU(nn.Module):
    """
    References:
        Shazeer et al., "GLU Variants Improve Transformer," 2020.
        https://arxiv.org/abs/2002.05202
    """

    def geglu(self, x: Tensor) -> Tensor:
        assert x.shape[-1] % 2 == 0
        a, b = x.chunk(2, dim=-1)
        return a * F.gelu(b)

    def forward(self, x: Tensor) -> Tensor:
        return self.geglu(x)

class SWGLU(nn.Module):
    """
    References:
        Shazeer et al., "GLU Variants Improve Transformer," 2020.
        https://arxiv.org/abs/2002.05202
    """

    def swglu(self, x: Tensor) -> Tensor:
        assert x.shape[-1] % 2 == 0
        a, b = x.chunk(2, dim=-1)
        return a * F.silu(b)

    def forward(self, x: Tensor) -> Tensor:
        return self.swglu(x)
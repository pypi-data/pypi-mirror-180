from abc import ABC

import torch
from pyro.nn import PyroParam
from torch.distributions.constraints import corr_cholesky, positive

from .abc import AbstractGaussianGTFlow, GTFlow


class LocatedGTFlow(GTFlow, ABC):
    @PyroParam(event_dim=1)
    def loc(self):
        return self.init[self.mask]


class GaussianGTFlow(LocatedGTFlow, AbstractGaussianGTFlow):
    init_scale = 1.

    @PyroParam(constraint=positive, event_dim=1)
    def scale(self):
        return self._scale_diagonal(self.init_scale, self.jacobian(self.loc))

    @PyroParam(constraint=corr_cholesky, event_dim=2)
    def corr_cholesky(self):
        return torch.eye(len(self.loc), device=self.loc.device, dtype=self.loc.dtype)

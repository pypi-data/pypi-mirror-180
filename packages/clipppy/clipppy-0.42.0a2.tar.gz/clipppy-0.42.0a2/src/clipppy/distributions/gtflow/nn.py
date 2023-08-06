from torch import Tensor
from torch.distributions import biject_to
from torch.distributions.constraints import corr_cholesky, positive
from torch.nn import Module

from .abc import AbstractGaussianGTFlow
from .gtflow import ConditionalGTFlow


class NNGaussianGTFlow(ConditionalGTFlow[Tensor], AbstractGaussianGTFlow):
    net_loc: Module
    net_scale: Module
    net_corr_cholesky: Module

    @property
    def loc(self) -> Tensor:
        return self.net_loc(self.conditional_context)

    @property
    def scale(self) -> Tensor:
        return biject_to(positive)(self.net_scale(self.conditional_context))

    @property
    def corr_cholesky(self) -> Tensor:
        return biject_to(corr_cholesky)(self.net_corr_cholesky(self.conditional_context))

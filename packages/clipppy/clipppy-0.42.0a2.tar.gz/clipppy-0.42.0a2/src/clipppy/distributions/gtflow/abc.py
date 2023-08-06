from abc import ABC, abstractmethod

from pyro.distributions import MultivariateNormal
from torch import Tensor

from .gtflow import GTFlow


class AbstractLocatedGTFlow(GTFlow, ABC):
    @property
    @abstractmethod
    def loc(self) -> Tensor: ...


class AbstractGaussianGTFlow(AbstractLocatedGTFlow):
    @property
    @abstractmethod
    def scale(self) -> Tensor: ...

    @property
    @abstractmethod
    def corr_cholesky(self) -> Tensor: ...

    @property
    def corr_cholesky_event_size(self):
        return (self.event_size * (self.event_size - 1)) // 2

    @property
    def scale_tril(self) -> Tensor:
        return self.scale.unsqueeze(-1) * self.corr_cholesky

    @property
    def prior(self):
        return MultivariateNormal(self.loc, scale_tril=self.scale_tril)

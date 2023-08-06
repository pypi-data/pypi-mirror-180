from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import Generic, Iterable, Mapping, MutableMapping, TypeVar, Union

import torch
from pyro.distributions import ConditionalDistribution, TorchDistribution
from pyro.distributions.distribution import DistributionMeta
from pyro.distributions.util import eye_like
from pyro.nn.module import _PyroModuleMeta, PyroModule
from torch import BoolTensor, Size, Tensor
from torch.distributions import constraints, Transform
from torch.nn import Module

from ...utils import to_tensor


_Tensor_Type = TypeVar('_Tensor_Type', bound=Tensor)
_ContextT = TypeVar('_ContextT')


class DistributionModuleMeta(_PyroModuleMeta, DistributionMeta):
    def __getattr__(self, item):
        if item.startswith('_pyro_prior_'):
            return getattr(self, item.lstrip('_pyro_prior_')).prior
        return super().__getattr__(item)

    def __getitem__(self, item):
        if isinstance(item, Module):
            return super().__getitem__(item)
        return self


@dataclass
class GTFlow(TorchDistribution, PyroModule, metaclass=DistributionModuleMeta):
    def __hash__(self):
        return super().__hash__()

    @staticmethod
    def _scale_diagonal(scale: Union[Tensor, float], jac: Tensor):
        return to_tensor(scale).to(jac).expand_as(jac) / jac

    @staticmethod
    def _scale_matrix(scale: Union[Tensor, float], jac: Tensor):
        scale = to_tensor(scale).to(jac)
        if not scale.shape[-2:] == 2*(jac.shape[-1],):
            scale = eye_like(jac, jac.shape[-1]) * scale.expand_as(jac).unsqueeze(-2)
        return scale / jac.unsqueeze(-1)

    arg_constraints = {}

    @property
    def support(self):
        return constraints.independent(constraints.real, 1)

    names: Iterable[str]
    sizes: MutableMapping[str, int]
    poss: MutableMapping[str, int]
    transforms: MutableMapping[str, Transform]
    event_dims: MutableMapping[str, int]
    masks: MutableMapping[str, BoolTensor]
    inits: MutableMapping[str, Tensor]

    def __post_init__(self):
        super().__init__()

    def _cat_sites(self, vals: Mapping[str, _Tensor_Type]) -> _Tensor_Type:
        return torch.cat(tuple(
            vals[name].flatten(vals[name].ndim-self.event_dims[name])
            if self.event_dims[name] else vals[name].unsqueeze(-1)
            for name in self.names if name in vals.keys()
        ), dim=-1)

    @cached_property
    def init(self) -> Tensor:
        return self._cat_sites(self.inits)

    @cached_property
    def mask(self) -> BoolTensor:
        return self._cat_sites(self.masks)

    @cached_property
    def event_shape(self):
        return Size((self.event_size,))

    @cached_property
    def event_size(self) -> int:
        return sum(self.sizes.values())

    def _unpack_site(self, arr: Tensor, name: str):
        return arr[..., self.poss[name]:self.poss[name]+self.sizes[name]]

    def unpack_site(self, group_z: Tensor, name: str):
        zs = self._unpack_site(group_z, name)
        z = self.inits[name].expand(zs.shape[:-1] + self.masks[name].shape).clone()
        z[..., self.masks[name]] = zs
        return z, self.transforms[name](z)

    def unpack(self, group_z: Tensor, names: Iterable[str] = None) -> MutableMapping[str, Tensor]:
        return {name: self.unpack_site(group_z, name)[1]
                for name in (names or self.names)}

    def pack(self, values: Mapping[str, Tensor]):
        return self._cat_sites({
            name: self.transforms[name].inv(val)
            for name, val in values.items()
        })

    def log_jacobian(self, value: Tensor, names: Iterable[str] = None) -> Tensor:
        return torch.cat(tuple(
            tr.log_abs_det_jacobian(z, tr(z))
            for name in self.names if (not names) or (name in names)
            for z in [self._unpack_site(value, name)]
            for tr in [self.transforms[name]]
        ), -1)

    def jacobian(self, value: Tensor, names: Iterable[str] = None) -> Tensor:
        return self.log_jacobian(value, names).exp()

    def log_abs_det_jacobian(self, value):
        return self.log_jacobian(value).sum(-1)

    @property
    @abstractmethod
    def prior(self) -> TorchDistribution: ...

    has_rsample = True
    include_det_jac = True

    def rsample(self, sample_shape=Size()):
        return self.prior.rsample(sample_shape=sample_shape)

    def log_prob(self, value):
        log_prob = self.prior.log_prob(value)
        return (log_prob - self.log_abs_det_jacobian(value)
                if self.include_det_jac else log_prob)

    def log_prob_transformed(self, values: Mapping[str, Tensor]):
        return self.log_prob(self.pack(values))

    def cdf(self, value):
        return self.prior.cdf(value)

    def icdf(self, value):
        return self.prior.icdf(value)


class ConditionalGTFlow(GTFlow, ConditionalDistribution, Generic[_ContextT], ABC):
    conditional_context: _ContextT

    def condition(self, context: _ContextT):
        self.conditional_context = context
        return self

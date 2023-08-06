import torch
from xitorch.optimize.rootfinder import rootfinder


def igammainv(a, y):
    d = 1 / (9 * a)
    y0 = a * (1 - d + 2**0.5 * torch.erfinv(2*y-1) * d**0.5)**3
    return rootfinder(lambda _: torch.igamma(a, _), y0)

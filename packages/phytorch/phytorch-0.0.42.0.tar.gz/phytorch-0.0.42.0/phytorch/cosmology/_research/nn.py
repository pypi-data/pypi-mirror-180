from contextlib import suppress

import numpy as np
import torch
from torch.distributions import Uniform
from torch.nn import LazyLinear, Module, ReLU, Sequential, Softplus, Tanh
from torch.optim import Adam
from tqdm.auto import tqdm


class CosmoNN(Module):
    def __init__(self):
        super().__init__()
        relu = ReLU()
        self.nn = Sequential(
            LazyLinear(64), relu,
            LazyLinear(64), relu,
            LazyLinear(1)
        )

    def forward(self, Om0, Ode0, z):
        return self.nn(torch.stack(torch.broadcast_tensors(Om0, Ode0, z), -1)).squeeze(-1)


from astropy.cosmology import LambdaCDM

hd = LambdaCDM(100, 0, 0).hubble_distance
f = np.vectorize(
    lambda _Om0, _Ode0, _z:
        (LambdaCDM(100, _Om0, _Ode0).comoving_distance(_z) / hd).to('').value,
    # signature='(),(),()->(k)'
)

net = CosmoNN()
lfunc = torch.nn.MSELoss()
optim = Adam(params=net.parameters(), lr=1e-4)

priors = {
    'Om0': Uniform(0, 1),
    'Ode0': Uniform(0, 1),
    'z': Uniform(0, 10)
}

nbatch = 32

with tqdm() as tq, suppress(KeyboardInterrupt):
    while True:
        optim.zero_grad()

        Om0, Ode0, z = (p.sample((nbatch,)) for p in priors.values())
        pred = net(Om0, Ode0, z)
        truth = torch.as_tensor(f(Om0.numpy(), Ode0.numpy(), z.numpy()),
                                device=pred.device, dtype=pred.dtype)

        loss = ((pred - truth)**2).exp().mean()
        loss.backward()
        optim.step()

        with torch.no_grad():
            tq.update(nbatch)
            tq.set_postfix_str(str((loss - 1).sqrt().item()))

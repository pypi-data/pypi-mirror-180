from itertools import combinations_with_replacement

import numpy as np
import sympy as sym
from astropy.cosmology import LambdaCDM
from tqdm.auto import tqdm

Om0 = np.linspace(0, 1, 101)
Ode0 = np.linspace(0, 1, 101)
z = np.linspace(0, 10, 1001)

xs = np.meshgrid(Om0 - 0.5, Ode0 - 0.5)

hd = LambdaCDM(100, 0, 0).hubble_distance
ys = np.vectorize(
    lambda _Om0, _Ode0:
        (LambdaCDM(100, _Om0, _Ode0).comoving_distance(z) / hd).to('').value,
    signature='(),()->(k)'
)(Om0[:, None], Ode0[None, :])
coeffs = np.polyfit(z, ys.reshape(-1, len(z)).T, 16).reshape(-1, *ys.shape[:-1])


DEGREE = 19
xs_s = sym.symbols('Om0 Ode0')
features_s = list(map(np.prod, combinations_with_replacement(xs_s + (1,), DEGREE)))
features = np.stack([sym.lambdify(xs_s, f)(*xs) for f in tqdm(features_s[:-1])] + [np.ones_like(xs[0])], -1)

A = features.reshape(-1, features.shape[-1])
b = coeffs.reshape(len(coeffs), -1).T

coeffs2, *_ = np.linalg.lstsq(A, b, rcond=0)
pred = np.polyval((A @ coeffs2).T[..., None], z[None, :]).reshape(ys.shape)

# b = ys.reshape(-1)
# coeffs, *stats = np.linalg.lstsq(A, b, rcond=0)

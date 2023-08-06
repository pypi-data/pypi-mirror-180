import os
from warnings import warn

import mpmath
import numpy as np
import torch
from astropy.cosmology import default_cosmology, FlatLambdaCDM, LambdaCDM
from torch.utils.cpp_extension import load

# noinspection PyUnresolvedReferences
from matplotlib import pyplot as plt
# noinspection PyUnresolvedReferences
from matplotlib.colors import LogNorm, SymLogNorm


os.environ['CXX'] = 'g++-8'
test_cpp = load('ellipr', ['/home/kosio/Projects/Python/phytorch-extensions/ellipr.cpp'])
elliprf = test_cpp.elliprf


def efunc(z, Or0, Om0, Ode0):
    z1 = z+1
    return Or0*z1**4 + Om0*z1**3 + Ok0(Or0, Om0, Ode0)*z1**2 + Ode0


def eint_num(z, Or0, Om0, Ode0, n=1000):
    dz = z/n
    _z = np.linspace(0, z, n) + dz/2
    return (1 / np.sqrt(efunc(_z, Or0, Om0, Ode0))).sum() * dz


def quartic_roots(a, b, c, d, e, eps=1e-10):
    if isinstance(a, float):
        a, b, c, d, e = map(complex, (a, b, c, d, e))
    twop = (8*a*c - 3*b**2) / (4*a**2)
    q = (b**3 - 4*a*b*c + 8*a**2*d) / (8*a**3)
    D0 = c**2 - 3*b*d + 12*a*e
    D1 = 2*c**3 - 9*b*c*d + 27*b**2*e + 27*a*d**2 - 72*a*c*e
    Q = (D1 + (D1**2 - 4 * D0**3)**0.5)**(1/3) / 2**(1/3)
    _S2 = ((Q + D0 / Q) / a - twop) / 12
    S2 = _S2
    # if abs(_S2) < eps:
    #     Q = Q * (-0.5 - 3**0.5 * 0.5j)
    #     S2 = ((Q + D0 / Q) / a - twop) / 12
    # else:
    #     S2 = _S2
    fourS2mtwop = -4*S2 - twop
    S = S2**0.5
    qS = q / S
    pmp = (fourS2mtwop + qS)**0.5 / 2
    pmm = (fourS2mtwop - qS)**0.5 / 2
    mb4a = -b / (4*a)
    mb4apS = mb4a + S
    mb4amS = mb4a - S
    return mb4amS - pmp, mb4amS + pmp, mb4apS - pmm, mb4apS + pmm


def companion(p):
    p = torch.as_tensor(p)
    n = p.shape[-1]-1
    return torch.cat((
        -(p[..., 1:] / p[..., :1]).unsqueeze(-2),
        torch.eye(n-1, n).expand(*p.shape[:-1], n-1, n)
    ), -2)


def roots(p):
    return torch.complex(*companion(p).eig(eigenvectors=False)[0].movedim(-1, 0))


def s(x):
    return x**0.5


def Ok0(Or0, Om0, Ode0):
    return 1 - (Or0 + Om0 + Ode0)


def solve_cosmo_quartic(Or0, Om0, Ode0, z=None, eps=1e-4):
    # rs = quartic_roots(Or0, Om0, Ok0(Or0, Om0, Ode0), 0, Ode0)
    # rs = [root.item() for root in roots([Or0, Om0, Ok0(Or0, Om0, Ode0), 0, Ode0])]
    rs = np.roots([Or0, Om0, Ok0(Or0, Om0, Ode0), 0, Ode0])
    # if z is not None:
    #     poles = [r for r in roots if 1 <= r.real <= z+1 and abs(r.imag) < eps]
    #     if poles:
    #         warn('There are poles along the integration path:\n'
    #              f'(Or0={Or0}, Om0={Om0}, Ode0={Ode0}) -> {poles}', RuntimeWarning)
    #         return len(roots) * (float('nan')*complex(),)
    return rs


def eint_general(z, Or0, Om0, Ode0):
    a = [r-1 for r in solve_cosmo_quartic(Or0, Om0, Ode0, z)]

    u01_2 = ((
         s(z-a[0])*s(z-a[1]) * s(-a[2])*s(-a[3])
         + s(-a[0])*s(-a[1]) * s(z-a[2])*s(z-a[3])
    ) / z)**2
    u02_2 = u01_2 - (a[3]-a[0])*(a[2]-a[1])
    u12_2 = u01_2 - (a[3]-a[1])*(a[2]-a[0])

    return 2 * elliprf(u01_2, u02_2, u12_2) / s(Or0)


c: FlatLambdaCDM = default_cosmology.get().clone(Neff=0, Tcmb0=10)
hd = c.hubble_distance

ZMAX = 10
Om0 = np.linspace(0, 2, 41)
Ode0 = np.linspace(0, 2, 41)
z = np.linspace(0.1, ZMAX, 100)

dx, dy = (Om0[1]-Om0[0])/2, (Ode0[1]-Ode0[0])/2
imkwargs = dict(origin='lower', extent=(Om0[0]-dx, Om0[-1]+dx, Ode0[0]-dy, Ode0[-1]+dy))
xlabel = r'$\Omega_{m, 0}$'
ylabel = r'$\Omega_{\Lambda}$'

args = (z, c.Ogamma0 + c.Onu0, Om0[:, None, None], Ode0[None, :, None])


from time import time

t0 = time()
mine = np.vectorize(eint_general)(*args)
print('mine', time() - t0)
t0 = time()
# theirs = np.vectorize(eint_short)(*args)
# theirs = np.vectorize(eint_num)(*args)
theirs = np.vectorize(
    lambda _z, _Or0, _Om0, _Ode0:
        (LambdaCDM(c.H0, _Om0, _Ode0, Tcmb0=c.Tcmb0, Neff=c.Neff).comoving_distance(_z) / hd).to('').value,
)(*args)
print('theirs', time() - t0)


ratio = abs(mine)/theirs
ratio = ratio[np.arange(ratio.shape[0])[:, None], np.arange(ratio.shape[0])[None, :],
              np.ma.array(abs(np.log(ratio)), mask=np.isnan(ratio)).argmax(-1)]
plt.imshow(ratio.T - 1, **imkwargs,
           norm=SymLogNorm(1e-8, vmin=-2e-7, vmax=2e-7), cmap='bwr')
plt.colorbar()
# plt.contour(Om0, Ode0, ratio, levels=(1.,))
plt.xlabel(xlabel), plt.ylabel(ylabel)
plt.xlim(*Om0[(0, -1),]), plt.ylim(*Ode0[(0, -1),])


import sympy as sym
A, B, C = sym.symbols('A B C', real=True, nonnegative=True)
_x = sym.Symbol('x')
discrim = sym.polys.polytools.discriminant(A*_x**4 + B*_x**3 + Ok0(A, B, C) * _x**2 + C)
D = sym.lambdify((B, C), discrim.subs(A, args[1]))(*np.meshgrid(*2*[np.linspace(0, 2, 2001)]))
plt.contour(D, extent=(0, 2, 0, 2), origin='lower', levels=(0,), colors='red')

from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass
from functools import cached_property, partial, update_wrapper
from numbers import Number
from operator import itemgetter
from typing import Any, Callable, ClassVar, Generic, Iterable, Sequence, TypeVar

import numpy as np
import sympy as sym
from more_itertools import locate, only, take
from numpy import argsort

from ...utils.symmetry import product


_T = TypeVar('_T')
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')

_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

_sqrt = lambda x: x**(1/2)


class LazyDict(dict[_KT, _VT], Generic[_KT, _VT]):
    def __init__(self, func: Callable[[_KT], _VT]):
        super().__init__()
        self.func = func

    def __missing__(self, key):
        self[key] = ret = self.func(key)
        return ret


def starcall(f: Callable[[_T1, ...], _T2]) -> Callable[[tuple[_T1, ...]], _T2]:
    def _f(args) -> _T1:
        return f(*args)
    return update_wrapper(_f, f)


def lazify(f):
    @cached_property
    def _f(self):
        return LazyDict(f.__get__(self, type(self)))
    return _f


def starcall_lazify(f: Callable[[Any, _T1, ...], _T2]) -> cached_property[LazyDict[_T1, _T2]]:
    @cached_property
    def _f(self):
        return LazyDict(starcall(partial(f, self)))
    _f._lazified = True
    return _f


class NotABasicIntegralError(Exception):
    pass


class Array(np.ndarray):
    def add(self, *ii: int):
        ret = self.copy()
        for i in ii:
            ret[i] += 2
        return ret

    def sub(self, *ii: int):
        ret = self.copy()
        for i in ii:
            ret[i] -= 2
        return ret

    def __hash__(self):
        return hash(tuple(self))

    def __eq__(self, other):
        ret = super().__eq__(other)
        return all(ret) if isinstance(other, type(self)) else ret


@dataclass
class BaseEllipticReduction(Generic[_T], ABC):
    x: _T
    y: _T
    a: Sequence[_T]
    b: Sequence[_T] = None
    m: int = 4

    def __post_init__(self):
        if self.b is None:
            self.b = len(self.a) * (1,)

    @cached_property
    def n(self):
        return len(self.a)

    @cached_property
    def idx_set(self):
        return set(i-(self.m==3) for i in range(4))

    @starcall_lazify
    def d(self, i: int, j: int):
        return (
            -self.d[j, i] if j < i else
            self.b[j] if i<0 else
            self.a[i] * self.b[j] - self.a[j] * self.b[i]
        )

    @cached_property
    def xmy(self):
        return self.x - self.y

    @cached_property
    def xmy2(self):
        return self.xmy**2

    def _s(self, i: int, z: _T):
        return 1 if i<0 else (self.a[i] + self.b[i] * z)

    def _ss(self, i: int, z: _T):
        return _sqrt(self._s(i, z))

    @cached_property
    def X(self):
        return LazyDict(partial(self._ss, z=self.x))

    @cached_property
    def Y(self):
        return LazyDict(partial(self._ss, z=self.y))

    @abstractmethod
    def v(self, z: _T, *args, **kwargs) -> _T: ...

    def vx(self, *args, **kwargs):
        return self.v(self.x, *args, **kwargs)

    def vy(self, *args, **kwargs):
        return self.v(self.y, *args, **kwargs)

    def A(self, *args, **kwargs) -> _T:
        return self.vx(*args, **kwargs) - self.vy(*args, **kwargs)

    @starcall_lazify
    def U(self, i: int, j: int) -> _T:
        # C99, (4.12)
        if j < i:
            return self.U[j, i]

        k, l = self.idx_set - {i, j}
        return (self.X[i] * self.X[j] * self.Y[k] * self.Y[l]
                + self.Y[i] * self.Y[j] * self.X[k] * self.X[l])
        # if j < i:
        #     return self.U2(j, i)
        # elif i==3 and j==4:
        #     return self.U2(1, 2)
        # elif i==1 and j==2:
        #     k, l = 3, 4
        #     return ((self.X[i]*self.X[j] * self.Y[k]*self.Y[l] + self.Y[i]*self.Y[j] * self.X[k]*self.X[l]) / (self.x - self.y))**2
        # else:
        #     k, l = {1, 2, 3, 4} - {i, j}
        #     return self.d[i, l]*self.d[j, k] + self.U2(i, k)

    @starcall_lazify
    def U2(self, i: int, j: int) -> _T:
        return self.U[i, j]**2

    @starcall_lazify
    def U2nu(self, i: int, nu: int) -> _T:
        # C99, (4.15)
        j, k, l = self.idx_set - {i}
        return self.U2[i, j] - self.xmy2 * self.d[i, k] * self.d[i, l] * self.d[j, nu] / self.d[i, nu]

    @starcall_lazify
    def S2(self, i: int, nu: int) -> _T:
        # # TODO: S.real <= 0 ....
        j, k, l = self.idx_set - {i}
        # C88, (2.5)
        return self.Q2[i, nu] + self.xmy2 * self.d[j, nu]*self.d[k, nu]*self.d[l, nu]/self.d[i, nu]
        # C99, (4.16)
        # return (
        #     self.X[j]*self.X[k]*self.X[l] / self.X[i] * self.Y[nu]**2
        #     + self.Y[j]*self.Y[k]*self.Y[l] / self.Y[i] * self.X[nu]**2
        # )**2

    @starcall_lazify
    def Q2(self, i: int, nu: int) -> _T:
        # C99, (4.18)
        return (self.X[nu] * self.Y[nu] / (self.X[i] * self.Y[i]))**2 * self.U2nu[i, nu]

    @cached_property
    def U2xyz(self):
        return self.U2[0, 1], self.U2[0, 2], self.U2[1, 2]

    @abstractmethod
    @starcall_lazify
    def I1(self) -> _T: ...

    @abstractmethod
    @starcall_lazify
    def I2(self, i: int, j: int) -> _T: ...

    @abstractmethod
    @starcall_lazify
    def I3(self, i: int, nu: int) -> _T: ...


    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        for m in (cls.I2, cls.I3):
            if not getattr(m, '__isabstractmethod__', False) and not getattr(m, '_lazified', False):
                _m = starcall_lazify(m)
                _m.__set_name__(cls, m.__name__)
                setattr(cls, _m.attrname, _m)



class SymbolicER(BaseEllipticReduction, ABC):
    @cached_property
    def idx_set(self):
        return set(sym.symbols('i, j, k, l', positive=True, integral=True))

    @starcall_lazify
    def d(self, i: int, j: int):
        return sym.Indexed(sym.Symbol('d'), i, j)

    @cached_property
    def X(self):
        return LazyDict(lambda i: sym.Indexed(sym.Symbol('X'), i))

    @cached_property
    def Y(self):
        return LazyDict(lambda i: sym.Indexed(sym.Symbol('Y'), i))

    @starcall_lazify
    def U(self, i: int, j: int) -> _T:
        return sym.Indexed(sym.Symbol('U'), i, j)

    @cached_property
    def symbolic_I1(self):
        return 2 * self.xmy * sym.Symbol('R_F')

    @starcall_lazify
    def symbolic_I2(self, i, j):
        k, l = self.idx_set - {i, j}
        return 2 * self.xmy * (
            self.d[i, k] * self.d[i, l] / 3
            * self.xmy2 * sym.Function('R_D')(self.U2[i, k], self.U2[i, l], self.U2[i, j])
            + self.X[i] * self.Y[i] / (self.X[j] * self.Y[j]) / self.U[i, j]
        )

    @starcall_lazify
    def symbolic_I3(self, i: int, nu: int):
        if self.m == 3 and nu < 0:
            return self.symbolic_I2[i, nu]

        j, k, l = self.idx_set - {i}
        return 2 * self.xmy * (
            self.d[i, j] * self.d[i, k] * self.d[i, l] / self.d[i, nu] / 3
                * self.xmy2 * sym.Function('R_J')(i, nu)
            + sym.Function('R_C')(i, nu)
        )

    @cached_property
    def I1(self):
        return sym.Symbol('I_1')

    def I2(self, i: int, j: int):
        return sym.Function('I_2')(i, j)

    def I3(self, i: int, nu: int):
        return sym.Function('I_3')(i, nu)


class NumericER(BaseEllipticReduction, ABC):
    import mpmath as _math_base

    elliprc: ClassVar[Callable[[_T, _T], _T]] = staticmethod(_math_base.elliprc)
    elliprd: ClassVar[Callable[[_T, _T, _T], _T]] = staticmethod(_math_base.elliprd)
    elliprf: ClassVar[Callable[[_T, _T, _T], _T]] = staticmethod(_math_base.elliprf)
    elliprj: ClassVar[Callable[[_T, _T, _T, _T], _T]] = staticmethod(_math_base.elliprj)

    @cached_property
    def I1(self):
        return 2 * self.xmy * self.elliprf(*self.U2xyz)

    @starcall_lazify
    def I2(self, i: int, j: int):
        k, l = self.idx_set - {i, j}
        return 2 * self.xmy * (
            self.d[i, k] * self.d[i, l] / 3
            * self.xmy2 * self.elliprd(self.U2[i, k], self.U2[i, l], self.U2[i, j])
            + self.X[i] * self.Y[i] / (self.X[j] * self.Y[j]) / self.U[i, j]
        )

    @starcall_lazify
    def I3(self, i: int, nu: int):
        if self.m == 3 and nu < 0:
            return self.I2[i, nu]

        j, k, l = self.idx_set - {i}
        return 2 * self.xmy * (
            self.d[i, j] * self.d[i, k] * self.d[i, l] / self.d[i, nu] / 3
            * self.xmy2 * self.elliprj(*self.U2xyz, self.U2nu[i, nu])
            + self.elliprc(self.S2[i, nu], self.Q2[i, nu])
        )


class PPER(BaseEllipticReduction, ABC):
    def v(self, z: _T, p: Iterable[int] = None, *args):
        return product(self._s(i, z)**(_p/2) for i, _p in enumerate(p))


class G02ER(PPER, ABC):
    @cached_property
    def tau(self) -> tuple[Number]:
        return (1/2,) + (self.m-1)*(-3/2,) + (self.n-self.m)*(-1/2,)

    def rec_A(self, p: Array, i: int):
        p_add_i = p.add(i)
        return sum(
            _p * self.d[j, i] * self[p.sub(j)] + 2 * self.A(p_add_i)
            for j, _p in enumerate(p) if j != i
        ) / (sum(p) + 2) / self.b[i]

    def rec_B(self, p: Array, i: int, j: int):
        return (self.b[j] * self[p.add(i)] - self.b[i] * self[p.add(j)]) / self.d[i, j]

    def rec_C(self, p: Array, i: int, j: int):
        p_sub_i = p.sub(i)
        return (self.b[i] * self[p_sub_i.add(j)] + self.d[i, j] * self[p_sub_i]) / self.b[j]

    def rec_D(self, p: Array, i: int, j: int, k: int):
        p_sub_k = p.sub(k)
        return (
            self.d[i, k] * self[p_sub_k.add(j)]
            - self.d[j, k] * self[p_sub_k.add(i)]
        ) / self.d[i, j]

    def rec_A1(self, p: Array, i: int, j: int):
        p_add_j = p.add(j)
        return (
            (sum(p) + 4) * self.b[i] * self[p_add_j] - 2*self.A(p_add_j.add(i))
            - sum(_p * self.d[k, i] * self[p_add_j.sub(k)]
                  for k, _p in enumerate(p) if k != i and k != j)
        ) / self.d[j, i] / (p[j] + 2)

    def rec_AC(self, p: Array, i: int, j: int):
        p_sub_j = p.sub(j)
        return (
            p[j] * self.d[j, i] * self[p_sub_j] + 2*self.A(p.add(i))
            + sum(_p * self.d[k, i] / self.b[k] * (self.b[j] * self[p_sub_j] + self.d[j, k] * self[p_sub_j.sub(k)])
                  for k, _p in enumerate(p) if k != i and k != j)
        ) / (sum(p) + 2) / self.b[i]

    def __getitem__(self, p: Sequence[int]):
        assert len(p) == self.n
        p = np.asarray(p).view(Array)  # type: Array

        eps = p - self.tau
        high, low = sum(eps > 1), sum(eps < -1)
        s1, sn, sn1 = itemgetter(0, -1, -2)(argsort(eps)[::-1])

        if high >= self.n-1 and sum(p) != -2:
            return self.rec_A(p, sn)
        if low == 1 and p[sn] != -2 and (high >= self.n-2 or eps[sn] < -2):
            return self.rec_A1(p, sn1, sn)
        if high >= 1:
            if low >= 2:
                return self.rec_D(p, sn1, sn, s1)
            if low >= 1:
                return self.rec_C(p, s1, sn)
        if low >= 2:
            return self.rec_B(p, sn1, sn)
        if high >= 1 and low == 0 and sum(p) != -2:
            return self.rec_AC(p, sn, s1)

        return self.C(p)

    def C(self, p: Array):
        err = NotABasicIntegralError(p)

        i = only(locate(p[:self.m] > 0), None, too_long=err)
        if (nu := only(locate(p[self.m:]), None, too_long=err)) is not None:
            if i is None or p.__getitem__(nu := nu +self.m) != -2:
                raise err
            return self.I3[i, nu]
        else:
            p = p[:self.m]
            if Counter(p) == {1: 1, -1: self.m - 2, -3: 1}:
                return self.I2[i, next(locate(p == -3))]
            if all(_ in (1, -1) for _ in p):
                if i is None:
                    return self.I1
                else:
                    return self.I3[i, -1]

        raise err


class SymbolicG02ER(SymbolicER, G02ER):
    def A(self, p: Array) -> _T:
        return sym.Function('A')(*p)


class NumericG02ER(NumericER, G02ER):
    pass


# a = (0.3, 0.5, 0.7, 0.9)
# b = (0.3, 0.1, -0.1, -0.3)
# er = NumericG02ER(2., 0.5, a, b, m=3)
# print(er[1, 1, -1, -4])

cls = SymbolicG02ER
a = take(3, sym.numbered_symbols('a', start=1)) + [1]
x, y = sym.symbols('x, y')

# cls = NumericG02ER
# a = (1, 2, 3, 5)
# x, y = 17, 3

er = cls(x, y, a, m=len(a)-1)  # type: G02ER
res = er[er.m*(-1,) + (-2,)]
res = sum(_.factor() for _ in res.expand().collect((er.I1, er.I2[0, 1], er.I2[0, 2], er.I2[0, 3], er.I3[0, -1])).args)
print(res)

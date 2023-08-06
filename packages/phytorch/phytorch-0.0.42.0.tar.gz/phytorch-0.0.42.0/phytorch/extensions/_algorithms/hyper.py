from cmath import exp, inf, isinf, nan, pi, sin, sqrt
from math import log2
from typing import Callable, TypeAlias

import mpmath as mp

from .common import EPS, is_int, is_nonpositive_int, is_real_nonpositive, PREC, sign
from .gamma import gamma


NoConvergence = mp.fp.NoConvergence

vc: TypeAlias = list[complex]

term_t: TypeAlias = tuple[
    vc,  # w: len=l_r
    vc,  # c: len=l_r
    vc,  # alpha: len=m_r
    vc,  # beta:  len=n_r
    vc,  # a: len=p_r
    vc,  # b: len=q_r
    complex,  # z
]
series_return_t: TypeAlias = list[term_t]  # len=N


def nint_distance(x: complex):
    return (n := round(x.real)), log2(abs(x-n)) if x != n else -inf



def hypsum(p: int, q: int, args: vc, z: complex, *, maxterms):
    a_s, b_s = args[:p], args[p:p+q]
    s = t = 1
    for k in range(maxterms):
        for a in a_s: t *= (a + k)
        for b in b_s: t /= (b + k)
        t /= k+1; t *= z; s+= t
        if abs(t) < EPS: return s
    raise NoConvergence


# def hypsum(p: int, q: int, args: vc, z: complex, *, maxterms):
#     return complex(mp.fp.hypsum(p, q, (p+q)*('C',), args, z, maxterms=maxterms))


def _hyp0f1_series(b: complex, z: complex) -> series_return_t:
    jw = sqrt(-z) * 1j
    u = 1 / (4 * jw)
    c = 0.5 - b
    E = exp(2 * jw)
    return [
        ([-jw, E], [c, -1], [], [], [b - 0.5, 1.5 - b], [], -u),
        ([jw, E], [c, 1], [], [], [b - 0.5, 1.5 - b], [], u)
    ]


def hyp0f1(b: complex, z: complex, *, force_series, maxterms) -> complex:
    if abs(z) > 2**7 and not force_series:
        try:
            return gamma(b)/(2*sqrt(pi)) * hypercomb(lambda params: _hyp0f1_series(b, z), [], force_series=True, maxterms=maxterms)
        except NoConvergence:
            if force_series:
                raise
    return hypsum(0, 1, [b], z, maxterms=maxterms)


def hyp1f0(a: complex, z: complex, *, force_series, maxterms) -> complex:
    return (1-z)**(-a)


def _hyp1f1_series(z: complex, params: vc) -> series_return_t:
    a, b = params
    E = exp(1j*pi*(-a if z.imag < 0 else a))
    return [
        ([E, z], [1, -a], [b], [b-a], [a, 1+a-b], [], -1/z),
        ([exp(z), z], [1, a-b], [b], [a], [b-a, 1-a], [], 1/z)
    ]


def hyp1f1(a: complex, b: complex, z: complex, *, force_series, maxterms) -> complex:
    if not z:
        return 1
    if abs(z) > 2**6 and not is_nonpositive_int(a):
        if isinf(z):
            if sign(a) == sign(b) == sign(z) == 1:
                return inf
            return nan * z
        try:
            return hypercomb(lambda params: _hyp1f1_series(z, params), [a, b], force_series=True, maxterms=6000)
        except NoConvergence:
            if force_series:
                raise
    return hypsum(1, 1, [a, b], z, maxterms=maxterms)


def _hyp1f2_series(z: complex, params: vc) -> series_return_t:
    a, b1, b2 = params
    X = (a - b1 - b2) / 2 + 0.25

    c = [1, 2 * ((3*a+b1+b2-2)*(a-b1-b2)/4 + b1*b2-3/16)]

    s1 = 0
    s2 = 0
    k = 0
    wprev = 0

    while True:
        if k >= 2:
            uu1 = 3*k**2 + (-6*a + 2*b1 + 2*b2 - 4) * k + 3*a**2 - (b1-b2)**2 - 2*a * (b1+b2-2) + 0.25
            uu2 = (k-a+b1-b2-0.5) * (k-a-b1+b2-0.5) * (k-a+b1+b2-2.5)
            c[k % 2] = 1 / (2*k) * (uu1 * c[(k-1) % 2] - uu2 * c[(k-2) % 2])
        w = 2**(-k) * c[k % 2] * (-z)**(-0.5 * k)
        if abs(w) < 0.1 * EPS:
            S = exp(1j * (pi*X + 2*sqrt(-z)))
            S = s1 * S + s2 / S
            return [
                ([S/2, pi, -z], [1, -0.5, X], [b1, b2], [a], [], [], 0),
                ([-z], [-a], [b1, b2], [b1-a, b2-a], [a, a-b1+1, a-b2+1], [], 1/z)
            ]

        # Quit if the series doesn't converge quickly enough
        if k > 5 and abs(wprev) / abs(w) < 1.5:
            raise NoConvergence

        s1 += (-1j)**k * w
        s2 += 1j**k * w
        wprev = w
        k += 1


def hyp1f2(a: complex, b1: complex, b2: complex, z: complex, *, force_series, maxterms) -> complex:
    absz = abs(z)
    if not force_series and absz >= 2**19 and absz**0.5 > 1.5* PREC:
        try:
            return hypercomb(lambda params: _hyp1f2_series(z, params), [a, b1, b2], force_series=True, maxterms=4 * PREC)
        except NoConvergence:
            if force_series:
                raise
    return hypsum(1, 2, [a, b1, b2], z, maxterms=maxterms)


def _hyp2f0_series(z: complex, params: vc) -> series_return_t:
    a, b = params
    w = sin(pi*b)
    rz = -1 / z
    return [
        ([pi, w, rz], [1, -1, a], [], [1+a-b, b], [a], [b], rz),
        ([-pi, w, rz], [1, -1, 1+a-b], [], [a, 2-b], [1+a-b], [2-b], rz)
    ]


def hyp2f0(a: complex, b: complex, z: complex, *, force_series, maxterms) -> complex:
    # We want to try aggressively to use the asymptotic expansion,
    # and fall back only when absolutely necessary
    try:
        return hypsum(2, 0, [a, b], z, maxterms=PREC)
    except NoConvergence:
        if force_series:
            raise
    return hypercomb(lambda params: _hyp2f0_series(z, params), [a, 1+a-b], force_series=force_series, maxterms=maxterms)


def _hyp2f1_zerodiv(a: complex, b: complex, c: complex):
    return is_nonpositive_int(c) and not (
            (is_nonpositive_int(a) and c.real <= a.real) or
            (is_nonpositive_int(b) and c.real <= b.real))


def _hyp2f1_series1(c: complex, z: complex, params: vc) -> series_return_t:
    a, b = params
    return [
        ([-z], [-a], [c, b-a], [b, c-a], [a, 1-c+a], [1+a-b], 1/z),
        ([-z], [-b], [c, a-b], [a, c-b], [b, 1-c+b], [1+b-a], 1/z)
    ]


def _hyp2f1_series2(c: complex, z: complex, params: vc) -> series_return_t:
    a, b = params
    return [
        ([], [], [c, c-a-b], [c-a, c-b], [a,b], [1-c+a+b], 1-z),
        ([1-z], [c-a-b], [c, a+b-c], [a, b], [c-a, c-b], [1+c-a-b], 1-z)
    ]


def _hyp2f1_gosper(a: complex, b: complex, c: complex, z: complex) -> complex:
    abz = a * b * z
    nz = 1 - z
    g = z / nz
    abg = a * b * g
    z2 = z - 2
    ch = c / 2
    c1h = (c + 1) / 2
    cba = c - b - a

    tol = log2(abs(EPS)) - 10
    maxprec = 100 * PREC
    extra = 10

    while True:
        maxmag = -inf
        d, e, f = 0, 1, 0
        k = 0
        while True:
            kch = k + ch
            kakbz = (k+a)*(k+b)*z / (4*(k+1)*kch*(k+c1h))
            d1 = kakbz*(e-(k+cba)*d*g)
            e1 = kakbz*(d*abg+(k+c)*e)
            ft = d*(k*(cba*z+k*z2-c)-abz)/(2*kch*nz)
            f1 = f + e - ft
            maxmag = max(maxmag, log2(abs(f1)))

            if log2(abs(f1 - f)) < tol:
                break

            d, e, f = d1, f1, e1

            k += 1

        cancellation = maxmag - log2(abs(f1))
        if cancellation < extra:
            break
        else:
            extra += cancellation
            if extra > maxprec:
                raise mp.fp.NoConvergence

    return f1


def hyp2f1(a: complex, b: complex, c: complex, z: complex, *, force_series, maxterms) -> complex:
    if z==1:
        return (
            gamma(c) * gamma(c - a - b) / gamma(c - a) / gamma(c - b)
            if ((c-a-b).real > 0 or is_nonpositive_int(a) or is_nonpositive_int(b)) and not _hyp2f1_zerodiv(a, b, c)
            else inf
        )
    if z==0:
        return 1 if c != 0 or a == 0 or b == 0 else nan
    if _hyp2f1_zerodiv(a, b, c):
        return inf
    if (abs(z) <= 0.8
        or (is_real_nonpositive(a) and is_int(a) and -1000 <= a.real <= 0)
        or (is_real_nonpositive(b) and is_int(b) and -1000 <= b.real <= 0)):
        return hypsum(2, 1, [a, b, c], z, maxterms=maxterms)
    if abs(z) >= 1.3:
        return hypercomb(lambda params: _hyp2f1_series1(c, z, params), [a, b], force_series=force_series, maxterms=maxterms)
    elif abs(1-z) <= 0.75:
        return hypercomb(lambda params: _hyp2f1_series2(c, z, params), [a, b], force_series=force_series, maxterms=maxterms)
    elif abs(z/(z-1)) <= 0.75:
        return hyp2f1(a, c-b, c, z/(z-1), force_series=force_series, maxterms=maxterms) / (1-z)**a
    else:
        return _hyp2f1_gosper(a, b, c, z)


def _hyp2f2_series(z: complex, params: vc) -> series_return_t:
    a1, a2, b1, b2 = params
    X = a1 + a2 - b1 - b2
    A2 = a1 + a2
    B2 = b1 + b2
    c = [1, (A2 - 1) * X + b1*b2 - a1*a2]

    s = 0
    k = 0
    tprev = 0

    while True:
        if k >= 2:
            uu1 = 1 - B2 + 2*a1 + a1**2 + 2*a2 + a2**2 - A2*B2 + a1*a2 + b1*b2 + (2*B2 - 3 * (A2 + 1)) * k + 2*k**2
            uu2 = (k - A2 + b1 - 1) * (k - A2 + b2 - 1) * (k - X - 2)
            c[k % 2] = 1 / k * (uu1 * c[(k-1) % 2] - uu2 * c[(k-2) % 2])
        t = c[k % 2] * z**(-k)
        if abs(t) < 0.1 * EPS:
            S = exp(z) * s
            return [
                ([z, S], [X, 1], [b1, b2], [a1, a2], [], [], 0),
                ([-z], [-a1], [b1, b2, a2-a1], [a2, b1-a1, b2-a1], [a1, a1-b1+1, a1-b2+1], [a1-a2+1], -1/z),
                ([-z], [-a2], [b1, b2, a1-a2], [a1, b1-a2, b2-a2], [a2, a2-b1+1, a2-b2+1], [a2-a1+1], -1/z)
            ]

        # Quit if the series doesn't converge quickly enough
        if k > 5 and abs(tprev) / abs(t) < 1.5:
            raise mp.fp.NoConvergence

        s += t
        tprev = t
        k += 1


def hyp2f2(a1: complex, a2: complex, b1: complex, b2: complex, z: complex, *, force_series, maxterms) -> complex:
    if not force_series and abs(z) > 2**2:
        try:
            return hypercomb(lambda params: _hyp2f2_series(z, params), [a1, a2, b1, b2], force_series=True, maxterms=4 * PREC)
        except NoConvergence:
            if force_series:
                raise
    return hypsum(2, 2, [a1, a2, b1, b2], z, maxterms=maxterms)


def _hyp2f3_series(z: complex, params: vc) -> series_return_t:
    a1, a2, b1, b2, b3 = params
    X = (a1 + a2 - b1 - b2 - b3) / 2 + 0.25
    A2 = a1 + a2
    B3 = b1 + b2 + b3
    A = a1*a2
    B = b1*b2 + b3*b2 + b1*b3
    R = b1*b2*b3

    c1 = 2 * (B - A + (3 * A2 + B3 - 2) * (A2 - B3) / 4 - 3/16)

    c = [
        1,
        c1,
        c1**2 / 2 + (-16 * (2 * A2 - 3) * (B - A) / 16 + 32 * R + 4 * (-8 * A2**2 + 11 * A2 + 8 * A + B3 - 2) * (A2 - B3) - 3) / 16
    ]
    s1 = 0
    s2 = 0
    k = 0
    wprev = 0

    while True:
        if k >= 3:
            uu1 = (k - 2*X - 3) * (k - 2*X - 2*b1 - 1) * (k - 2*X - 2*b2 - 1) * (k - 2*X - 2*b3 - 1)
            uu2 = (4*(k-1)**3 - 6*(4*X+B3)*(k-1)**2 + 2*(24*X**2+12*B3*X+4*B+B3-1)*(k-1) - 32*X**3 - 24*B3*X**2 - 4*B - 8*R - 4*(4*B+B3-1)*X + 2*B3-1)
            uu3 = (5*(k-1)**2 + 2 * (-10*X + A2 - 3*B3 + 3) * (k-1) + 2*c1)
            c[k%3] = 1/(2*k) * (
                uu1*c[(k-3) % 3]
                - uu2*c[(k-2) % 3]
                + uu3*c[(k-1) % 3]
            )
        w = 2**(-k) * c[k % 3] * (-z)**(-0.5 * k)
        if abs(w) < 0.1 * EPS:
            S = exp(1j * (pi*X + 2*sqrt(-z)))
            S = s1 * S + s2 / S
            return [
                ([0.5 * S, pi, -z], [1, -0.5, X], [b1, b2, b3], [a1, a2], [], [], 0),
                ([-z], [-a1], [b1, b2, b3, a2-a1], [a2, b1-a1, b2-a1, b3-a1], [a1, 1+a1-b1, 1+a1-b2, 1+a1-b3], [1+a1-a2], 1 / z),
                ([-z], [-a2], [b1, b2, b3, a1-a2], [a1, b1-a2, b2-a2, b3-a2], [a2, 1+a2-b1, 1+a2-b2, 1+a2-b3], [1-a1+a2], 1 / z)
            ]

        # Quit if the series doesn't converge quickly enough
        if k > 5 and abs(wprev) / abs(w) < 1.5:
            raise mp.fp.NoConvergence

        s1 += (-1j)**k * w
        s2 += 1j**k * w
        wprev = w
        k += 1


def hyp2f3(a1: complex, a2: complex, b1: complex, b2: complex, b3: complex, z: complex, *, force_series, maxterms) -> complex:
    if not force_series and abs(z) > 2**18 and abs(z)**0.5 > 1.5* PREC:
        try:
            return hypercomb(lambda params: _hyp2f3_series(z, params), [a1, a2, b1, b2, b3], force_series=True, maxterms=4 * PREC)
        except NoConvergence:
            if force_series:
                raise
    return hypsum(2, 3, [a1, a2, b1, b2, b3], z, maxterms=maxterms)


# def hypq1fq(p: int, q: int, a_s: vc, b_s: vc, z: complex, *, force_series, maxterms):
#     ispoly = False
#     for a in a_s:
#         if is_nonpositive_int(a):
#             ispoly = True
#             break
#
#     # Direct summation
#     if abs(z) < 1 and ispoly:
#         return hypsum(p, q, a_s+b_s, z, maxterms=maxterms)
#     if z==1:
#         S = (sum(a_s) + sum(b_s)).real
#         if S <= 0:
#             return hyper(a_s, b_s, 0.9, force_series=force_series, maxterms=maxterms) * inf
    # if p==3 and q==2 and abs(z-1) < 0.05:
    # if abs(z) < 1.1 and z.real <= 1:


def hyper(a_s: vc, b_s: vc, z: complex, *, force_series, maxterms) -> complex:
    p = len(a_s)
    q = len(b_s)

    # TODO: Reduce degree by eliminating common parameters

    # Handle special cases
    if p == 0:
        if q == 0: return exp(z)
        if q == 1: return hyp0f1(b_s[0], z, force_series=force_series, maxterms=maxterms)
    elif p == 1:
        if q == 0: return hyp1f0(a_s[0], z, force_series=force_series, maxterms=maxterms)
        if q == 1: return hyp1f1(a_s[0], b_s[0], z, force_series=force_series, maxterms=maxterms)
        if q == 2: return hyp1f2(a_s[0], b_s[0], b_s[1], z, force_series=force_series, maxterms=maxterms)
    elif p == 2:
        if q == 0: return hyp2f0(a_s[0], a_s[1], z, force_series=force_series, maxterms=maxterms)
        if q == 1: return hyp2f1(a_s[0], a_s[1], b_s[0], z, force_series=force_series, maxterms=maxterms)
        if q == 2: return hyp2f2(a_s[0], a_s[1], b_s[0], b_s[1], z, force_series=force_series, maxterms=maxterms)
        if q == 3: return hyp2f3(a_s[0], a_s[1], b_s[0], b_s[1], b_s[2], z, force_series=force_series, maxterms=maxterms)
    # elif p == q+1:
    #     return hypq1fq(p, q, a_s, b_s, z)
    # elif p > q+1 and not force_series:
    #     return hyp_borel(p, q, a_s, b_s, z)

    return hypsum(p, q, a_s+b_s, z, maxterms=maxterms)


def _check_need_perturb(terms: series_return_t):
    perturb = False
    discard = []

    for term_index, term in enumerate(terms):
        w_s, c_s, alpha_s, beta_s, a_s, b_s, z = term
        have_singular_nongamma_weight = False
        # Avoid division by zero in leading factors
        # TODO: near divisions by zero
        for k, w in enumerate(w_s):
            if abs(w) < 2* EPS:
                if c_s[k].real <= 0 and c_s[k]:
                    perturb = True
                    have_singular_nongamma_weight = True
        pole_count = [0, 0, 0]
        # Check for gamma and series poles and near-poles
        for data_index, data in enumerate([alpha_s, beta_s, b_s]):
            for x in data:
                n, d = nint_distance(x)
                # Poles
                if n > 0:
                    continue
                elif d == -inf:
                    # OK if we have a polynomial
                    # ------------------------------
                    ok = False
                    if data_index == 2:
                        for u in a_s:
                            if u and u.real >= int(n):
                                ok = True
                                break
                    if ok:
                        continue
                    pole_count[data_index] += 1
        if pole_count[1] > pole_count[0] + pole_count[2] and not have_singular_nongamma_weight:
            discard.append(term_index)
        elif sum(pole_count):
            perturb = True
    return perturb, discard


def hypercomb(function: Callable[[vc], series_return_t], params: vc, *, force_series, maxterms):
    params = params[:]
    terms = function(params)

    perturb, discard = _check_need_perturb(terms)
    if perturb:
        h = 2**(-int(PREC * 0.3))
        for k in range(len(params)):
            params[k] += h
            # Heuristically ensure that the perturbations
            # are "independent" so that two perturbations
            # don't accidentally cancel each other out
            # in a subtraction.
            h += h / (k + 1)
        terms = function(params)
    terms = [term for (i, term) in enumerate(terms) if i not in discard]

    evaluated_terms = []
    for term in terms:
        print(term)
        w_s, c_s, alpha_s, beta_s, a_s, b_s, z = term
        v = hyper(a_s, b_s, z, force_series=force_series, maxterms=maxterms)
        for a in alpha_s:
            v *= gamma(a)
        for b in beta_s:
            v /= gamma(b)
        for w, c in zip(w_s, c_s):
            v *= w**c
        evaluated_terms.append(v)

    print(evaluated_terms)

    return sum(evaluated_terms)

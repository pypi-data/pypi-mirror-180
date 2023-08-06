from cmath import atan, inf, isinf, isnan, log, nan, pi, sin, sqrt

from .common import are_conjugate, EPS, is_real_nonnegative


def csc2(phi: complex):
    s = sin(phi)
    return inf if s == 0 else s**(-2)


def elliprc(x: complex, y: complex):
    if isinf(x) or isinf(y): return 1 / (x*y)
    if not y: return inf
    if not x: return pi/2 / sqrt(y)

    # TODO: handle x=y in elliprc better
    if sqrt(1-x/y) == 0:
        return 1 / (6 * sqrt(y))

    # principal value
    if not y.imag and y.real < 0:
        return sqrt(x / (x-y)) * elliprc(x-y, -y)

    v = sqrt(x) / sqrt(y)
    return (pi/2 + 1j*log(v*1j + sqrt(1 - v*v))) / (sqrt(1 - x/y) * sqrt(y))


def elliprj(x, y, z, p):
    if isnan(x) or isnan(y) or isnan(z) or isnan(p): return x * y * z
    if isinf(x) or isinf(y) or isinf(z) or isinf(p): return 0
    if not p or ((not x) + (not y) + (not z) > 1): return inf

    if not (
        (x.real >= 0 and y.real >= 0 and z.real >= 0 and p.real > 0)
        or (p and (
            (is_real_nonnegative(x) and is_real_nonnegative(y) and is_real_nonnegative(z))
            or (is_real_nonnegative(x) and are_conjugate(y, z) and y)
            or (is_real_nonnegative(y) and are_conjugate(z, x) and z)
            or (is_real_nonnegative(z) and are_conjugate(x, y) and x)
        ))
        or (x == p or y == p or z == p)  # last paragraph of algorithm
    ):
        print('Carlson\'s elliprj algorithm not guaranteed.'
              # ' Chickening out!'
              ' But nobody calls me chicken!'
              )
        # return nan

    xm, ym, zm, pm = x, y, z, p
    A0 = Am = (x + y + z + p + p) / 5
    delta = (p-x) * (p-y) * (p-z)
    Q = (0.25 * EPS * 2**10)**(-1/6) * max(abs(A0-x), abs(A0-y), abs(A0-z), abs(A0-p))

    pow4 = 1
    s = 0
    m = 0
    while pow4 * Q >= abs(Am):
        sx, sy, sz, sp = map(sqrt, (xm, ym, zm, pm))
        lm = sx*sy + sx*sz + sy*sz
        xm, ym, zm, pm, Am = map(lambda _: (_ + lm) / 4, (xm, ym, zm, pm, Am))
        dm = (sp + sx) * (sp + sy) * (sp + sz)
        em = delta * 4**(-3*m) / (dm*dm)
        s += atan(sqrt(em)) / em * pow4 / dm
        pow4 /= 4
        m += 1

    t = pow4 / Am
    X, Y, Z = map(lambda _: (A0 - _) * t, (x, y, z))
    P = (-X-Y-Z) / 2
    E2 = X*Y + X*Z + Y*Z - 3*P*P
    E3 = X*Y*Z + 2*E2*P + 4*P*P*P
    E4 = (2*X*Y*Z + E2*P + 3*P*P*P) * P
    E5 = X*Y*Z*P*P

    return 6*s + pow4 / Am / sqrt(Am) * (
        1 - 3/14 * E2 + E3/6 + 9/88 * E2*E2
        - 3/22 * E4 - 9/52 * E2*E3 + 3/26 * E5
    )


    # m = 0
    # g = 0.25
    # pow4 = 1
    # S = 0
    # while 1:
    #     sx = sqrt(xm)
    #     sy = sqrt(ym)
    #     sz = sqrt(zm)
    #     sp = sqrt(pm)
    #     lm = sx*sy + sx*sz + sy*sz
    #     Am1 = (Am + lm) * g
    #     xm = (xm + lm) * g
    #     ym = (ym + lm) * g
    #     zm = (zm + lm) * g
    #     pm = (pm + lm) * g
    #     dm = (sp + sx) * (sp + sy) * (sp + sz)
    #     em = delta * 4**(-3*m) / dm**2
    #     if pow4 * Q < abs(Am):
    #         break
    #     T = elliprc(1, 1+em) * pow4 / dm
    #     S += T
    #     pow4 *= g
    #     m += 1
    #     Am = Am1

    # t = 2**(-2*m) / Am
    # X = (A0 - x) * t
    # Y = (A0 - y) * t
    # Z = (A0 - z) * t
    # P = (-X - Y - Z) / 2
    # E2 = X*Y + X*Z + Y*Z - 3 * P**2
    # E3 = X*Y*Z + 2*E2*P + 4*P**3
    # E4 = (2*X*Y*Z + E2*P + 3*P**3) * P
    # E5 = X * Y * Z * P**2
    # P = 24024 - 5148*E2 + 2457*E2**2 + 4004*E3 - 4158*E2*E3 - 3276*E4 + 2772*E5
    # Q = 24024
    # v1 = g**m * Am**(-1.5) * P / Q
    # v2 = 6 * S
    # return v1 + v2

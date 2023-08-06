def roots2(b: complex, c: complex):
    if c==0:
        return 0, -b
    q = -(b + (1 if b.real >= 0 else -1) * (b*b - 4*c)**0.5) / 2
    return q, c/q


def roots3(b: complex, c: complex, d: complex):
    Q = (b*b - 3*c) / 9
    R = (2*b*b*b - 9*b*c + 27*d) / 54
    A = - (R + (1 if R.real >= 0 else -1) * (R*R - Q*Q*Q)**0.5)**(1/3)
    B = Q / A if A != 0 else 0
    return (
        A + B - b/3,
        -(A+B)/2 - b/3 + 1j * 3**0.5/2 * (A-B),
        -(A+B)/2 - b/3 - 1j * 3**0.5/2 * (A-B),
    )


def roots4_depressed(p, q, r):
    if q == 0:
        s1, s2 = (_**0.5 for _ in roots2(p, r))
        return s1, -s1, s2, -s2

    s1, s2 = (_**0.5 for _ in roots3(2*p, p*p-4*r, -q*q)[1:])
    s3 = -q / (s1*s2)

    return (s1+s2+s3) / 2, (s1-s2-s3) / 2, (s2-s1-s3) / 2, (s3-s1-s2) / 2


def roots4(b, c, d, e):
    return tuple(_ - b/4 for _ in roots4_depressed(
        (8*c - 3*b*b) / 8,
        (b*b*b - 4*b*c + 8*d) / 8,
        (-3*b*b*b*b + 256*e - 64*b*d + 16*b*b*c) / 256
    ))


def quartic_roots(a, b, c, d, e, eps=1e-10):
    a, b, c, d, e = map(complex, (a, b, c, d, e))

    twop = (8*a*c - 3*b**2) / (4*a**2)
    q = (b**3 - 4*a*b*c + 8*a**2*d) / (8*a**3)
    D0 = c**2 - 3*b*d + 12*a*e
    D1 = 2*c**3 - 9*b*c*d + 27*b**2*e + 27*a*d**2 - 72*a*c*e

    if abs(D0) < eps:
        if abs(D1) < eps:
            denom = 9*(8*a**2*d - 4*a*b*c + b**3)
            if abs(denom) < eps:
                x0 = 0
            else:
                x0 = (-72*a**2*e + 10*a*c**2 - 3*b**2*c) / denom
            x1 = -b/a - 3*x0
            return x0, x0, x0, x1
        else:
            Q = D1**(1/3)
    else:
        Q = (D1 + (D1**2 - 4 * D0**3)**0.5)**(1/3) / 2**(1/3)
    _S2 = ((Q + D0 / Q) / a - twop) / 12
    if abs(_S2) < eps:
        Q = Q * (-0.5 - 3**0.5 * 0.5j)
        S2 = ((Q + D0 / Q) / a - twop) / 12
    else:
        S2 = _S2
    fourS2mtwop = -4*S2 - twop
    S = S2**0.5
    qS = q / S
    pmp = (fourS2mtwop + qS)**0.5 / 2
    pmm = (fourS2mtwop - qS)**0.5 / 2
    mb4a = -b / (4*a)
    mb4apS = mb4a + S
    mb4amS = mb4a - S
    return mb4amS - pmp, mb4amS + pmp, mb4apS - pmm, mb4apS + pmm

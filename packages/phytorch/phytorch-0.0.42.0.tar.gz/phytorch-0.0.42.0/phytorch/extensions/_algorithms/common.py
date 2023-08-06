PREC = 53
EPS = 2.220446049250313e-16


def sign(z: complex):
    return abs(z) / z if z else 0


def is_real(x: complex):
    return not x.imag


def is_real_nonpositive(x: complex):
    return is_real(x) and x.real <= 0


def is_real_nonnegative(x: complex):
    return is_real(x) and x.real >= 0


def is_int(x: complex):
    return is_real(x) and int(x.real) == x.real


def is_nonpositive_int(x: complex):
    return is_int(x) and x.real <= 0


def are_conjugate(a: complex, b: complex):
    return not (a.imag + b.imag)

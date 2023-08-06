from cmath import exp, log, pi, sin, tan



_lanczos_g = 7
_lanczos_p = (
    0.99999999999980993, 676.5203681218851, -1259.1392167224028,
    771.32342877765313, -176.61502916214059, 12.507343278686905,
    -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7)


def gamma(z: complex):
    if z.real < 0.5:
        try:
            sinpiz = sin(pi*z)
        except ValueError:
            raise OverflowError from None
        return pi / (sinpiz * gamma(1-z))

    z -= 1
    r = (
        _lanczos_p[0]
        + _lanczos_p[1] / (z+1)
        + _lanczos_p[2] / (z+2)
        + _lanczos_p[3] / (z+3)
        + _lanczos_p[4] / (z+4)
        + _lanczos_p[5] / (z+5)
        + _lanczos_p[6] / (z+6)
        + _lanczos_p[7] / (z+7)
        + _lanczos_p[8] / (z+8)
    )
    t = z + _lanczos_g + 0.5
    return 2.506628274631000502417 * t**(z+0.5) * exp(-t) * r


def digamma(z: complex):
    if z.real < 0.5:
        return digamma(1-z) - pi / tan(pi * z)

    c = (
        0.99999999999999709182,
        57.156235665862923517,
        -59.597960355475491248,
        14.136097974741747174,
        -0.49191381609762019978,
        .33994649984811888699e-4,
        .46523628927048575665e-4,
        -.98374475304879564677e-4,
        .15808870322491248884e-3,
        -.21026444172410488319e-3,
        .21743961811521264320e-3,
        -.16431810653676389022e-3,
        .84418223983852743293e-4,
        -.26190838401581408670e-4,
        .36899182659531622704e-5
    )

    d = n = 0

    for k in range(14, 0, -1):
        dz = 1 / (z+k-1)
        dd = c[k] * dz
        d += dd
        n -= dd * dz

    d += c[0]

    return log(z + 607/128 - 0.5) + (n / d - (607/128) / (z + 607/128 - 0.5))

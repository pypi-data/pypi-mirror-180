from .hyper import hypercomb, series_return_t, vc


def meijerg_series1(m, n, p, q, z: complex, r: complex, args: vc) -> series_return_t:
    print(f'series 1: {m}, {n}, {p}, {q}')
    print(args)
    a = args[:p]
    b = args[p:]
    terms = [(
        [z],
        [b[k] / r],
        [b[j] - b[k] for j in range(m) if j != k] + [1 - a[j] + b[k] for j in range(n)],
        [a[j] - b[k] for j in range(n, p)] + [1 - b[j] + b[k] for j in range(m, q)],
        [1 - a[j] + b[k] for j in range(p)],
        [1 - b[j] + b[k] for j in range(q) if j != k],
        (-1)**(p - m - n) * z**(1 / r)
    ) for k in range(m)]
    print('\n'.join(map(str, terms)))
    return terms


def meijerg_series2(m, n, p, q, z: complex, r: complex, args: vc) -> series_return_t:
    a = args[:p]
    b = args[p:]
    return [(
        [z],
        [(a[k] - 1) / r],
        [a[k] - a[j] for j in range(n) if j != k] + [1 - a[k] + b[j] for j in range(m)],
        [a[k] - b[j] for j in range(m, q)] + [1 - a[k] + a[j] for j in range(n, p)],
        [1 - a[k] + b[j] for j in range(q)],
        [1 + a[j] - a[k] for j in range(p) if j != k],
        (-1)**(q - m - n) / z**(1 / r)
    ) for k in range(n)]


def meijerg(an: vc, ap: vc, bm: vc, bq: vc, z: complex, r: complex = 1., *, force_series=False, maxterms=6000):
    n = len(an)
    p = n + len(ap)
    m = len(bm)
    q = m + len(bq)

    series = 1 if p < q else 2 if p > q else 2 if m + n == p and abs(z) > 1 else 1

    return hypercomb(lambda params: (meijerg_series1 if series == 1 else meijerg_series2)(m, n, p, q, z, r, params), an+ap+bm+bq, force_series=force_series, maxterms=maxterms)


def Tgamma(m: int, a: complex, z: complex):
    return meijerg([], (m-1)*[0], [a-1] + (m-1)*[-1], [], z)

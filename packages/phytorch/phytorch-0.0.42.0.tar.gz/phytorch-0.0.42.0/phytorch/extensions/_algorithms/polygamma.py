from cmath import cos, nan, pi, sin

import numpy as np
from scipy.special import gamma


g = 607/128
h = 0.5


def polygamma(n: int, z: complex):
    if z.real < 0:
        if n==0:
            c = [1, 0]
        elif n==1:
            c = [-1]
        else:
            c = np.array(abs(n-1)*[0] + [-1])
            for m in range(1, n):
                dc = [0] + list((c * np.arange(len(c)-1, -1, -1))[:-1])
                c = -(np.array(list((m+1) * c[1:]) + [0]) + np.array(dc) - np.array((dc[2:] + [0, 0])))

        return (-1)**n * polygamma(n, 1-z) - np.polyval(c, cos(pi * z)) * (sin(pi*z) / pi)**(-n-1)

    r = [-4.1614709798720630-.14578107125196249j, -4.1614709798720630+.14578107125196249j,
         -4.3851935502539474-.19149326909941256j, -4.3851935502539474+.19149326909941256j,
         -4.0914355423005926, -5.0205261882982271, -5.9957952053472399, -7.0024851819328395,
         -7.9981186370233868, -9.0013449037361806, -9.9992157162305535, -11.0003314815563886,
         -11.9999115102434217, -13.0000110489923175587]

    s = 0
    for k in range(len(r)-1, -1, -1):
        s += (z - r[k])**(-n - 1) - (z + k)**(-n - 1)
    zgh = z + (g-h)
    return (
        (-1)**(n + 1) * (
            gamma(n) * zgh**(-n)
            + gamma(n + 1) * zgh**(-n - 1) * g
        )
        + (-1)**n * gamma(n+1) * s)


# n = 16
# c = np.array(abs(n - 1) * [0] + [-1])
# for m in range(1, n):
#     dc = [0] + list((c * np.arange(len(c) - 1, -1, -1))[:-1])
#     c = -(np.array(list((m + 1) * c[1:]) + [0]) + np.array(dc) - np.array((dc[2:] + [0, 0])))
#     print(f'{tuple(c[-m-1:])},  \\')

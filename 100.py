"""
If a box contains twenty-one coloured discs, composed of fifteen blue
discs and six red discs, and two discs were taken at random, it can be
seen that the probability of taking two blue discs, P(BB) =
(15/21)(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of
taking two blue discs at random, is a box containing eighty-five blue
discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 =
1,000,000,000,000 discs in total, determine the number of blue discs
that the box would contain.

Solution
--------

Consider the sequence of (num, den) pairs such that num/den = 1/2. The
ration den_i+1 / den_i increases monotonically towards a fixed number
around 5.83. Each time we find a new num/den pair, we calculate the
factor den_i+1 / den_i, and multiply the current denominator by this
factor. This gives a (close) lower bound on the next denominator in
the sequence.
"""
from itertools import count

xx, dd = 1, 1
n, d = 15, 21
fac = 1. * 85 / 21
stop = 10**12
while True:
    dd = int(d * fac)
    for d in count(dd):
        a = 1
        b = -1
        c = (d - d**2) / 2
        x = -b + (b**2 - 4 * a * c)**0.5
        x /= 2 * a
        x = int(x)
        if (x**2 - x) * 2 == d**2 - d:
            fac = 1. * x / n
            break
    n = x
    if d > stop:
        print n
        break

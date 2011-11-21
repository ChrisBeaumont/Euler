"""Consider the fraction, n/d, where n and d are positive integers. If
nd and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending
order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of
3/7.

By listing the set of reduced proper fractions for d 1,000,000 in
ascending order of size, find the numerator of the fraction
immediately to the left of 3/7.


Solution:

We search backwards from denominators, calculating the fractions around 3/7.
We can stop once we find a denominator which can produce 3/7 exactly, because
any smaller denominator d2 will differ from 3/7 by at least 1/d2 > 1/d.
"""

from fraction import Fraction

fs = []
stop = 1000000 + 1
#stop = 8 + 1
for d in xrange(stop, 0, -1):
    lo = 3 * d / 7 - 1
    hi = min(lo + 3, d)
    for n in range(lo, hi):
        fs.append(Fraction(n, d))
        fs[-1].reduce()
    if (3 * d) % 7 == 0: break

fs = sorted(fs)
target = Fraction(3, 7)
for i in range(len(fs)):
    if fs[i] >= target:
        print fs[i-1].num
        break

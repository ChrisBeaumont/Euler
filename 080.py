"""
It is well known that if the square root of a natural number is not an
integer, then it is irrational. The decimal expansion of such square
roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital
sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the
digital sums of the first one hundred decimal digits for all the
irrational square roots.

Solution:
---------
Use integer math to find solution * 10**100
"""
def digital_sum(x):
    """ Use binary search to find the nearest integer solution 
    to sqrt(10**200 x). Then add the digits """

    if int(x**.5)**2 == x: return 0 # don't consider perfect squares

    target = x * 10 ** 200
    lo, hi = 1, target
    while (hi - lo > 1):
        mid = (lo + hi) / 2
        test = mid ** 2
        if test > target:
            hi = mid
        else:
            lo = mid

    # sum first 100 digits
    result = str(lo)[:100]
    result = sum(map(int, str(result)))

    return result

print sum(map(digital_sum, xrange(2, 101)))

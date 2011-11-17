
from util import gcd, isprime

""" Informal argument that the answer is the largest product of the
first n primes that is still below 1 million:

Want to maximize n / phi(n) -> maximize n, minimize phi

Every number is a product of primes.


n should be the product of non-repeated primes, since each prime x
knocks out a fraction ~ 1 / x of candidate relative primes regardless
of how many times it divides n

The lowest primes knock out the highest fraction of candidate relative
primes. Thus, multiplying the smallest primes will lead to large phi
and small n.
"""

top = 1000000
ps = filter(isprime, xrange(2, 100))
answer = 1
for p in ps:
    if answer * p < top:
        answer *= p

print answer

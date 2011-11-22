from operator import mul
from numpy import argmin

def totient(n, primes):
    num = reduce(mul, (p-1 for p in primes))
    den = reduce(mul, primes)
    return n * num / den

perm = lambda x,y: sorted(str(x)) == sorted(str(y))
top = 10**7

facs = [[] for i in xrange(top)]
for p in xrange(2, top):
    if facs[p]: continue
    for j in xrange(p, top, p):
        facs[j].append(p)

best = 1000
answer = None
for n in xrange(2, top):
    f = facs[n]
    phi = totient(n, f)
    nphi = 1. * n / phi
    if perm(n, phi) and nphi < best:
        best, answer = nphi, n
        print best, answer, phi

print answer

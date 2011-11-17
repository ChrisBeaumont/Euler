"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are
prime. The sum of these four primes, 792, represents the lowest sum
for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.

Solution:

Just a bunch of guess-and-checking of the first ~10K primes, with lots
of tests to skip unecessary loops. The upper bound of 10K was
discovered empirically -- it'd be nice to have a more robust solution
"""
from util import isprime


ps = filter(isprime, xrange(2, 8400))
ps.remove(2)
ps.remove(5)

best = ps[-1] * 5

def test(a, b):
    if not isprime(int(str(a) + str(b))): return False
    if not isprime(int(str(b) + str(a))): return False
    return True

for a in xrange(len(ps)):
    pa = ps[a]
    for b in xrange(a+1, len(ps)):
        pb = ps[b]
        if pa + pb * 4 > best: continue
        if not test(pa, pb): continue
        for c in xrange(b+1, len(ps)):
            pc = ps[c]
            if pa + pb + pc * 3 > best: continue
            if not test(pa, pc): continue
            if not test(pb, pc): continue
            for d in xrange(c+1, len(ps)):
                pd = ps[d]
                if pa + pb + pc + pd * 2 > best: continue
                if not test(pa, pd): continue
                if not test(pb, pd): continue
                if not test(pc, pd): continue
                for e in xrange(d+1, len(ps)):
                    pe = ps[e]
                    if pa + pb + pc + pd + pe > best: continue
                    if not test(pa, pe): continue
                    if not test(pb, pe): continue
                    if not test(pc, pe): continue
                    if not test(pd, pe): continue
                    best = pa + pb + pc + pd + pe
                    print best

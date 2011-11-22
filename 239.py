from operator import mul

def f(n, m, q):
    """ probability that, in a lineup of n integers, 
    the first m are in order, the next q are not """
    numerator = [n - m - i for i in range(1, q+1)]
    numerator = reduce(mul, numerator)
    
    denom = [n - m for i in range(1, q+1)]
    denom = reduce(mul, denom)
    denom *= n ** m

    return numerator, denom


#there are 25 primes below 100
n = 100
m = 3
q = 22
n, d = f(n, m, q)

#number of ways to choose 22 primes
perm = 25 * 24 * 23 / 6
answer = 1. * (perm * n) / d
print "%0.12f" % answer

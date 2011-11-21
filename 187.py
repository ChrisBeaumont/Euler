from util import firstprimes
from bisect import bisect_left

top = 10 ** 8
ps = firstprimes(top/2) #all primes < top/2

answer = 0
for i in xrange(len(ps)):
    if ps[i] ** 2 >= top: break
    #find maximum j >= i
    j = bisect_left(ps, 1. * top / ps[i], lo = i)
    #ps[j] >= top/i
    #ps[i] * ps[k] valid for all k=i..j-1
    answer += j - i
    
    
print answer

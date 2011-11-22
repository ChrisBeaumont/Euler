"""
Consider the fraction, n/d, where n and d are positive integers. If nd
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending
order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper
fractions for d 1,000,000?


Solution
--------

A numerator/denominator pair that are not relatively prime can be
reduced. Thus, we wan't to add up all of the relatively prime
numerator/denominator pairs.  The number of such numerators for each
denominator is the Euler Totient function, which takes as input the
prime factors of the denominator.

We collect the prime factors, and add up the totients
"""
from util import totient
top = 1000001

#prime factors of numbers
fs = [[] for i in range(top)]
for i in xrange(2, top):
    if fs[i]: continue
    for j in xrange(i, top, i):
        fs[j].append(i)

#totients for each number. Skip 0,1
ts = [totient(i, fs[i]) for i in range(2, top)]

#the answer
print sum(ts)    

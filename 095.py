"""
The proper divisors of a number are all the divisors excluding the
number itself. For example, the proper divisors of 28 are 1, 2, 4, 7,
and 14. As the sum of these divisors is equal to 28, we call it a
perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum
of the proper divisors of 284 is 220, forming a chain of two
numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with
12496, we form a chain of five numbers:

12496 14288 15472 14536 14264 ( 12496 ...)

Since this chain returns to its starting point, it is called an
amicable chain.

Find the smallest member of the longest amicable chain with no element
exceeding one million.

Solution
--------
Just a direct search, storing the answer to every number
as it gets generated in a chain. 
"""
import numpy as np

top = 1000001
length = np.zeros(top)

best = 0
index = 0

sumdivs = np.ones(top, dtype=int)
for i in xrange(2, top):
    sumdivs[i + i::i] += i

def sumdiv(num):
    #direct calculation of all factors slow.
    #return sum(factors(num)[:-1])
    return sumdivs[num]
    

def chain(num, start=None):
    global best
    global index

    #start the chain
    if start is None:
        start = []

    # wandered into a closed loop
    if num < top and length[num] != 0:
        for s in start:
            length[s] = -1
        return

    # element too large. Not a chain
    if num >= top:
        for s in start:
            length[s] = -1
        return


    #completed a cycle
    if num in start:
        # mark the elements
        # not in the cycle
        i = 0
        while start[i] != num:
            length[start[i]] = -1
            i += 1
            
        # elements in the cycle
        answer = len(start) - i
        if answer > best:
            best, index = answer, min(start[i:])
        while i < len(start):
            length[start[i]] = answer
            i += 1

        return

    start.append(num)
    next = sumdiv(num)

    # num is prime. Not a chain
    if next == 1:
        for s in start:
            length[s] = -1
        return

    l = chain(next, start)

for i in xrange(2, top):
    chain(i)

print index

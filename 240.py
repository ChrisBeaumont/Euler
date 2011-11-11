from math import factorial
from itertools import combinations_with_replacement as comb


sides = 12
n_total = 20
n_top = 10
target_sum = 70

n_bot = n_total - n_top
memo = {}

def unique(sequence):
    """ Calculates the number of unique ways to arrange the objects in
    sequence, if the order of the unique elements in sequence matters,
    but the order of identical elements doesn't"""
    result = factorial(len(sequence))
    digits = [0] * (max(sequence) + 1)
    for s in sequence:
        digits[s] += 1
    for d in digits:
        result /= factorial(d)
    return result

def pickless(num, top):
    """ 
    Returns the number of sequences of (num) numbers from 1-(top-1)
    """

    key = (num, top)
    if key in memo:
        return memo[key]

    if num == 0: return 1
    if top == 1: return 0

    result = 0
    for i in range(num+1):
        result += pickless(num - i, top - 1) * shuffle(num-i, i)

    memo[key] = result
    return result
    
        
def shuffle(n, m):
    """ 
    Returns the number of unique arrangements of n red balls and m
    blue balls
    """
    return unique(([1] * n) + ([0] * m))


""" Solve the actual problem 

First, consider each unique combination of top dice that sum to the
target.

For each of these, consider each number of remaing dice equal to the
minimum value of the top dice.

Partition into two groups: dice >= min value of top, and dice < this
value. Compute the number of arrangements of each of these groups, 
as well as the number of ways to distribute those two partitions 
over all dice.

Add it all up.
"""
result = 0
# unique sequences of top dice
for rolls in comb(range(1, sides+1), n_top): 
    if sum(rolls) != target_sum: continue
    lo = min(rolls)

    #group lo dice by how may of them = lo
    for nlo in range(n_bot+1):

        #partition of dice >= lo
        hi = rolls + tuple([lo] * (n_bot - nlo))        
        nhi = unique(hi)

        #partition of dice < lo
        numlo = pickless(nlo, lo)

        #number of ways to arrange
        #these partitions among all dice
        nshuffle = shuffle(nlo, len(hi))

        #add it up
        result += nshuffle * numlo * nhi
    
print result

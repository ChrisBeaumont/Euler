"""
Using the numbers 1 to 10, and depending on arrangements, it is
possible to form 16- and 17-digit strings. What is the maximum
16-digit string for a "magic" 5-gon ring?

Solution
--------
Enumerate all combinations
"""
from itertools import permutations
from numpy import argmin

side = 5
def magic(s):
    """ Is a sequence magic? """
    num = s[side] + s[0] + s[1]
    for i in xrange(1, side):
        if s[i] + s[(i+1) % side] + s[i+side] != num: return False
    return True

def string(s):
    """ Convert a sequence into the string that the problem requires """
    start = argmin(s[side:])
    s = map(str, s)
    ind = [ ''.join([s[i+side], s[i], s[(i+1) % side]]) for i in range(side)]
    result = ''.join([ind[(start + i) % side] for i in range(side)])
    return result

#consider each sequence of integers 1-10. Arrange into ring
#by placing 1st element at top of inner ring, and work clockwise

# find the magic rings
result = filter(magic, permutations(range(1, 2 * side + 1)))

# turn into strings
result = map(string, result)

# keep only length 16 results
result = filter(lambda x:len(x) == 16, result)

# turn into integers
result = map(int, result)

# pick the biggest
print max(result)

from itertools import permutations
import sys

result = []
for p in permutations('123456789'):
    #note: no term can be larger than 5 digits
    for xpos in range(1, 6):
        lo = max(xpos + 1, 6 - xpos) 
        hi = 6 
        for epos in range(lo, hi):
            m1 = int(''.join(p[:xpos]))
            m2 = int(''.join(p[xpos:epos]))
            m3 = int(''.join(p[epos:]))
            if m1 * m2 == m3:
                result.append(m3)
print sum(set(result)) # set() removes duplicates

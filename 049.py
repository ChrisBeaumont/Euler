from itertools import permutations, combinations, combinations_with_replacement as cwr
import sys

from util import isprime

# iterate over each combination of 4 numbers
for digits in cwr('0123456789', 4):

    # all permutations of digits, in numerical order
    perms = [int(''.join(p)) for p in permutations(digits)]
    perms = sorted(perms)

    # each increasting pair
    for t1, t2 in combinations(perms, 2):
        if t1 < 1000: continue # must be 4 digits
        if t2 == t1: continue  # must be increasing
        if t1 == 1487: continue
        t3 = t2 + (t2 - t1)
        if not isprime(t1) or not isprime(t2): continue
        if not isprime(t3) or t3 not in perms: continue
        print "%4.4i%4.4i%4.4i" % (t1, t2, t3)
        sys.exit(1)

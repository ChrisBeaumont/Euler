import sys
from util import isprime

for i in xrange(3, 10000000, 2):
    if isprime(i): continue
    solved = True
    for n in xrange(1, i):
        k = i - 2 * n ** 2
        if k < 0: 
            break
        if isprime(k): 
            solved = False
            break
    if solved:
        print i
        sys.exit()

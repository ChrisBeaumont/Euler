import sys
from itertools import permutations

def can_solve(num, split):
    base = int(num[:split])
    pos = split
    n = 2
    while(pos < 9):
        search = str(base * n)
        if num[pos: pos + len(search)] != search:
            return False
        pos += len(search)
        n += 1
    return True

#search the pandigitals in descending order
for p in permutations('987654321'):
    num = ''.join(p)
    for i in range(1, 9):
        if can_solve(num, i):
            print num
            sys.exit()

from itertools import permutations

i = 1
for p in permutations('0123456789'):
    if i == 1000000:
        print ''.join(p)
    i += 1

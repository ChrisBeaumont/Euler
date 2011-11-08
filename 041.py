from util import isprime
from itertools import permutations

#can exclude following ns:
#1-3 (example gives a 4-digit pandigital)
#5,6,8,9 (divisible by 3)
#thus, look at 7 then 4
#that leaves 4! + 7! = 5064 permutations to search through
#order permutations in reverse order to speed up search

for p in permutations('7654321'):
    num = int(''.join(p))
    if isprime(num):
        break
print num

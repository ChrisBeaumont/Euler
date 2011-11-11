from itertools import count
import sys

from util import isprime

memo = {}
memo[('', 1)] = True
memo[('', -1)] = True

def truncate_prime(num): # num is  a string
    return _prime(num, 1) and _prime(num, -1)

def _prime(num, direction):
    key = (num, direction)
    if key in memo:
        return memo[key]

    recurse = num[1:] if direction == 1 else num[:-1]
    if _prime(recurse, direction):
        result = isprime(int(num))
    else: 
        result = False

    memo[key] = result
    return result


result = []
for num in count(11, 2):
    if truncate_prime(str(num)):
        result.append(int(num))
        print num, len(result)
        if len(result) == 11:
            print sum(result)
            sys.exit()
                

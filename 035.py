from itertools import product

from util import isprime

def is_circular_prime(num): # num is a string
    for i in range(len(num)):
        shift = int(num[i:] + num[:i])
        if not isprime(shift): 
            return False
    return True
        

#just search from 10-1M
#we can skip any number containing 024568
#because one of the rotations will be divisible by 2 or 5
digits = '1379'

#all 2-to-6 digit combinations of digits
numbers = (''.join(n) for i in [2,3,4,5,6] 
           for n in product(digits, repeat=i))
#remove the non-circular-primes
numbers = filter(is_circular_prime, numbers)

#add to the 1 digit answers
result = [2, 3, 5, 7] + numbers

print len(result)


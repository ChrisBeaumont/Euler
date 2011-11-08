from util import isprime


sum = 2
for i in range(3, 2000000, 2):
    if isprime(i): sum += i

print sum

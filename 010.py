def isprime(x):
    for i in range(2, int(x ** .5)+1):
        if x % i == 0:
            return False
    return True

sum = 2
for i in range(3, 2000000, 2):
    if isprime(i): sum += i

print sum

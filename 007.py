def isprime(x):
    for i in range(2, int(x ** .5)+1):
        if x % i == 0:
            return False
    return True

num = 1
x = 3
prime = 2
stop = 10001
while(num < stop):
    if isprime(x): 
        num += 1
        prime = x
    x += 2

print prime


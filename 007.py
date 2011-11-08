from util import isprime


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


fib = [1, 2]
while fib[-1] <= 4000000:
    fib.append(fib[-1] + fib[-2])
    
answer = sum(filter(lambda x: x % 2 == 0, fib))
print answer


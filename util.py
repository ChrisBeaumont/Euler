def factors(n):
    result = []
    for i in range(1, n+1):
        div = n / i
        if div < i:
            break
        if div * i != n:
            continue
        if div == i:
            result.append(i)
        else:
            result.extend([i, div])
    return sorted(result)

def isprime(x):
    for i in range(2, int(abs(x) ** .5)+1):
        if x % i == 0:
            return False
    return True

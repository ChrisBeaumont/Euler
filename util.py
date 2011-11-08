prime_memo = {}
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
    if x in prime_memo:
        return prime_memo[x]

    for i in range(2, int(abs(x) ** .5)+1):
        if x % i == 0:
            prime_memo[x] = False
            return False

    prime_memo[x] = True
    return True

def primefactors(num):
    result = []
    for div in xrange(2, num+1):
        if div > num: break
        if num % div != 0: continue
        result.append(div)
        while (num % div) == 0:
            num /= div
    return result

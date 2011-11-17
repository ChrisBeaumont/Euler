from random import uniform
prime_memo = {}
#p_10M = open('primes_tenmillion.dat').read().split()
#p_10M = map(int, p_10M)
#p_10M = dict(zip(p_10M, p_10M))

def dictionary():
    words = open('words').readlines()
    words = map(lambda x: x.strip().lower(), words)
    return dict(zip(words, words))

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
    if x < 2:
        return False
    if x in prime_memo:
        return prime_memo[x]

    #if x < 10000000:
    #    return x in p_10M

    for i in xrange(2, int(abs(x) ** .5)+1):
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

def digits(num):
    return map(int, str(num))

def gcd(x, y):
    if y > x: x,y = y,x
    while y != 0:
        x,y = y, x % y
    return x

def modular_exponentiation(a, b, n):
    c = 0
    d = 1
    bs = []
    x = b
    while x > 0:
        bs.append(x & 1)
        x >>= 1
    bs = bs[::-1]
    for i in xrange(len(bs)):
        c *= 2
        d = d ** 2 % n
        if bs[i] == 1:
            c += 1
            d = (d * a) % n
    return d

def witness(a, n):
    # Cormen sec 31.8, p969
    u = n-1
    t = 0
    while (u & 1 == 0):
        u >>= 1
        t += 1
        
    assert(2 ** t * u == n - 1)
    assert(t >= 1)

    x0 = modular_exponentiation(a, u, n)
    for i in xrange(t):
        x1 = x0 ** 2 % n
        if x1 == 1 and x0 != 1 and x0 != (n-1):
            return True
        x0 = x1
    if x1 != 1:
        return True
    return False
    

def miller_rabin(n, s=20):
    if n == 2: return True
    if n & 1 == 0: return False

    for j in xrange(s):
        a = int(uniform(1, n))
        if witness(a, n):
            return False
    return True
        

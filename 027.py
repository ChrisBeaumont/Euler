#only ~4Million combinations. Just check

from util import isprime

best = (0, 0, 0)
#the n=0 term is always b. Only consider prime bs
bs = filter(isprime, range(-999, 1000))

for a in range(-999, 1000):
    for b in bs:
        #count prime sequence
        n = 0        
        while isprime(n**2 + a * n + b):
            n += 1
        if n > best[0]:
            best = (n, a, b)

print best[0], best[1] * best[2]
            

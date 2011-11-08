from util import isprime

#compute primes
top = 1000001
primes = filter(isprime, xrange(2, top))
d = dict(zip(primes, primes)) # store in dictionary for fast lookup

#consider all possible sequences, keep track of best
maxlen = 1
maxprime = 0
for i in range(len(primes)):
    for j in range(i + maxlen, len(primes)):
        s = sum(primes[i:j])
        if s > primes[-1]: 
            break
        if s in d:
            maxlen = j-i
            maxprime = s

print maxprime, maxlen

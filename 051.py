from itertools import count, permutations, combinations_with_replacement

from util import isprime

target = 8
digits = '0123456789'
answer = None

# within a digit search, not guaranteed to find smallest solution first,
# so must find _all_ solutions wiht a given digit before exiting.
for d in count(2):
    ds = range(d)
    #how many digits to fill in?
    for f in range(1, d):
        #where to fill them in at?
        for p in permutations(ds, f):
            #what digits to fill in with?
            for r in combinations_with_replacement(digits, f):                
                if r[0] == '0': continue
                base = ['.'] * d
                for i,j in zip(p, r):
                    base[i] = j
                result = []
                #what digit to fill in remaining spots?
                for i in digits:
                    if i == '0' and base[0] == '.': continue
                    num = int(''.join(base).replace('.', i))
                    if isprime(num):
                        result.append(num)
                    if len(result) == target:
                        if answer is None: answer = result[0]
                        answer = min(answer, result[0])
                        break
    if answer is not None:
        print answer
        break

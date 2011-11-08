MAX = 1000000
chains = [0 for i in xrange(MAX)]
chains[1] = 1

def chainlength(num):
    if num == 1: 
        return 1
    if num < MAX and chains[num] != 0:
        return chains[num]
    if num % 2 == 0:
        result = 1 + chainlength(num / 2)
    else:
        result = 1 + chainlength(3 * num + 1)

    if num < MAX:
        chains[num] = result
    return result

start = 0
maxl = 0
for i in xrange(1, 1000000):
    cl = chainlength(i)
    if cl > maxl:
        start = i
        maxl = cl

print start
        

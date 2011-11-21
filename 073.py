from util import gcd
stop = 12000
answer = 0

for i in xrange(1, stop+1):
    xx = i / 3
    yy = i / 2 + 2
    for j in xrange(xx, yy):
        if gcd(i, j) != 1: continue #counted earlier
        if 3 * j > i and 2 * j < i: answer += 1

print answer

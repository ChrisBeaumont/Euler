from continued_fraction import convergent
from util import digits

def seq():
    yield 2
    k = 1
    while True:
        yield 1
        yield 2 * k
        yield 1
        k += 1


con = convergent([1], seq())
top = 100
for i in range(top):
    n,d = con.next()

print sum(digits(n))

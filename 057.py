from util import digits
from continued_fraction import convergent

answer = 0
con = convergent([1], [1,2])
top = 1000
#ignoring the first convergent in this problem
con.next()

for i in range(top):    
    n, d = con.next()
    if len(digits(n)) > len(digits(d)):
        answer += 1

print answer



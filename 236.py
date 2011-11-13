import sys

from fraction import Fraction

a = [5248, 1312, 2624, 5760, 3936]
b = [640,  1888, 3776, 3776, 5664]
ca = [sum(a[i:]) for i in range(len(a))]
cb = [sum(b[i:]) for i in range(len(b))]
tot_a = sum(a)
tot_b = sum(b)
    
def valid_m(M, bad_a, bad_b, row = 1):
    if row == 5:
        #net spoilage in A / net spoilage in B
        f = Fraction(bad_a, tot_a) / Fraction(bad_b, tot_b)
        return f == M

    #easy early termination test
    if Fraction(ca[row] + bad_a, tot_a) < M * Fraction(bad_b, tot_b):
        return False

    rate_a = Fraction(a[row], b[row]) / M
    rate_a.reduce()
    for i in range(rate_a.denom, b[row]+1, rate_a.denom):
        ct = rate_a * i
        assert ct.whole()
        if valid_m(M, bad_a + ct.int(), bad_b + i, row + 1):
            return True
    
    return False

result = []

ct = 0
for i in range(1, b[0] + 1):
    if i % 10 == 0: print i, b[0]
    for j in range(1, a[0]+1):
        #num, denom of M, the ratio of spoilage rates in B / A
        rate_b = Fraction(i, b[0])
        rate_a = Fraction(j, a[0])
        M = rate_b / rate_a
        if M < 1: break
        if valid_m(M, j, i): 
            M.reduce()
            print M
            result.append(M)

print result


        

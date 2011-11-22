"""
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 131802 =
1.

It can be assumed that there are no solutions in positive integers
when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain
the following:

32 – 222 = 1
22 – 312 = 1
92 – 542 = 1
52 – 622 = 1
82 – 732 = 1

Hence, by considering minimal solutions in x for D 7, the largest x is
obtained when D=5.

Find the value of D 1000 in minimal solutions of x for which the
largest value of x is obtained.


Solution
--------
The fundamental (i.e. minimum x) solution (x,y) is also a convergent
in the continued fraction expansion of sqrt(D). See Pell's
Equation. Use helper routines to iterate through the convergents.
"""
from continued_fraction import root, convergent

def minx(D):
    if int(D**0.5)**2 == D: return 0
    b = root(D)
    for x,y in convergent([1], b):
        if x**2 - D * y ** 2 == 1:
            return x

best, answer = 0,0
for i in xrange(2, 1001):
    mx = minx(i)
    print i, mx
    if mx > best:
        best, answer = mx, i

print answer

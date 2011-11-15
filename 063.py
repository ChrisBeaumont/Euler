""" When can we stop the search?

Let f(x) denote the number of digits in x:
f(x) = floor(log10(x) + 1)

The problem restricts x to be a power: x = b^d for integers b,d

f(b,d) = floor(d log10(b) + 1)

We seek the number of (b,d) pairs for which f(b,d) == d
This is equivalent to the (b,d) pairs for which
d <= d log10(b) + 1 < d+1

solving for b:

b >= 10^((d - 1) / d)
b < 10

Once d >= 22, b > 9. But b is an integer < 10. So there are
no feasible bs for d >= 22
"""

def digits(n):
    return len(str(n))

answer = 0
for d in range(22):
    for b in range(10):
        #skip 0, problem wants positive integers
        num = b ** d
        if num == 0: continue
        nd = digits(num)
        if nd > d: break
        if nd == d:
            answer += 1
print answer

from util import factors

top = 10000
d = [0] * (top+1)
for i in range(top):
    d[i] = sum(factors(i)[:-1])

result = 0
for i in range(1, top):
    if d[i] > i and d[i] < top and d[d[i]] == i:
        result += d[i] 
        result += i

print result

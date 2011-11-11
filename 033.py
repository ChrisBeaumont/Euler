from util import factors

def is_curious(num, denom):
    if num % 10 == 0 and denom % 10 == 0: return False

    n = str(num)
    d = str(denom)
    n2 = ''.join(filter(lambda x: x not in d, n))
    d2 = ''.join(filter(lambda x: x not in n, d))
    if n2 == '' or d2 == '': return False
    n2 = int(n2)
    d2 = int(d2)
    if n2 == num or d2 == denom: return False
    return d2 * num == n2 * denom

result = []
for i in range(10, 100):
    for j in range(i+1, 100):
        if is_curious(i, j):
            result.append((i,j))

print result
#1/4, 1/5, 2/5, 1/2
#= 2 / 200 = 1/100

from util import digits


answer = 0
stop = 10000000
sumsq = lambda a: sum((x ** 2) for x in a)

#takes 2 minutes
memo = {}
def stop89(n):
    if n == 1: return False
    if n == 89: return True
    if n in memo: return memo[n]
    result = stop89(sumsq(digits(n)))
    memo[n] = result
    return result

answer = len(filter(stop89, xrange(1, stop)))
print answer

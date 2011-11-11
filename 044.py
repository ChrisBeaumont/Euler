from itertools import combinations

pentagonals = [n * (3 * n - 1) / 2 for n in xrange(1, 10000)]
d = dict(zip(pentagonals, pentagonals))
pairs = combinations(pentagonals, 2)

#note -- we should really sort the pairs by 
# difference to be sure to find the correct answer
# nevertheless, this happens upon the solution
for p in pairs:
    sum = p[1] + p[0]
    diff = p[1] - p[0]
    if sum in d and diff in d:
        print diff
        break

import numpy as np

from util import factors

""" Find sum of numbers not expressible as the sum of two abundant numbers """

TOP = 28124
abundants = []
nosum = np.ones(TOP, dtype='bool')

# find the abundant numbers below TOP
for i in range(12, TOP):
    if sum(factors(i)[:-1]) > i:
        abundants.append(i)
abundants = np.array(abundants)

# compute each pairwise sum of abundants
# mark the corresponding number as disqualified
for i in range(len(abundants)):
    if abundants[i] > TOP / 2: 
        break
    s = abundants[i] + abundants[i:]
    hit = np.where(s < TOP)
    nosum[s[hit]] = False

#sum up the numbers
ind, = np.where(nosum)
print ind.sum()

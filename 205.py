"""
Peter has nine four-sided (pyramidal) dice, each with faces numbered
1, 2, 3, 4.  Colin has six six-sided (cubic) dice, each with faces
numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total
wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give
your answer rounded to seven decimal places in the form 0.abcdefg

Solution:
---------
Enumerate every possible outcome for pete and colin. Then compute
sum_x P(pete rolls x) * P(colin rolls < x)
"""

from itertools import product

#ith entry gives number of outcomes summing to i
pete = [0] * 37
colin = [0] * 37

for p in product([1,2,3,4], repeat=9):
    pete[sum(p)] += 1

for p in product([1,2,3,4,5,6], repeat=6):
    colin[sum(p)] += 1

#total outcomes
sp = sum(pete)
sc = sum(colin)

#collect probability
n = 0
d = sp * sc
for i in range(7, len(pete)):
    nn = pete[i] * sum(colin[:i])
    n += nn    

print "%0.7f" % (1. * n / d)

"""
Using a combination of black square tiles and oblong tiles chosen
from: red tiles measuring two units, green tiles measuring three
units, and blue tiles measuring four units, it is possible to tile a
row measuring five units in length in exactly fifteen different ways.


How many ways can a row measuring fifty units in length be tiled?

Solution
--------
Dynamic programming
"""

memo = {}
l = (2,3,4)
def block(x):
    """ Number of ways to place 1 or more blocks into x slots """

    #calculated answer before
    if x in memo:
        return memo[x]

    result = 0
    for i in range(0, x):
        for ll in l:
            #spots [0,i) empty, block ll in slot i
            if x - i >= ll:
                result += 1 + block(x - i - ll)

    #save result
    memo[x] = result
    return result

def answer(x):
    return block(x) + 1 # add 1 for the empty solution

print answer(50)

    

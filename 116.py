"""
A row of five black square tiles is to have a number of its tiles
replaced with coloured oblong tiles chosen from red (length two),
green (length three), or blue (length four).

Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of
replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty
units in length be replaced if colours cannot be mixed and at least
one coloured tile must be used?

Solution:
---------
Dynamic Programming
"""
memo = {}

def block(x, l):
    """ 
    Number of ways to place 1 or more blocks of length l into x slots
    """

    key = (x,l)
    if key in memo:
        return memo[key]

    result = 0
    for i in range(0, x - l + 1):
        #slots 0-(i-1) empty. Put a block in slot i. Add up all
        #remining ways of adding blocks to the remaining x - i - l
        #slots to the right of this block
        result += 1 + block(x - i - l, l)

    memo[key] = result
    return result

def answer(x):
    return block(x, 2) + block(x, 3) + block(x, 4)

print answer(50)

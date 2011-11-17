"""
Find the sum of the only ordered set of six cyclic 4-digit numbers for
which each polygonal type: triangle, square, pentagonal, hexagonal,
heptagonal, and octagonal, is represented by a different number in the
set.

Solution:
Just a recursive search over the possible combinations
"""

#the relevant numbers to search through
dig4 = lambda x: x > 999 and x < 10000
tri = map(str, filter(dig4, [n * (n+1) / 2 for n in xrange(500)]))
squ = map(str, filter(dig4, [n ** 2 for n in xrange(100)]))
pen = map(str, filter(dig4, [n * (3 * n-1) / 2 for n in xrange(100)]))
hex = map(str, filter(dig4, [n * (2 * n - 1) for n in xrange(100)]))
hep = map(str, filter(dig4, [n * (5 * n - 3)/2 for n in xrange(100)]))
oct = map(str, filter(dig4, [n * (3 * n - 2) for n in xrange(100)]))

#test if two numbers are cyclic
def is_cyclic(x, y):
    return x[-2:] == y[:2]

#input for sample problem
#sets = (tri, squ, pen)

sets = (tri, squ, pen, hex, hep, oct)

def find_cycle(partial, indices):
    plen = len(partial)

    # found an answer: print and exit
    if plen == len(indices) and is_cyclic(partial[-1], partial[0]):
        print sum(map(int, partial))
        return True
    elif plen == len(indices):
        return False

    #iterate over sets of numbers
    for i in xrange(len(sets)):
        if indices[i] >= 0: continue #already have a guess

        #iterate within this set
        for j in xrange(len(sets[i])):

            indices[i] = j
            cand = sets[i][j]
            if plen != 0 and not is_cyclic(partial[-1], cand):
                continue

            #recures
            partial.append(cand)
            if find_cycle(partial, indices):
                return True
            partial.pop()
        indices[i] = -1
    return False

find_cycle([], [-1] * len(sets))
        

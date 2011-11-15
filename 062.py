from itertools import count
from collections import defaultdict
from sys import exit

""" Brute force generation of permutations is inefficient, since the
number of n digit cubes is usually the permutations of an n digit
number

Instead, order the digits of all the cubes -- permutations of each
other with map to the same digit sequence. Group cubes together by
this key, and find the smallest cube with 4 partners
"""

for d in count(1):
    #all 0-(3d-1) digit cubes
    cubes = [i ** 3 for i in range(0, 10 ** d)]
             
    #assign permutation keys
    cubes = map(str, cubes)
    codes = [''.join(sorted(c)) for c in cubes]
   
   #group together
    dict = defaultdict(list)
    for i in range(len(cubes)):
        dict[codes[i]].append(i)
       
    #search for target number of permutations
    target = 5
    for i in range(len(cubes)):
        if len(dict[codes[i]]) == target:
            print cubes[i]
            exit()

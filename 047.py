from itertools import count
from util import primefactors

#jumping ahead for convenience
#you must of course verify 0-start aren't
#solutions
start = 134000
num = 0
for i in count(start):
    if len(primefactors(i)) == 4:
        num += 1
        if num == 4:
            print i - 3
            break
    else:
        num = 0

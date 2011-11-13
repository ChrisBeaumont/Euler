from itertools import count

from util import isprime


num = 1
n_prime = 0.
n_tot = 1.
for side in count(3, 2):
    jump = side - 1
    corners = [num + jump, num + 2 * jump, 
               num + 3 * jump, num + 4 * jump ]
    num = corners[-1]
    n_prime += sum(map(isprime, corners))
    n_tot += 4
    if n_prime * 10 < n_tot: 
        print side
        break
    

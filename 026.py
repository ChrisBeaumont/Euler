from numpy import argmax
import itertools

def cycle(n):
    sequence = {}
    remainder = 1
    for i in itertools.count(0):

        #we've seen this remainder before. 
        #just completed one cycle
        if remainder in sequence:
            return i - sequence[remainder]

        sequence[remainder] = i

        #implicitly calculate each digit in the fraction
        #by multiplying by 10 and dividing. keep track of remainder        
        remainder = (remainder * 10) % n

        # converged with no cycles
        if remainder == 0: return 0


cycles = [cycle(i) for i in range(1, 1000)]
print argmax(cycles) + 1

        

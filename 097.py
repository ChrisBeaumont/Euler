"""
The first known prime found to exceed one million digits was
discovered in 1999, and is a Mersenne prime of the form 269725931; it
contains exactly 2,098,960 digits. Subsequently other Mersenne primes,
of the form 2p1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which
contains 2,357,207 digits: 2843327830457+1.

Find the last ten digits of this prime number.
"""
fac = 28433
exp = 7830457
    
# direct calculation -- takes 3 min!
#num = str(fac * (1 << exp) + 1)
#print str(num)[-10:]

# modulos along the way modulos are safe, because number always
# increases with each operation. Digits lost in the modulo never come
# back to affect the low digits
# runs in 2.5s
num = 1
for i in xrange(exp):
    num <<= 1
    num %= 10000000000
num *= fac
num %= 10000000000
num += 1
num %= 10000000000

print num


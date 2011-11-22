"""
Exactly four continued fractions, for N  13, have an odd period.
How many continued fractions for N  10000 have an odd period?

Solution
--------

Just use the algorithm for continued fraction expansion for square
roots (see Wikipedia).
"""
from continued_fraction import root_period

is_odd = lambda x: x % 2 == 1
stop = 10001
periods = map(root_period, xrange(2, stop))
print len(filter(is_odd, periods))

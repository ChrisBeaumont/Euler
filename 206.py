"""
Find the unique positive integer whose square has the form
1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit.

Solution
--------
upper bound = 1389026624
lower bound = 1010101010
(search space ~300M)
last digit of solution -> last digit of sqrt = 0
(search space ~30M)

just try the rest.
"""
hi = 1389026624
lo = 1010101010
for x in xrange(lo, hi, 10):
    if str(x ** 2)[::2] == '1234567890': break
print x

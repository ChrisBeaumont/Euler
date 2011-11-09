from multiprocessing import Pool
"""
The sum of factorials is always <= 9! number_of_digits
thus, we can terminate search above 2,540,160

range       max factorial sum
[0, 10)         362880      
[10-100)        725760
[100, 1K)      1088640
[1K, 10K)      1451520
[10K, 100K)    1814400
[100K, 1M)     2177280
[1M, 10M)      2540160
"""
def is_sum_of_fac(n):
    # 0!-9!
    digits = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 363880]

    # convert each digit to its factorial
    facs = map(digits.__getitem__, map(int, str(n)))

    #add them up, and check for equality
    return n == sum(facs)


start = 10
stop = 2540161 # see above
numbers = xrange(start, stop)

#serial computation
#result = filter(is_sum_of_fac, numbers)

#parallel computation
p = Pool()
result = p.map(is_sum_of_fac, numbers)
result = filter(lambda x: result[x-start], numbers)


print result
print sum(result)

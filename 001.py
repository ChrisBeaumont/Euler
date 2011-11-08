# factors of 3 and 5 below 1000
threes = [3 * i for i in range(1, 334)]
fives = [5 * i for i in range(1, 200)]
# remove the duplicates
factors = set(threes + fives)
#add them up
print sum(factors)

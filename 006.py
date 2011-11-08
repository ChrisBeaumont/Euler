x = range(1, 101)
x2 = [i ** 2 for i in x]
print sum(x) ** 2 - sum(x2)

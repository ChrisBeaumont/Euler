import numpy as np
""" Caculate the logs as exponent * log(base). Find maximum of these
numbers """

data = open('base_exp.txt').readlines()
data = [map(int, d.strip().split(',')) for d in data]
data = [d[1] * np.log(d[0]) for d in data]
print np.argmax(data) + 1


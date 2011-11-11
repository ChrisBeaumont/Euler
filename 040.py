num = ''.join([str(i) for i in range(1, 1000000)])
num = map(int, num)
print num[0] * num[9] * num[99] * num[999] * num[9999] * \
                  num[99999] * num[999999]

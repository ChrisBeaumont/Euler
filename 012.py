def divisors(num):
    result = [1, num]
    for i in xrange(2, int(round(num ** 0.5))):
        if num % i == 0:
            d = num / i
            if d < i:
                break
            if i == d:
                result.extend([i])
            else:
                result.extend([i, d])
    return result

i = 1
while True:
    num = sum(xrange(i+1))
    d = divisors(num)
    if len(d) > 500 :
        print num
        break
    i += 1

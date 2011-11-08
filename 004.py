def ispalindrome(number):
    s = str(number)
    return s[::-1] == s

#just look at all the products of 3 digit numbers
hi = 0
for i in range(100, 1000):
    for j in range(i+1, 1000):
        product = i * j
        if not ispalindrome(product): 
            continue
        if product > hi:
            hi = product

print hi

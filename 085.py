memo = {}

stop = 200
target = 2000000
closest = target
area = 0
for x in range(1, stop):
    for y in range(x, stop):
        #number of rectangles = x(x+1) y(y+1) / 4
        n = x * (x+1) * y * (y+1) / 4
        resid = abs(target - n)
        if resid < closest:
            closest = resid
            area = x * y

print area

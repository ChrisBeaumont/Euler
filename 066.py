from numpy import sqrt

def next_convergent(args):
    a,b,A11,B11,A1,B1 = args
    A = b * A1 + a * A11
    B = b * B1 + a * B11
    args[2] = args[4]
    args[3] = args[5]
    args[4] = A
    args[5] = B
    return A,B

def init_convergent(num):
    x = int(num ** .5)
    y = num - x ** 2
    b0 = x
    b1 = 2 * x
    a1 = y
    a2 = y
    A0 = b0
    B0 = 1
    A1 = b1 * b0 + a1
    B1 = b1  
    return [y, 2 * x, A0, B0, A1, B1]

def minx(D):
    # x,y are one of the convergents of root(D)
    args = init_convergent(D)
    if args[2] **2 - D * args[3] ** 2 == 1:
        return args[2]
    if args[4] ** 2 - D * args[5] **2 == 1:
        return args[3]
    while True:
        aa = next_convergent(args)
        if aa[0] **2 - D * args[3] **2 == 1:
            return aa[0]


print minx(3)

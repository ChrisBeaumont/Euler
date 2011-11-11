def is_pent(c):
    a,b = 1.5, -0.5
    i = int((-b + (b **2 + 4 * a * c) ** 0.5) / (2 * a))
    return i * (3 * i - 1) / 2 == c

def is_hex(c):
    a,b = 2, -1
    i = int((-b + (b **2 + 4 * a * c) ** 0.5) / (2 * a))
    return i * (2 * i - 1) == c


tris = (n * (n + 1) / 2 for n in xrange(286, 1000000))
for t in tris:
    if is_pent(t) and is_hex(t):
        print t
        break
    

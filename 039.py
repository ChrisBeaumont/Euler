from numpy import argmax
def triangle_solutions(p):
    result = 0
    for s1 in range(1, p):
        for s2 in range(s1, p):
            s3 = p - s1 - s2
            if s3 < s2: break
            if s1 ** 2 + s2 ** 2 != s3 ** 2: 
                continue
            result += 1

    return result


ps = range(10, 1001)
ns = map(triangle_solutions, ps)

print ps[argmax(ns)]

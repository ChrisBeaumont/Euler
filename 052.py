from itertools import count

for d in count(2):
    # first digit must be one, or else we 6x will have an extra digit
    for i in range(10 ** d, 2 * (10 ** d), 1):
        s = sorted(str(i))
        solved = True
        for j in range(2, 7):
            t = sorted(str(i * j))
            if t != s:
                solved = False
                break
        if solved:
            print i
            break
    if solved: break

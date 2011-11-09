import sys

for a in range(1, 334):
    for b in range(a+1, 500):
        c = 1000 - a - b
        if c < b: continue
        if a ** 2 + b ** 2 == c ** 2:
            print a * b * c
            sys.exit()

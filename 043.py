from itertools import permutations

#brute force with some pre-pruning
#to avoid obvious dead ends

sum = 0
for d5 in '05': # divisibility by 5 criterion
    d3s = '02468' if d5 == '5' else '2468' #div by 2 criterion
    for d3 in d3s:
        perms = [i for i in '0123456789' if i not in [d3, d5]]
        for p in permutations(perms):
            s = ''.join(p[0:3]) + d3 + p[3] + d5 + ''.join(p[4:])
            if int(s[2:5]) % 3 != 0: continue
            if int(s[4:7]) % 7 != 0: continue
            if int(s[5:8]) % 11 != 0: continue
            if int(s[6:9]) % 13 != 0: continue
            if int(s[7: ]) % 17 != 0: continue
            sum += int(s)

print sum
    

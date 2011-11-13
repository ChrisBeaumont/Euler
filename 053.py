
#ncr[n][r] = n choose r
#recursion relation: nc(r+1) = ncr * (n-r) / (r+1)
#boundary conditions: nc(0) = 1
ncr = [ [] ] * 101
for n in range(1, 101):
    ncr[n] = [1]
    for r in range(1, n+1):
        ncr[n].append(ncr[n][-1] * (n - r + 1) / r)

#how many above 1000000
f = lambda x: x > 1000000
answer = sum([sum(map(f, row)) for row in ncr])
print answer

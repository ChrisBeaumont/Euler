data = open('matrix.txt').readlines()
data = [ map(int, d.strip().split(',')) for d in data ]

#data = [[131, 673, 234, 103, 18],
#        [201, 96, 342, 965, 150], 
#        [630, 803, 746, 422, 111],
#        [537, 699, 497, 121, 956],
#        [805, 732, 524, 37, 331]]
total = sum(sum(d) for d in data)

""" Recursively solve subproblem of finding best path
from location i,j. Memoize results, since subproblems overlap"""
memo = {}
def path(data, i=0, j=0):
    if j == len(data) - 1:
        return data[i][j]

    key = (i,j)
    if key in memo:
        return memo[key]

    result = [data[i][j] + path(data, i, j+1)]
    col = data[i][j]
    for ii in range(i-1, -1, -1):
        col += data[ii][j]
        result.append(col + path(data, ii, j+1))
    col = data[i][j]
    for ii in range(i+1, len(data)):
        col += data[ii][j]
        result.append(col + path(data, ii, j+1))
    result = min(result)

    memo[key] = result
    return result

answer = total
for i in range(len(data)):
    memo.clear()
    answer = min(answer, path(data, i, 0))

print answer

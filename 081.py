data = open('matrix.txt').readlines()
data = [ map(int, d.strip().split(',')) for d in data ]

#data = [[131, 673, 234, 103, 18],
#        [201, 96, 342, 965, 150], 
#        [630, 803, 746, 422, 111],
#        [537, 699, 497, 121, 956],
#        [805, 732, 524, 37, 331]]

""" Recursively solve subproblem of finding best path
from location i,j. Memoize results, since subproblems overlap"""
memo = {}
def path(data, i=0, j=0):
    key = (i,j)
    if key in memo:
        return memo[key]

    if i == len(data) - 1:
        if j == len(data) - 1:
            result =  data[i][j]
        else:
            result =  data[i][j] + path(data, i, j+1)
    else:
        if j == len(data) - 1:
            result = data[i][j] + path(data, i+1, j)
        else:
            result = data[i][j] + min(path(data, i+1, j), 
                                      path(data, i, j+1))            
    memo[key] = result
    return result

print path(data)

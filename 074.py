top = 1000000
target = 60
facs = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

memo = {} # memo[i] = sum(factorial of digits of i)
def build_chain():
    for nn in xrange(top):
        n = nn
        while n not in memo:
            memo[n] = sum([facs[i] for i in map(int, str(n))])
            n = memo[n]

def cycle_length(n):
    visited = {}
    while n not in visited:
        visited[n] = 1
        n = memo[n]
    return len(visited)
    
build_chain()
l = map(cycle_length, xrange(top))

print len(filter(lambda x: x == target, l))

from astar import astar

keylogs = open('keylog.txt').readlines()
keylogs = [k.strip() for k in keylogs]

class Node(object):
    def __init__(self, fragment, index):
        self.fragment = fragment
        self.index = index

    def is_goal(self):
        return self.index == len(keylogs) - 1

    def steps(self):
        key = keylogs[self.index + 1]
        f = self.fragment
        for i in range(len(f)+1):
            for j in range(i, len(f)+1):
                for k in range(j, len(f)+1):
                    f2 = f[:i]
                    if (len(f2) == 0 or key[0] != f2[-1]): \
                            f2 += key[0]
                    f2 += f[i:j]
                    if (len(f2) == 0 or key[1] != f2[-1]): \
                            f2 += key[1]
                    f2 += f[j:k]
                    if (len(f2) == 0 or key[2] != f2[-1]): \
                            f2 += key[2]
                    f2 += f[k:]
                    yield Node(f2, self.index+1)

    def __str__(self):
        return self.fragment

    def __lt__(self, other):
        return len(self.fragment) <= len(other.fragment)
    

def topological_sort(network):
    """ Sorts a network of directed edges such that,
    for every edge u->v, u appears before v in output
    Network is a numpy array such that, for every edge u->v, 
    network[i,j] = True
    """

    L = [] # the answer
    #find nodes with no incoming edges
    S = []
    n = network.shape[0]
    for x in range(n):
        if not any(network[:, x]) and any(network[x,:]):
            S.append(x)

    #Everytime a node n is added to L, all of the nodes with edges
    #leading to n have already been added to L. We keep track of this
    #by removing all edges out of a node once it is added to L, and
    #look for new nodes with no incoming edges.
    while len(S) != 0:
        node = S.pop()
        L.append(node)
        for i in range(n):
            if not network[node, i]: continue
            network[node, i] = False
            if not any(network[:, i]):
                S.append(i)

    if any(network.flat):
        raise ValueError("Network has at least one cycle")    
    return L
            

def solve_slow():
    """ First attempt at a solution. Slow, but more general than
solve_fast. It conducts a best-first traversal over all the ways that
the first N keylogs can be interleaved into a password. It terminates
once it finds a password that is consistent with all the keylogs """
    start = Node(keylogs[0], 0)
    print astar(start)


def solve_fast():
    """Use topological sorting to find a password that respects all of the
keylog orderings. This only works if each digit is used at most once
in the password. The algorithm knows when this constraint is violated
and, in this case, it isn't.
"""
    from numpy import zeros
    nodes = zeros((10,10), dtype='bool')
    for k in keylogs:
        nodes[int(k[0]), int(k[1])] = True
        nodes[int(k[1]), int(k[2])] = True

    print ''.join(map(str, topological_sort(nodes)))
        
#solve_slow()
solve_fast()

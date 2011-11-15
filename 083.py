import numpy as np

from astar import astar, AStarNode


""" Solve using the A-star pathfinding algorithm """

testing = False
data = open('matrix.txt').readlines()
data = [ map(int, d.strip().split(',')) for d in data ]

if testing:
    data = [[131, 673, 234, 103, 18],
            [201, 96, 342, 965, 150], 
            [630, 803, 746, 422, 111],
            [537, 699, 497, 121, 956],
            [805, 732, 524, 37, 331]]

data = np.array(data)

class Node(AStarNode):
    def __init__(self, i, j, cost, path=None):
        super(Node, self).__init__()
        self.i = i
        self.j = j
        self._cost = cost + data[i,j]
        if path is not None:
            self.path = [p for p in path] + [(i,j)]
        else:
            self.path = [(i,j)]

    def cost(self):
        return self._cost

    def heuristic(self):
        return 0

    def is_goal(self):
        return self.i == data.shape[0]-1 and \
            self.j == data.shape[1]-1

    def steps(self):
        result = []
        i,j,c,p = self.i, self.j, self._cost, self.path
        if i > 0:
            result.append(Node(i-1, j, c, p))
        if j > 0:
            result.append(Node(i, j-1, c, p))
        if i < data.shape[0]-1:
            result.append(Node(i+1, j, c, p))
        if j < data.shape[1]-1:
            result.append(Node(i, j+1, c, p))
        return result

    def __str__(self):
        return "%s: %i" % (self.path, self._cost)

    def __hash__(self):
        return (self.i, self.j).__hash__()
    
    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

start = Node(0,0,0)
node = astar(start)
print node.cost()
        

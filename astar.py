from heapq import heappush as push, heappop as pop

class AStarNode(object):
    def is_goal(self):
        raise NotImplementedError()

    def steps(self):
        raise NotImpementedError()

    def cost(self):
        raise NotImplementedError()

    def heuristic(self):
        raise NotImplementedError()

    def __lt__(self, other):
        return self.cost() + self.heuristic() < \
            other.cost() + other.heuristic()
                   
def astar(start, verbose=False):
    q = [start]
    visited = {}
    while len(q) != 0:
        node = pop(q)
        if verbose:
            print node
        if node.is_goal():
            return node
        for step in node.steps():
            if step not in visited or visited[step] > step.cost():
                push(q, step)
                visited[step] = step.cost()

    print 'No solution found!'

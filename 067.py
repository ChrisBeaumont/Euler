class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.max = None

def build_tree(data):
    parent = [Node(data[0][0])]
    result = parent[0]
    for row in data[1:]:
        nodes = [Node(v) for v in row]
        for i in range(len(nodes)):
            if i > 0:
                parent[i-1].right = nodes[i]
            if i < (len(nodes) - 1):
                parent[i].left = nodes[i]
        parent = nodes
    return result


def maxsum(node):
    if node is None:
        return 0
    if node.max is not None:
        return node.max
    maxl = maxsum(node.left) + node.value
    maxr = maxsum(node.right) + node.value
    
    best = max(maxl, maxr)
    node.max = best
    return best

data = open('067.txt','r').readlines()
data = [map(int, d.strip().split()) for d in data]
root = build_tree(data)
print maxsum(root)

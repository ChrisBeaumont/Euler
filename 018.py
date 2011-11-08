class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.max = None

def build_tree(data):
    parent = None
    for row in data:
        nodes = [Node(v) for v in row]
        if parent is not None:
            for i in range(len(nodes)):
                if i > 0:
                    parent[i-1].right = nodes[i]
                if i < (len(nodes) - 1):
                    parent[i].left = nodes[i]
        else:
            assert len(nodes) == 1, len(nodes)
            result = nodes[0]
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




data = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
    ]

root = build_tree(data)
print maxsum(root)

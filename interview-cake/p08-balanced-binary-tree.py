from collections import deque


class Tree(object):
    def __init__(self):
        self.right = None
        self.left = None


def is_superbalanced(tree):
    unexplored = deque([(tree, 0)])
    depths = []
    while len(unexplored) > 0:
        print unexplored
        current = unexplored.popleft()
        node = current[0]
        depth = current[1]
        if node.left is None and node.right is None:
            if depth not in depths:
                depths.append(depth)
        else:
            if node.left:
                unexplored.append((node.left, depth+1))
            if node.right:
                unexplored.append((node.right, depth+1))
            # possible short circuit
            if depth+1 not in depths:
                if ((len(depths) == 1 and abs(depths[0]-(depth+1)) > 1)
                        or len(depths) > 1):
                    return False
    return True


test_tree = Tree()
test_tree.left = Tree()
test_tree.left.left = Tree()
test_tree.left.right = Tree()
test_tree.left.left.left = Tree()
test_tree.right = Tree()
test_tree.right.left = Tree()
test_tree.right.left.left = Tree()
test_tree.right.right = Tree()
test_tree.right.right.right = Tree()
test_tree.right.right.right.left = Tree()
print is_superbalanced(test_tree)

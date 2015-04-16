from collections import deque


class Tree(object):
    def __init__(self, init_value):
        self.value = init_value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def is_bst(tree):
    if not tree or (not tree.left and not tree.right):
        return True
    if tree.left:
        left_is_bst = is_bst(tree.left)
        if not left_is_bst:
            return False
        left_greatest_value = get_rightmost_leaf(tree.left).value
    else:
        left_greatest_value = float('-infinity')
    if tree.right:
        right_is_bst = is_bst(tree.right)
        if not right_is_bst:
            return False
        right_smallest_value = get_leftmost_leaf(tree.right).value
    else:
        right_smallest_value = float('infinity')
    return (left_greatest_value < tree.value
            and right_smallest_value > tree.value)


def get_rightmost_leaf(tree):
    current = tree
    while current.right:
        current = current.right
    return current


def get_leftmost_leaf(tree):
    current = tree
    while current.left:
        current = current.left
    return current


t = Tree(50)
t.left = Tree(30)
t.right = Tree(80)
t.left.left = Tree(20)
t.left.right = Tree(60)
t.right.right = Tree(90)
t.right.left = Tree(70)

print is_bst(t)


def is_bst2(tree):
    stack = deque([(tree, float('inf'), float('-inf'))])

    while len(stack) > 0:
        current_node, upper_bound, lower_bound = stack.pop()

        if (current_node.value > upper_bound
                or current_node.value < lower_bound):
            return False
        if current_node.right:
            stack.append((current_node.right, upper_bound, current_node.value))
        if current_node.left:
            stack.append((current_node.left, current_node.value, lower_bound))
    return True

print is_bst2(t)

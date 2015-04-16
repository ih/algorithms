class Tree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def get_rightmost(tree):
    if not tree:
        return None
    else:
        while tree.right:
            tree = tree.right
        return tree


def get_second_largest(tree):
    if not tree.right and not tree.left:
        return None
    while tree:
        if not tree.right:
            return get_rightmost(tree.left).value
        if not tree.right.right and not tree.right.left:
            return tree.value
        else:
            tree = tree.right

t = Tree(10)
t.left = Tree(5)

print get_second_largest(t)

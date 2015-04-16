import unittest


class Node(object):
    def __init__(self):
        self.value = None
        self.children = {}

    def __hash__(self):
        return hash(self.value)


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, key, value):
        current_node = self.root
        for character in key:
            if character not in current_node.children:
                new_node = Node()
                current_node.children[character] = new_node
                current_node = new_node
            else:
                current_node = current_node.children[character]
        current_node.value = value

    def lookup(self, key):
        current_node = self.root
        for character in key:
            current_node = current_node.children[character]
        return current_node.value


class TestTrie(unittest.TestCase):
    def test_trie(self):
        trie = Trie()
        trie.insert('abcd', 3)
        trie.insert('ab', 2)
        self.assertEquals(trie.lookup('ab'), 2)
        self.assertEquals(trie.lookup('abcd'), 3)

if __name__ == '__main__':
    unittest.main()

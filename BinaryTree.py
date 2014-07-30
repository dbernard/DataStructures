from StatTracker import StatTracker
import random


class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return str(self.value)


class BinaryTree(object):
    # Binary Trees, unlike Binary Search Trees, are not sorted.
    def __init__(self, root_value):
        # Initialize a Binary Tree with a root node value of (root_value)
        self.root = self._create_node(root_value)

    def _create_node(self, value):
        return Node(value)

    def insert(self, value, nodes=None):
        # Use a Breadth First Search to find the first empty child
        # to ensure we fill out each row entirely and keep a balanced tree.
        children = []
        nodes = [self.root] if nodes is None else nodes
        for node in nodes:
            if node.left == None:
                node.left = self._create_node(value)
                return node.left

            elif node.right == None:
                node.right = self._create_node(value)
                return node.right

            else:
                children.append(node.left)
                children.append(node.right)

        return self.insert(value, children)

    def delete(self, value):
        pass

    def depth_first_search(self, node, value):
        pass

    def breadth_first_search(self, value, nodes, stats=None):
        # Check (node), store pointers to all children nodes for each node in
        # the current level then traverse the children using the same method.
        children = []
        if not nodes:
            print "Value %s not found in tree" % value
            return
        for node in nodes:
            if node == None:
                continue
            elif node.value == value:
                print 'Node with value %s found!' % value
                return node
            else:
                children.append(node.left)
                children.append(node.right)

        return self.breadth_first_search(value, children, stats)


if __name__ == '__main__':
    max = 10000
    tree = BinaryTree(random.randint(0, max))
    for i in range(max/2):
        tree.insert(random.randint(0, max))

    for i in range(10):
        tree.breadth_first_search(random.randint(0, max), [tree.root])


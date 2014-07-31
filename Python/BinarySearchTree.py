from StatTracker import StatTracker
import random

class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return str(self.value)


class BinarySearchTree(object):
    def __init__(self, root_value):
        # Initialize a tree with the root node value of (root_value)
        self.root = self.insert(None, root_value)

    def _create_node(self, value):
        return Node(value)

    def insert(self, root, value):
        # If root is None, we have found the location where we wish to insert
        # our node
        if root == None:
            return self._create_node(value)
        else:
            # Traverse the LEFT side of the tree
            if value <= root.value:
                root.left = self.insert(root.left, value)
            # Traverse the RIGHT side of the tree
            else:
                root.right = self.insert(root.right, value)
            return root

    def search(self, value, node, stats=None):
        # Search the tree for a given value.
        # Track stats for the search, if requested
        if stats != None:
            stats.tick()
        # If the current node doesn't exist, the value is not in our tree
        if node == None:
            print "No value '%s' found in tree" % value
            return
        # If the current node's value is the value we are looking for, return it
        elif node.value == value:
            if stats != None:
                stats.done()
                print ( " --------------------------- \n" +
                        "Node found!\n" +
                        " -- %s nodes visited\n" % stats.nodes_visited +
                        " -- %s time elapsed\n" % stats.total_time +
                        " -- node value: %s\n" % node.value +
                        " -- node left child: %s\n" % node.left +
                        " -- node right child: %s\n" % node.right +
                        " --------------------------- ")

            return node
        elif value < node.value:
            return self.search(value, node.left, stats)
        else:
            return self.search(value, node.right, stats)


if __name__ == '__main__':
    max = 1000000
    tree = BinarySearchTree(random.randint(0, max))
    for i in range(max/2):
        tree.insert(tree.root, random.randint(0, max))

    st = StatTracker()

    for i in range(10):
        tree.search(random.randint(0, max), tree.root, st)
        st.reset()


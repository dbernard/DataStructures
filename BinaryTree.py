#!/usr/bin/python

from StatTracker import StatTracker
import random


class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.discovered = False

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

    def depth_first_search(self, node, value, stats=None):
        # Check if the node we are working on has been looked at and compare the
        # value to the one we are searching for.
        if not node.discovered:
            if stats != None:
                stats.tick()
            if node.value == value:
                self._output_result(node, stats)
                return True

            # Mark the node as discovered
            node.discovered = True

            # Recursively search the children nodes, starting with the left
            for child in (node.left, node.right):
                if child == None:
                    continue
                elif not child.discovered:
                    # If we have found our result, return True all the way back
                    # up the recursive tree.
                    if self.depth_first_search(child, value, stats):
                        return True

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

    def _output_result(self, node, stats):
        if stats == None:
            print 'Node with value %s found!' % node.value
        else:
            stats.done()
            print ( " --------------------------- \n" +
                    " Node found!\n" +
                    " -- %s nodes visited\n" % stats.nodes_visited +
                    " -- %s time elapsed\n" % stats.total_time +
                    " -- node value: %s\n" % node.value +
                    " -- node left child: %s\n" % node.left +
                    " -- node right child: %s\n" % node.right +
                    " --------------------------- ")




if __name__ == '__main__':
    st = StatTracker()
    '''
    max = 10000
    tree = BinaryTree(random.randint(0, max))
    for i in range(max/2):
        tree.insert(random.randint(0, max))

    for i in range(10):
        tree.breadth_first_search(random.randint(0, max), [tree.root])
    '''
    tree = BinaryTree(1)

    tree.insert(2)
    tree.insert(5)
    tree.insert(3)
    tree.insert(4)
    tree.insert(6)
    tree.insert(7)

    tree.depth_first_search(tree.root, 4, st)



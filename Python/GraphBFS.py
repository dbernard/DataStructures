#!/usr/bin/python
# This is an implementation of a BFS on a graph. We won't search for a specific
# value (although that would be easy to implement from this solution), but
# instead will trace and output the search path.
import Queue

class GraphNode(object):
    def __init__(self, value, neighbors=[]):
        self.value = value
        self.neighbors = neighbors

    def addNeighbors(self, neighbors):
        for n in neighbors:
            self.neighbors.append(n)


class Graph(object):
    def __init__(self, root_node):
        self.root = root_node

    def addNode(val, neighbors):
        node = GraphNode(val, neighbors)
        for n in neighbors:
            n.addNeighbor(node)

    def searchPath(self):
        # This will trace the BFS path and return a list of node values in order
        # of traversal.
        q = Queue.Queue()
        visited = []
        traversal = []
        visited.append(self.root)
        q.put(self.root)

        while not q.empty():
            next = q.get()
            traversal.append(next.value)
            for n in next.neighbors:
                if n not in visited:
                    visited.append(n)
                    q.put(n)

        return traversal


if __name__ == '__main__':
    root = GraphNode(0)
    one = GraphNode(1)
    two = GraphNode(2)
    three = GraphNode(3)
    four = GraphNode(4)
    five = GraphNode(5)

    root.addNeighbors([one])
    one.addNeighbors([root, two, three])
    two.addNeighbors([one, four])
    three.addNeighbors([one, four])
    four.addNeighbors([two, three, five])
    five.addNeighbors([four])

    g = Graph(root)
    path = g.searchPath()

    print 'Node traversal: ' + ' -> '.join(str(x) for x in path)


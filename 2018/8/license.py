""" Day 8: Memory Maneuver """
import sys

class Node:
    def __init__(self, children_counter, metadata, parent=None):
        self.parent = parent
        self.children_counter = children_counter
        self.metadata = metadata

        # Added for part 2
        self.value = 0
        self.children = []
        self.meta = []

    def is_root(self):
        return self.parent is None

def traverse(tree):
    """ Traversing tree list, counting as we go. """
    node = Node(tree[0], tree[1])
    i = 2
    metadata = []
    while True:
        if node.children_counter:
            child = Node(tree[i], tree[i+1], node)
            i += 2
            node.children.append(child)
            node = child
        else:
            node.meta = tree[i:i+node.metadata]
            metadata.extend(node.meta)

            node.value = (sum(node.children[m-1].value
                             for m in node.meta
                             if m <= len(node.children))
                          if node.children else
                          sum(node.meta))

            if node.is_root():
                return sum(metadata), node.value
            node.parent.children_counter -= 1
            i += node.metadata
            node = node.parent

# (Part 1, Part 2)
print(traverse([int(t) for t in sys.stdin.read().strip().split()]))

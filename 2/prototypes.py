"""Part 2 of Day 2: Inventory Management System."""
import sys

class Node():
    """Trie node class."""
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    """The trie class."""
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        """Trie insertion."""
        node = self.root
        for i, char in enumerate(key):
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]

    def find(self, key):
        """Find key in trie.
        """
        node = self.root
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True

    def traverse(self, node, chars="", level=0):
        """Trie traversal."""
        #print(" "*level, "".join(chars))
        for char, child in node.children.items():
            self.traverse(child, chars + char, level+1)

def find_prototype_fabric_boxes():
    """..."""
    lines = [line.rstrip("\n") for line in sys.stdin.readlines()]

    for line in lines:
        print(sum(ord(l) for l in line))

### Creating a trie, deleting branches as we go
#    trie = Trie()
#
#    for line in lines:
#        trie.insert(line)
#
#    # We can have maximum 1 differing character
#    # In addition, 2 keys should approximately the same
#    # Thus, the starter branch with only 1 child can be removed
#    #trie.clean_only_children()
#
#    # Then, we are going to traverse the trie
#    # If 2 different characters are found in one path,
#    # the path is aborted
#    trie.traverse(trie.root)
#
#
#    print()
#    print(len(lines))
#    for line in lines:
#        if not trie.find(line):
#            lines.remove(line)
#    print(len(lines))

    return "Didn't find an answer yet"


print(find_prototype_fabric_boxes())

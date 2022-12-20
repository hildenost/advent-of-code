""" Advent of Code 2022. Day 20: Grove Positioning System """

numbers = [1, 2, -3, 3, -2, 0, 4]

with open("input.txt") as f:
    numbers = [int(n) for n in f.read().splitlines()]

# Linked list?
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return f"Node({self.value})"

def initiate_nodes(nodelist, key=1):
    nodes = [Node(s*key) for s in nodelist]

    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    nodes[-1].next = nodes[0]

    for a, b in zip(nodes[1:], nodes):
        a.prev = b
    nodes[0].prev = nodes[-1]

    pivot = [node for node in nodes if node.value == 0][0]
    return nodes, pivot

def mixing(nodelist):
    length = len(nodelist)
    for n in nodelist:
        steps = n.value % (length - 1)
        for __ in range(steps):
            prevold = n.prev
            nextold = n.next

            # First change is that z (a.prev) now should point to b (a.next)
            prevold.next = nextold
            # And b.prev should point to z
            nextold.prev = prevold

            # Second, a.next should point to b.next
            n.next = n.next.next
            # And a.prev should point to b
            n.prev = nextold

            # Third, c.prev should point to a
            nextold.next.prev = n
            # And b.next should point to a
            nextold.next = n

def find_total(pivot, length):
    steps = [n % length for n in (1000, 2000, 3000)]
    total = 0
    for step in steps:
        v = pivot
        for __ in range(step):
            v = v.next
        total += v.value
    return total

nodes, pivot = initiate_nodes(numbers)
mixing(nodes)
print("Part 1:\t", find_total(pivot, len(nodes)))

nodes, pivot = initiate_nodes(numbers, key=811589153)

for __ in range(10):
    mixing(nodes)
print("Part 2:\t", find_total(pivot, len(nodes)))

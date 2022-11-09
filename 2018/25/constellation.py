""" Day 25: Four-Dimensional Adventure """

with open("input.txt") as f:
    points = [[int(n) for n in line.split(",")] for line in f.read().splitlines()]


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f"Edge({self.u}, {self.v}, {self.weight})"


def dist(pt, other):
    return sum(abs(a - b) for a, b in zip(pt, other))


edges = [
    Edge(i, j, dist(a, b))
    for i, a in enumerate(points)
    for j, b in enumerate(points)
    if i != j and j > i
]

tree_id = [i for i in range(len(points))]

# Simple Kruskal but with weight criterion
for edge in sorted(edges):
    if tree_id[edge.u] != tree_id[edge.v] and edge.weight <= 3:
        old_id = tree_id[edge.u]
        new_id = tree_id[edge.v]
        for i in range(len(tree_id)):
            if tree_id[i] == old_id:
                tree_id[i] = new_id

print("Part 1: ", len(set(tree_id)))

""" Advent of Code 2017. Day 7: Recursive Circus """
import re

towers = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
""".splitlines()

with open("input.txt") as f:
    towers = f.read().splitlines()

pattern = re.compile(r"[a-z]+")
tree = {}

all_children = set()

for tower in towers:
    parent, *children = re.findall(pattern, tower)
    weight = int(re.findall(r"\d+", tower)[0])
    tree[parent] = (weight, children)
    all_children.update(set(children))

root = (tree.keys() - all_children).pop()
print("Part 1:\t", root)

from collections import Counter


def dfs(node):
    weight, children = tree[node]
    if not children:
        return weight

    childrens_weights = [dfs(child) for child in children]

    # Are all the childrens' weights the same?
    weights_freq = Counter(childrens_weights)
    if len(weights_freq) > 1:
        (true_weight, __), (wrong_weight, __) = weights_freq.most_common()
        diff = true_weight - wrong_weight

        which_child = childrens_weights.index(wrong_weight)
        wrong_child_weight = tree[children[which_child]][0]
        print("Part 2:\t", wrong_child_weight + diff)
        exit()

    return weight + sum(childrens_weights)


# Need postorder traversal to visit all children before the root
dfs(root)

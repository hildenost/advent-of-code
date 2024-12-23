""" Advent of Code 2024. Day 23: LAN Party """

network = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""".splitlines()

with open("input.txt") as f:
    network = f.read().splitlines()

from collections import defaultdict

interconnections = defaultdict(set)

for connection in network:
    a, b = connection.split("-")
    interconnections[a].add(b)
    interconnections[b].add(a)

threes = set()
alls = set()
for i, v in interconnections.items():
    for b in v:
        intersect = (v - {b}) & interconnections[b]

        if i.startswith("t"):
            threes.update({frozenset((i, b, c)) for c in intersect})

        if intersect:
            alls.add(frozenset((i, b)) | intersect)
print("Part 1:\t", len(threes))

# Add to possible passwords if
# the group set minus the computer is a subset of that computer's
# network list
passwords = [
    ",".join(sorted(a)) for a in alls if all(a - {b} <= interconnections[b] for b in a)
]

print("Part 2:\t", max(passwords, key=len))

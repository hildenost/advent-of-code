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

        for c in intersect:
            if i.startswith("t"):
                threes.add(frozenset((i, b, c)))

        if intersect:
            alls.add(frozenset((i, b)) | intersect)
print("Part 1:\t", len(threes))

# Need to do some housekeeping in alls
passwords = []
for a in alls:
    is_all = True
    for b in a:
        intersect = (a - {b}) & interconnections[b]
        is_all = is_all and (intersect == (a - {b}))
    if is_all:
        passwords.append(",".join(sorted(a)))
print("Part 2:\t", max(passwords, key=len))

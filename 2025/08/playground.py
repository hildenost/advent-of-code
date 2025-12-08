"""Advent of Code 2025. Day 8: Playground"""

import math
from itertools import combinations

with open("input.txt") as f:
    boxes = {tuple(int(n) for n in row.split(",")) for row in f.read().splitlines()}


def straight_line(box1, box2):
    return math.sqrt(sum((x1 - x2) ** 2 for x1, x2 in zip(box1, box2)))


priority = sorted((straight_line(a, b), a, b) for a, b in combinations(boxes, 2))


from collections import defaultdict

parents = defaultdict(set)
for c in boxes:
    for __, a, b in priority[:1000]:
        if a == c:
            parents[c].add(b)
        if b == c:
            parents[c].add(a)


circuits = []
while boxes:
    t = boxes.pop()

    circuit = {t}
    stack = parents[t]
    while stack:
        c = stack.pop()
        # Also remove from boxes
        boxes -= {c}

        if c not in circuit:
            circuit.add(c)
            stack |= parents[c]

    circuits.append(circuit)

ans = sorted(circuits, key=lambda c: len(c), reverse=True)[:3]

print("Part 1:\t", math.prod(len(c) for c in ans))

for __, a, b in priority[1000:]:
    ai, bi = -1, -1
    for i, c in enumerate(circuits):
        if {a, b} <= c:
            # Both in circuit already
            # skip
            break
        elif a in c:
            ai = i
        elif b in c:
            bi = i
    if (ai, bi) == (-1, -1):
        # Both in circuit already
        continue

    if len(circuits) == 2:
        # Final merge
        break

    # mergeing circuits at ai and bi
    new_c = circuits[ai].union(circuits[bi])
    circuits = [c for i, c in enumerate(circuits) if i not in {ai, bi}]
    circuits.append(new_c)

print("Part 2:\t", a[0] * b[0])

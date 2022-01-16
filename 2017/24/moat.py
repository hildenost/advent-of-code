""" Advent of Code 2017. Day 24: Electromagnetic Moat """

with open("input.txt") as f:
    bridges = [tuple(int(l) for l in line.split("/")) for line in f.read().splitlines()]

from collections import defaultdict
pins = defaultdict(list)

for bridge in bridges:
    a, b = bridge
    pins[a].append(b)
    if a != b:
        pins[b].append(a)

dists = {v: 0 for v in pins}
lengths = {v: 0 for v in pins}
def dfs(v, strength, length, edges):
    for n in pins[v]:
        if (n, v) in edges or (v, n) in edges:
            remaining = {e for e in edges if e != (n, v) and e != (v, n)}
            dfs(n, strength + v + n, length + 1, remaining)
    dists[v] = max(dists[v], strength)
    lengths[v] = max(lengths[v], length)
    return strength

dfs(0, 0, 0, {e for e in bridges})

print("Part 1:\t", max(dists.values()))

max_length = max(lengths.values())
strength = max(dists[v] for v, l in lengths.items() if l == max_length)
print("Part 2:\t", strength)

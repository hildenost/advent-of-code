""" Advent of Code 2017. Day 11: Hex Ed """


with open("input.txt") as f:
    path = f.read().strip().split(",")

max_dist = 0
sums = {k: 0 for k in ["n", "nw", "ne", "s", "sw", "se"]}

for step in path:
    q = 0
    r = 0
    s = 0

    sums[step] += 1

    r -= (sums["n"] - sums["s"])
    s += (sums["n"] - sums["s"])

    q += (sums["ne"] - sums["sw"])
    r -= (sums["ne"] - sums["sw"])

    q -= (sums["nw"] - sums["se"])
    s += (sums["nw"] - sums["se"])

    max_dist = max(max_dist, abs(q), abs(r), abs(s))

print("Part 1:\t", max(abs(q), abs(r), abs(s)))
print("Part 2:\t", max_dist)


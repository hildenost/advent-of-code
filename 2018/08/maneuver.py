""" Advent of Code 2018. Day 8: Memory Maneuver """

with open("input.txt") as f:
    license = [int(n) for n in f.read().split()]

metadata = []
def parse(license):
    n_children, n_metadata, *rest = license

    values = []
    for c in range(n_children):
        rest, v = parse(rest)
        values.append(v)

    node_metadata = rest[:n_metadata]

    # For part 1
    metadata.extend(node_metadata)

    # For part 2
    if n_children == 0:
        return rest[n_metadata:], sum(node_metadata)

    value = sum(values[i-1] for i in node_metadata if i-1 < n_children)

    return rest[n_metadata:], value

__, v = parse(license)

print("Part 1:\t", sum(metadata))
print("Part 2:\t", v)

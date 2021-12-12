""" Advent of Code 2021. Day 12: Passage Pathing """

rough_map = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".splitlines()

rough_map = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""".splitlines()

rough_map = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
""".splitlines()

from collections import defaultdict

caves = defaultdict(list)

for line in rough_map: 
    start, end = line.split("-")
    caves[start].append(end)
    if start != "start" and end != "end":
        caves[end].append(start)

def enumerate(caves, part=1):
    # All paths start from start
    paths = {("start",)}
    counter = 0
    while paths:
        path = paths.pop()

        for cave in caves[path[-1]]:
            if cave == "end":
                counter += 1
                continue
            elif cave == "start" and part == 2:
                # Part 2: Cannot visit start again
                continue
            elif cave.islower() and cave in path:
                # Part 1: Cannot visit this cave again, skipping
                if part == 1:
                    continue
                # Part 2: Can visit twice, but then the other 
                # small caves can be visited only once
                if any(path.count(c) == 2 for c in path if c.islower()):
                    #Already a two
                    continue
            # Adding the valid path forward
            paths.add((*path, cave))
    return counter

print("Part 1:\t", enumerate(caves))
print("Part 2:\t", enumerate(caves, part=2))

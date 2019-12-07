from collections import defaultdict
orbits = defaultdict(list)

mapp = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L",
    # PART 2
    "K)YOU",
    "I)SAN",
]

with open("input.txt", "r") as f:
    mapp = f.readlines()

def create_dag(mapp):
    for m in mapp:
        inner, outer = m.strip().split(")")
        orbits[inner].append(outer)
    return orbits

def traverse(orbits):
    root = "COM"

    visited = set()
    depths = {}
    depths[root] = 0

    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(orbits[node])
            for n in orbits[node]:
                depths[n] = depths[node] + 1
    return depths

def get_orbitted(orbits, node):
    for k, v in orbits.items():
        if node in v:
            return [k]
    return []

def find_santa(orbits, depths):
    root = "YOU"
    goal = "SAN"

    queue = []
    queue.append(root)
    visited = {root}
    distance = defaultdict(lambda: 999999999)
    distance[root] = 0

    while queue:
        node = queue.pop(0)
        if node == goal:
            print("FOUND SANTA!!!!")
            return distance[n] # Feels like a hack
        for n in orbits[node] + get_orbitted(orbits, node):
            if n not in visited:
                visited.add(n)
                queue.append(n)
                distance[n] = min(distance[n], distance[node] + 1)

    print("Couldn't reach him :(")

orbits = create_dag(mapp)
depths = traverse(orbits)

### PART 1
print(sum(depths.values()))

### PART 2
print(find_santa(orbits, depths))

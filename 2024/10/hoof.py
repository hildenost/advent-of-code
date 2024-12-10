""" Advent of Code 2024. Day 10: Hoof It """


topo = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".splitlines()

with open("input.txt") as f:
    topo = f.read().splitlines()

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_within_bounds(i, j):
    return 0 <= i < len(topo) and 0 <= j < len(topo[0])


def dfs(v, i, j, part=1):
    # Use a set for the final destinations
    # to avoid counting those twice
    reached = set() if part == 1 else 0

    children = [(i, j, int(v))]
    while children:
        i, j, v = children.pop()

        if v == 9:
            if part == 1:
                reached.add((i, j))
            else:
                reached += 1
            continue

        # Expanding node
        for di, dj in dirs:
            if not is_within_bounds(i + di, j + dj):
                continue

            # Verifying incline
            if int(topo[i + di][j + dj]) == int(v) + 1:
                children.append((i + di, j + dj, int(topo[i + di][j + dj])))
    return len(reached) if part == 1 else reached


def score(part=1):
    return sum(
        dfs(cell, i, j, part=part)
        for i, line in enumerate(topo)
        for j, cell in enumerate(line)
        if cell == "0"
    )


print("Part 1:\t", score(part=1))
print("Part 2:\t", score(part=2))

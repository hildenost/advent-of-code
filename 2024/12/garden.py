""" Advent of Code 2024. Day 12: Garden Groups """


region = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".splitlines()

with open("input.txt") as f:
    region = f.read().splitlines()


def is_within_bounds(i, j):
    return 0 <= i < len(region) and 0 <= j < len(region[0])


E = 0
N = 1
W = 2
S = 3

nesw = {(-1, 0): N, (1, 0): S, (0, -1): W, (0, 1): E}

dirs = {
    E: [(-1, 0), (0, 1), (1, 0), (0, -1)],
    W: [(1, 0), (0, -1), (-1, 0), (0, 1)],
    N: [(0, -1), (-1, 0), (0, 1), (1, 0)],
    S: [(0, 1), (1, 0), (0, -1), (-1, 0)],
}


def get_sides(nodes):
    if len(nodes) == 1:
        return 4
    if len(nodes) == 2:
        return 4

    # We start at the topmost leftmost point of the plot
    start = sorted(nodes)[0]
    # with a starting direction of East
    d = E
    # We will walk clockwise
    # Each step, we will attempt
    # 1. a left turn
    # 2. straight
    # 3. a right turn
    # in that order
    i, j = start
    turns = 1
    while True:
        for di, dj in dirs[d]:
            # Attempting a turn
            if (i + di, j + dj) not in nodes:
                # But alas, cannot do
                continue

            # A 180 turn increases the turn counter by 2
            # Outer and inner turns increase the turn counter by 1
            # Straigh walks do not increase it

            if d == nesw[(di, dj)]:
                # Walking straight
                turns += 0
            elif abs(d - nesw[(di, dj)]) == 2:
                # Complete 180
                turns += 2
            else:
                # Regular corner
                turns += 1

            # Successful turn
            break

        # Housekeeping
        i, j = i + di, j + dj
        d = nesw[(di, dj)]

        # Special case: we are at start point heading W
        if (i, j) == start and d == W:
            # Must check whether we can go south, in which case
            # we're not done yet
            di, dj = dirs[d][0]
            if (i + di, j + dj) in nodes:
                continue
            # If not, we need to do a complete turn to reach start
            turns += 1

        if (i, j) == start:
            break

    return turns


neighbours = [(0, -1), (0, 1), (1, 0), (-1, 0)]
allneighbours = neighbours + [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def minibfs(start, submarked, plant, imin, imax, jmin, jmax):
    def is_within_area(m, n):
        return imin <= m <= imax and jmin <= n <= jmax

    subvisited = set()
    subqueue = [start]
    subsides = 0
    has_border = False
    while subqueue and not has_border:
        m, n = subqueue.pop(0)

        if region[m][n] == plant:
            # Ignoring the actual plant
            continue

        if (m, n) in subvisited:
            continue

        subvisited.add((m, n))

        # Keeping tracked of explored tiles to avoid
        # double triple quadruple work
        submarked.add((m, n))

        # We are inside, and now we search diagonally as well
        for dm, dn in allneighbours:
            if not is_within_area(m + dm, n + dn):
                # If this is the case, then this is
                # not a secluded area
                has_border = True
                break

            if region[m + dm][n + dn] != plant:
                subqueue.append((m + dm, n + dn))

    if subvisited and not has_border:
        subsides += get_sides(subvisited)

    return submarked, subsides


def find_interior(nodes, plant):
    imin, jmin = sorted(nodes)[0]
    imax, __ = sorted(nodes)[-1]

    # Keeping track of the interior (or some exterior) nodes
    # that we have explored already
    submarked = set()
    totalsides = 0

    for row in range(imin, imax + 1):
        # Getting the valid col range for this row
        js = [j for i, j in nodes if i == row]
        jmax = max(js)
        jmin = min(js)

        # Check whether all tiles are filled between jmin and jmax
        not_filled = [(row, j) for j in range(jmin, jmax + 1) if (row, j) not in nodes]

        # If not, we start a search to find the sides of the interior
        for n in not_filled:
            if n in submarked:
                # Been searching here before
                continue

            submarked, subsides = minibfs(n, submarked, plant, imin, imax, jmin, jmax)
            totalsides += subsides

    return totalsides


def bfs(start, plant, marked):
    visited = set()
    queue = [start]

    # We track the perimeter her
    perimeter = 0

    while queue:
        i, j = queue.pop(0)

        if region[i][j] != plant:
            continue

        if (i, j) in visited or (i, j) in marked:
            continue

        visited.add((i, j))
        marked.add((i, j))

        border = 4

        for di, dj in neighbours:
            if not is_within_bounds(i + di, j + dj):
                continue

            if region[i + di][j + dj] == plant:
                queue.append((i + di, j + dj))

                # For every neighbour that is also a plant
                # remove 1 potential border tile
                border -= 1

        perimeter += border

    return visited, perimeter, marked


marked = set()


price = 0
price2 = 0

for k, line in enumerate(region):
    for l, plant in enumerate(line):
        # Use bfs to collect plots and borders (= perimeter)
        visited, perimeter, marked = bfs((k, l), plant, marked)

        if not visited:
            # Nothing to report here, let's move on
            continue

        area = len(visited)

        subsides = find_interior(visited, plant)
        sides = get_sides(visited) + subsides

        price += area * perimeter
        price2 += area * sides
print("Part 1:\t", price)
print("Part 2:\t", price2)

""" Advent of Code 2018. Day 17: Reservoir Research """
# Slow af, but it works

scan = """x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
""".splitlines()
with open("input.txt") as f:
    scan = f.read().splitlines()

import re
def parse(scan):
    clay = set()
    for line in scan:
        x = [(int(a), int(b)) if b else int(a)
             for a, b in re.findall(r"x=(\d+)(?:,|\.\.(\d+))", line)][0]
        y = [(int(a), int(b)) if b else int(a)
             for a, b in re.findall(r"y=(\d+)(?:,|\.\.(\d+))", line)][0]

        if isinstance(x, int):
            ymin, ymax = y
            for y in range(ymin, ymax+1):
                clay.add((x, y))
        else:
            xmin, xmax = x
            for x in range(xmin, xmax+1):
                clay.add((x, y))
    return clay

clay = parse(scan)

still = set()
running = set()

ymin = min(clay, key=lambda x: x[1])[1]
ymax = max(clay, key=lambda x: x[1])[1]
def dfs(source):
    stack = [source]

    while stack:
        x, y = stack[-1]

        if (x, y) in still:
            stack.pop()
            continue

        if {(x, y+1), (x+1, y+1), (x-1, y+1), (x, y), (x, y-1)} <= (running - still):
            # Nothing more to do here
            x_new, y = stack.pop()
            while x_new == x and stack:
                x_new, y = stack.pop()

            if not stack:
                # It means we done
                continue

            # Else we need to add back the ones we popped
            stack.append((x_new, y))

        if {(x-1,y), (x+1,y), (x, y+1)} <= clay | still:
            # Edge case, convert to still
            still.add((x, y))
            stack.pop()
            continue

        if {(x-1,y), (x+1,y), (x, y+1)} <= running | still | clay:
            # Nothing more to do here
            stack.pop()
            continue

        running.add((x, y))

        # Can add the square below? Do it! And continue
        if (x, y+1) not in running | still | clay:
            if y + 1 <= ymax:
                stack.append((x, y+1))
            else:
                x_new, y = stack.pop()
                while x_new == x and stack:
                    x_new, y = stack.pop()

                stack.append((x_new, y))
            continue

        # Flowing sideways
        left = x
        while (left, y + 1) in clay | still and (left, y) not in clay | still:
            left -= 1

        right = x
        while (right, y + 1) in clay | still and (right, y) not in clay | still:
            right += 1

        # We are here because at least one side is open
        left_wall = (left, y)
        right_wall = (right, y)

        if {left_wall, right_wall} <= clay:
            still.update({(x_new, y) for x_new in range(left + 1, right)})
            stack.pop()
            continue

        running.update({(x_new, y) for x_new in range(left+1, right)})
        # Add to stack those who have solid or still water underneath
        if left_wall not in clay | still | running:
            # We do NOT have a boundary
            # Add the overflow
            stack.append(left_wall)

        if right_wall not in clay | still | running:
            # We do NOT have a boundary
            # Add the overflow
            stack.append(right_wall)


def print_water(still_water, running_water, clay, curr=None):
    WATER = '\033[94;44m'
    RUNNING = '\033[34;104m'
    CLAY = '\033[1;38;5;3;48;5;3m'
    CURSOR = '\033[1;41m'
    ENDC = '\033[0m'
    if curr is None:
        xmin = min(x for x, y in clay) - 1
        xmax = max(x for x, y in clay) + 1
        ymin = 0
        ymax = max(y for x, y in clay)
    else:
        X, Y = curr
        deltax = 60
        deltay = 35
        xmin = min(x for x, y in clay if abs(X-x) <= deltax) - 1
        xmax = max(x for x, y in clay if abs(X-x) <= deltax) + 1
        ymin = min(y for x, y in clay if abs(Y-y) <= deltay) - 1
        ymax = max(y for x, y in clay if abs(Y-y) <= deltay) + 1

    output = "\n".join(
        "".join(
            "O"
            if (i, j) == (500, ymin)
            else CURSOR + "X" + ENDC
            if curr == (i, j)
            else WATER + "~" + ENDC
            if (i, j) in still_water
            else RUNNING + "|" + ENDC
            if (i, j) in running_water
            else CLAY + "#" + ENDC
            if (i, j) in clay
            else " "
            for i in range(xmin, xmax + 1)
        )
        for j in range(ymin, ymax + 1)
    )
    return output
dfs((500, 0))
print("Part 1:\t", sum(ymin <= y <= ymax for __, y in running | still))
print("Part 2:\t", len(still))

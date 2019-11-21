"""Module solving Day 17: Reservoir Research, albeit very slowly and
perhaps even a bit hacky.
"""

test_input = "\n".join(
    #This input makes it fail!
    [
#        "x=495, y=2..7",
        "x=495, y=6..7",
        "x=500, y=3..3",
        "y=7, x=495..501",
        "x=501, y=3..7",
        "x=498, y=2..4",
        "x=506, y=1..2",
        "x=498, y=10..13",
        "x=504, y=10..13",
        "y=13, x=498..504",
    ]
)

#test_input = "\n".join(
#    [
#        "x=490, y=6..15",
#        "y=15, x=490..507",
#        "x=507, y=5..15",
#        "x=499, y=8..12",
#        "y=12, x=499..501",
#        "x=501, y=8..12",
#        "x=509, y=1..2",
#    ]
#)
#test_input = "\n".join(
#    [
#        "x=490, y=6..15",
#        "y=15, x=490..507",
#        "x=507, y=5..15",
#        "x=499, y=8..12",
#        "y=12, x=499..501",
#        "y=8, x=499..501",
#        "x=501, y=8..12",
#    ]
#)


def parse_range(range_coord):
    __, ranges = range_coord.split("=")
    min_coord, max_coord = map(int, ranges.split(".."))
    return list(range(min_coord, max_coord + 1))


def parse_input(scan):
    clay_coords = set()
    for line in scan:
#    for line in scan.split("\n"):
        first_co, second_range = line.split(", ")
        name, value = first_co.split("=")
        values = parse_range(second_range)
        clay_coords.update(
            (int(value), v) if name == "x" else (v, int(value)) for v in values
        )
    return clay_coords


source = (500, 0)
with open("input.txt") as f:
    input_scan = [line.strip() for line in f.readlines()]

#clay = parse_input(test_input)
clay = parse_input(input_scan)

xmin = min(x for x, y in clay) - 1
xmax = max(x for x, y in clay) + 1
ymin = min(y for x, y in clay)
ymax = max(y for x, y in clay)


def print_water(still_water, running_water, clay, curr=None):
    output = "\n".join(
        "".join(
            "X"
            if curr == (i, j)
            else "~"
            if (i, j) in still_water
            else "|"
            if (i, j) in running_water
            else "#"
            if (i, j) in clay
            else " "
            for i in range(xmin, xmax + 1)
        )
        for j in range(ymin, ymax + 1)
    )
    return output


# Let's do a depth first kind of search
running_water = set()
still_water = set()
stack = []
stack.append(source)
overflow = False
tick = 0

def clay_or_stillwater(pos):
    return pos in clay or pos in still_water

def right_flow(x, y, stack):
    while x <= xmax and not clay_or_stillwater((x, y)):
        running_water.add((x, y))
        x += 1
        # Detect overflow
        # Overflow occurs if there's a hole in the line below current
        if not clay_or_stillwater((x, y + 1)):
            stack.append((x, y))
            return x, True
    return x, False

while stack:
    tick += 1
#    if tick > 1500:
#        break
    print()
    print(f"~~~~ TICK {tick} ~~~~")
    overflow = False

    x, y = stack.pop()
    a, b = x, y
    print(f"Looking at ({x}, {y}) with {len(stack)} locations left in stack")
#    print(print_water(still_water, running_water, clay, (x, y)))

    if (x, y) in clay:
        continue

    if (x, y) in running_water and (x - 1, y) in running_water and clay_or_stillwater((x, y + 1)):
        x, overflow = right_flow(x, y, stack)
        if (x, y) in clay or overflow:
            continue


    # Falling
    while y <= ymax and not clay_or_stillwater((x, y)):
        falling = True
        #print("Down: Added ", x, y, " to running water set")
        running_water.add((x, y))
        y += 1
        if 0 <= y <= ymax and (x, y) not in running_water.union(still_water):
            stack.append((x, y))
    # Have to back up one unit
    y -= 1

    # If we hit the bottom
    if y == ymax:
        stack = [(i, j) for i, j in stack if i != x]
        continue

    # Find left boundary
#    if (x - 1, y) not in running_water:
    lefting = False
    while not clay_or_stillwater((x, y)) and x >= xmin:
        running_water.add((x, y))
        #print("Left: Added ", x, y, " to running water set")
        x -= 1
        lefting = True
        if not clay_or_stillwater((x, y + 1)):
            if (x, y) not in running_water:
                stack.append((x, y))
            overflow = True
            break
    if overflow:
        continue
    # And backing up
    if lefting:
        x += 1
    x_left = x
    #x_left = xmin

    min_x = min(i for i, j in running_water if j == y)
    x_left = max(x_left, min_x)

    # Filling to the right
    x, overflow = right_flow(x, y, stack)

    # 365, 1679
    is_clay_left = (x_left - 1, y) in clay
    if not overflow and is_clay_left and x_left > xmin and x < xmax:
        #print(f"Creating still water at {[(i, y) for i in range(x_left, x)]}")
        still_water.update((i, y) for i in range(x_left, x))
        running_water -= still_water



print()
print()
water_squares = still_water.union(running_water)
remove = sum(1 for __, y in water_squares if y < ymin)
print(len(water_squares) - remove)
print(len(still_water))
with open("output.txt", "w") as f:
    f.write(print_water(still_water, running_water, clay, curr=(a, b)))

#print(print_water(still_water, running_water, clay))

# 50838
# 43039

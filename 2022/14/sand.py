""" Advent of Code 2022. Day 14: Regolith Reservoir """

sample = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".splitlines()

with open("input.txt") as f:
    sample = f.read().splitlines()

paths = [[tuple(int(n) for n in coord.split(",")) for coord in s.split(" -> ")] for s in sample]

rock = set()
for path in paths:
    for (a, b), (x, y) in zip(path, path[1:]):
        rock |= {(min(a, x) + i, b) for i in range(abs(a-x) + 1)}
        rock |= {(a, min(b, y) + i) for i in range(abs(b-y) + 1)}

xmax = max(rock)[0]
xmin = min(rock)[0]
ymax = max(rock, key=lambda x: x[1])[1]
ymin = 0 
        
def pprint(rock, sand, curr=(0,0)):
    ymax = max(sand, key=lambda x: x[1])[1]+3 if sand else 10 
    for y in range(ymin, ymax+1):
        row = ""
        for x in range(xmin, xmax+1):
            if (x, y) in rock:
                row += "#"
            elif (x, y) in sand:
                row += "o"
            elif (x, y) == curr:
                row += "O"
            else:
                row += "."
        print(row)

within_bounds = True
sand = set()
while within_bounds:
    # Neverending sand, but gives correct answer for Part 1
    x, y = 500, 0
    is_down = True
    is_left = True
    is_right = True

    while is_down or is_left or is_right:
        #pprint(rock, sand, curr=(x, y))
        #print((x, y))
        #input()
        
        # Falling straight down
        while True:
            y += 1
            if (x, y) in sand | rock:
                y -= 1
                is_down = False
                break

        # Falling to the side (left)
        x -= 1
        y += 1
        if (x, y) in sand | rock:
            y -= 1
            x += 1
            is_left = False
        else:
            is_left = True

        # Falling to the side (right)
        if not is_down and not is_left:
            x += 1
            y += 1
            if (x, y) in sand | rock:
                y -= 1
                x -= 1
                is_right = False
            else:
                is_right = True

        if not (xmin <= x <= xmax and ymin <= y <= ymax):
            print(x, y, ymax)
            is_down = False
            is_left = False
            is_right = False
            within_bounds = False

    if within_bounds:
        sand.add((x, y))
        #pprint(rock, sand, curr=(x, y))
        #input()
        print(len(sand))

print(len(sand))

# For part 2, brute-force ain't gonna cut it
# Ok, bruteforce did cut it, but it took 2h30
# Let's flow out from the source instead
s = 500
sand = {(s, 0)}
for y in range(1, ymax+2):
    for x in range(s-y, s+y+1):
        tile = (x, y)
        # If tile is not rock and
        # the tile immediately or diagonally above is sand,
        # current tile is also sand
        if tile not in rock and {(x-1, y-1), (x, y-1), (x+1, y-1)} & sand:
            sand.add(tile)
print("Part 2:\t", len(sand))

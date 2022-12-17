""" Advent of Code 2022. Day 17: Pyroclastic Flow """

from itertools import cycle

shapes = [
    {(0,0), (1,0), (2,0), (3,0)},
    {(1,0), (0,1), (1,1), (2,1), (1,2)},
    {(2,2), (2,1), (0,0), (1, 0), (2,0)},
    {(0,0), (0,1), (0,2), (0,3)},
    {(0,0), (1,0), (0,1), (1,1)}
]

jet = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

with open("input.txt") as f:
    jet = f.read().strip()

def push(j, x, y, shape):
    go_right = j == ">"

    if go_right:
        new_x = x+1
    else:
        new_x = x-1

    # Check walls
    right_side = max(shape)[0]
    if new_x < 0:
        new_x = x
    if new_x + right_side >= 7:
        new_x = x
    
    # Check rocks
    new_shape = {(new_x+dx, y+dy) for dx, dy in shape}
    if any(pos in rocks for pos in new_shape):
        new_x = x
    return new_x

def is_at_rest(shape, x, y):
    new_shape = {(x+dx, y+dy) for dx, dy in shape}
    if y == 0 or any(pos in rocks for pos in new_shape):
        # Come to rest
        y += 1
        new_shape = {(x+dx, y+dy) for dx, dy in shape}
        rocks.update(new_shape)
        return True 
    return False

def pprint(rocks, shape, x=0, y=0):
    if not rocks:
        return
    modded = {(x+dx, y+dy) for dx,dy in shape}
    highest = max(rocks, key=lambda x: x[1])[1] + 8
    for j in range(highest+1, 0, -1):
        row = ""
        for i in range(7):
            if (i, j) in rocks:
                row += "#"
            elif (i, j) in modded:
                row += "@"
            else:
                row += "."
        print(row)
    print()



highest = 0
rocks = set()
i = 0
jet_index = 0
heights = {}
rounds = []
n_rocks = [] 
for k, shape in enumerate(cycle(shapes)):
    # Here be some hardcoded values from finding the positions of the substring
    if highest in [1756, 4458, 7160]:
        n_rocks.append(k)

    heights[k] = highest

    if k == 5000:
        break

    x = 2
    y = highest + 4

    while True:
        jet_index %= len(jet)
        j = jet[jet_index]
        jet_index += 1

        # Update x position
        x = push(j, x, y, shape)

        # Fall
        y -= 1
        if is_at_rest(shape, x, y):
            highest = max(rocks, key=lambda x: x[1])[1]
            break

print("Part 1:\t", heights[2022])

# Part 2 musings
# What is the cycle length?
# We create a string of one column of rocks, print it, and look for a pattern
mid = "".join("#" if (3, y) in rocks else "." for y in range(highest+1))
#print(mid)

import re
# When a pattern is visually found, we search for all the positions it occurs 
substring = "##########################.#..###.####..###...###."
poses = [m.start() for m in re.finditer(substring, mid)]
# And from there, we find the delta height of the periodic rockfalling 
delta_h = poses[1]-poses[0]

start = n_rocks[0]
period = n_rocks[1]-start
# We can subtract the starter stack of rocks from the limit
rock_limit = 1000000000000 - start
# Then we find how many times we can stack the periodic rocks
# and how many rocks remain after that
repeats, remainer = divmod(rock_limit, period)

delta_r = heights[start+period+remainer] - heights[start+period]

print("Part 2:\t", heights[start] + delta_h * repeats + delta_r)

"""
--- end rock limit
|   height of remaining rocks, r
--- repeating pattern n times periods
    end pattern at k+p rocks

    (period = p rocks)

--- start pattern at k rocks
|   height until start, height of the first rocks
---
"""

""" Advent of Code 2022. Day 23: Unstable Diffusion """

def parse_elves(sample):
    """
    ^
    |
    y
    |
    +--- x --->
    
    """
    rows = sample.splitlines()
    ymax = len(rows)

    elves = set()

    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            if cell == "#":
                # Inverting y so it's more Cartesian
                elves.add((x, ymax-y-1))
    return elves


dirs = {
    "N": lambda x, y: (x, y+1),
    "NE": lambda x, y: (x+1, y+1),
    "NW": lambda x, y: (x-1, y+1),
    "S": lambda x, y: (x, y-1),
    "SE": lambda x, y: (x+1, y-1),
    "SW": lambda x, y: (x-1, y-1),
    "W": lambda x, y: (x-1, y),
    "E": lambda x, y: (x+1, y)
}

where_to = {
    "N": lambda elf, elves: check_poses(elf, elves, poses=("N", "NE", "NW")),
    "S": lambda elf, elves: check_poses(elf, elves, poses=("S", "SE", "SW")),
    "E": lambda elf, elves: check_poses(elf, elves, poses=("E", "NE", "SE")),
    "W": lambda elf, elves: check_poses(elf, elves, poses=("W", "NW", "SW")),
}

def check_poses(elf, elves, poses=("N", "NE", "NW", "S", "SE", "SW", "W", "E")):
    return all(dirs[h](*elf) not in elves for h in poses)

def empty_tiles(elves):
    xmax = max(elves)[0]
    xmin = min(elves)[0]
    ymax = max(elves, key=lambda x: x[1])[1]
    ymin = min(elves, key=lambda x: x[1])[1]
    return (xmax + 1 - xmin)*(ymax + 1 - ymin) - len(elves)

with open("input.txt") as f:
    elves = parse_elves(f.read())

options = ["N", "S", "W", "E"]

rounds = 10
i = 0
from collections import defaultdict
while True:
    i+=1

    moves = defaultdict(list)

    # Checking positions
    for elf in elves:
        if check_poses(elf, elves):
            moves[elf].append(elf)
            continue

        for h in options:
            if where_to[h](elf, elves):
                moves[dirs[h](*elf)].append(elf)
                break
        else:
            moves[elf].append(elf)
        
    # Checking collisions
    new_pos = set()
    for move, elfs in moves.items():
        if len(elfs) == 1:
            new_pos.add(move)
        else:
            new_pos.update(elfs)
    
    if elves == new_pos:
        print("Part 2:\t", i)
        break

    elves = new_pos

    if i == rounds: 
        print("Part 1:\t", empty_tiles(elves))

    # Moving directions
    options = options[1:] + [options[0]]


""" Advent of Code 2021. Day 25: Sea Cucumber """

herd = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
""".splitlines()

def create_herds(herd):
    east = set()
    south = set()

    for j, row in enumerate(herd):
        for i, spot in enumerate(row):
            if spot == "v":
                south.add((i, j))
            elif spot == ">":
                east.add((i, j))

    return east, south

with open("input.txt") as f:
    herd = f.read().splitlines()
    

width, height = len(herd[0]), len(herd)
east, south = create_herds(herd)
step = 0

while True:
    step += 1

    no_move = False

    # First, the east-facing ones move
    new_east = {
        (i, j)
        if ((i + 1) % width, j) in east | south else
        ((i + 1) % width, j) 
        for i, j in east
    }

    no_move = new_east == east
    east = new_east

    # Then, the south-facing ones move
    new_south = {
        (i, j)
        if (i, (j+1)%height) in east | south else
        (i, (j+1)%height) 
        for i, j in south 
    }

    if no_move and new_south == south:
        print("Part 1:\t", step)
        break
    
    south = new_south

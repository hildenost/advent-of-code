""" Advent of Code 2016. Day 18: Like a Rogue """

startrow = "..^^."
startrow = ".^^.^.^^^^"

tilemap = [[s for s in startrow]]

part1_rows = 40
nrows = 400000
for n in range(nrows - 1): 
    if n == part1_rows - 1:
        print("Part 1:\t", sum(t == "." for row in tilemap for t in row))

    next_row = []
    for i in range(len(startrow)):
        if i == 0:
            tiles = ["."] + tilemap[-1][:i+2]
        elif i == len(startrow) - 1:
            tiles = tilemap[-1][i-1:] + ["."]
        else:
            tiles = tilemap[-1][i-1:i+2]

        if "".join(tiles) in ["^^.", ".^^", "^..", "..^"]:
            next_row.append("^")
        else:
            next_row.append(".")

    tilemap.append(next_row)


print("Part 2:\t", sum(t == "." for row in tilemap for t in row))



        

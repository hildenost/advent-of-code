
DIRECTIONS = {
    "ne": (1, 0, -1),
    "e": (1, -1, 0),
    "se": (0, -1, 1),
    "sw": (-1, 0, 1),
    "w": (-1, 1, 0),
    "nw": (0, 1, -1)
}

def sum_dirs(tiles, reference=(0, 0, 0)):
    for tile in tiles:
        reference = tuple(a + b for a, b in zip(reference, DIRECTIONS[tile]))
    return reference
    
def parse_instructions(line):
    instructions = []
    i = 0
    while i < len(line):
        d = line[i]
        i += 1
        if d in "ns":
            d += line[i]
            i += 1
        instructions.append(d)
    return instructions



#line = "esew"
#line = "nwwswee"
lines = """\
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
"""

with open("24/input.txt") as f:
    lines = f.read()

def initialise(lines):
    black_tiles = set()
    for line in lines.splitlines():
        instructions = parse_instructions(line)

        tile = sum_dirs(instructions)

        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)
    return black_tiles


def one_cycle(black_tiles):
    neighbours = set()
    to_remove = set()
    for tile in black_tiles:
        num_black_neighbours = 0
        for key in DIRECTIONS:
            neighbour = sum_dirs([key], reference=tile)
            if neighbour in black_tiles:
                num_black_neighbours += 1
            else:
                neighbours.add(neighbour)

        if num_black_neighbours not in  [1, 2]:
            to_remove.add(tile)

    to_add = set()
    for neighbour_tile in neighbours:
        num_black_neighbours = sum(sum_dirs([key], reference=neighbour_tile) in black_tiles for key in DIRECTIONS)
        if num_black_neighbours == 2:
            to_add.add(neighbour_tile)

    black_tiles -= to_remove
    black_tiles |= to_add

    return black_tiles

black_tiles = initialise(lines)
print("Part 1:\t", len(black_tiles))


for i in range(100):
    black_tiles = one_cycle(black_tiles)
print("Part 2:\t", len(black_tiles))



    



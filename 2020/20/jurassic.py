with open("input.txt") as f:
    test = f.read()


EDGES = {
    3: (-1, 0),
    1: (1, 0),
    0: (0, -1),
    2: (0, 1),
    }

class Tile:

    def __init__(self, number, image):
        self.number = int(number)
        self.image = image

        self.neighbours = []
        self.pos = None

        self.set_edges()

    def crop_image(self):
        self.image = [row[1:-1] for row in self.image[1:-1]] 

    def set_edges(self):
        # top right bottom left
        left, right = ["".join(col) for col in zip(*[(r[0], r[-1]) for r in self.image])]

        self.edges = [self.image[0], right, self.image[-1], left]

    def share_edge(self, other):
        for i, edge in enumerate(self.edges):
            nonflipped_in_other = edge in other.edges
            flipped_in_other = edge[::-1] in other.edges
            if nonflipped_in_other:
                other_i = other.edges.index(edge)
                # if absolute difference is 2, no rotation/flipping
                if other_i == i:
                    other.image = flip_y(other.image) if i % 2 else flip_x(other.image)
                elif other_i - i in {1, -3}:
                    other.image = rotate(other.image) if i % 2 else flip_y(rotate(other.image))
                elif other_i - i in {-1, 3}:
                    other.image = rotate(flip_x(other.image)) if i % 2 else rotate(rotate(rotate(other.image)))
            
            elif flipped_in_other: 
                other_i = other.edges.index(edge[::-1])
                if other_i == i:
                    other.image = rotate(rotate(other.image))
                elif abs(other_i - i) == 2:
                    other.image = flip_x(other.image) if i % 2 else flip_y(other.image)
                elif other_i + i == 3:
                    other.image = rotate(flip_y(other.image))
                elif (other_i, i) in [(0, 1), (1, 0), (2, 3), (3, 2)]:
                    other.image = rotate(rotate(rotate(other.image))) if i % 2 else rotate(other.image)

            if nonflipped_in_other or flipped_in_other:
                self.neighbours.append(other)
                other.neighbours.append(self)

                other.set_edges()

                if other.pos is None:
                    other.pos = (self.pos[0] + EDGES[i][0], self.pos[1] + EDGES[i][1])
                return other


    def __repr__(self):
        return f"{self.number}"

        
def flip_x(image):
    return list(reversed(image))

def flip_y(image):
    return ["".join(reversed(r)) for r in image]

def rotate(image):
    return ["".join(r[i] for r in image[::-1]) for i in range(len(image))]

def parse_input(images):
    tiles = []
    for tile in images.split("\n\n"):
        rows = tile.split()

        tile_id = rows[1].strip(":")
        image = rows[2:]

        tiles.append(Tile(tile_id, image))

    return tiles



def assemble_image(pieces):
    poses = [piece.pos for piece in pieces]
    max_x, max_y = max(poses)
    min_x, min_y = min(poses)

    dim = len(pieces[0].image)
    x_dim = dim * (max_x-min_x + 1)
    y_dim = dim * (max_y-min_y + 1)

    image = [[None for __ in range(x_dim)] for __ in range(y_dim)]

    for piece in pieces:
        y = (piece.pos[1] - min_y) * dim
        x = (piece.pos[0] - min_x) * dim
        for i, row in enumerate(image[y:y + dim]):
            row[x:x+dim] = piece.image[i]

    image = ["".join(r) for r in image]
    return image


def find_sea_monster_in_image(image, monster):
    max_offset = abs(max(monster[1]) + 1 - len(image[0]))

    def has_monster(row, row_offset, col_offset):
        return all(image[row+row_offset][col + col_offset] == "#" for col in monster[row_offset])

    return sum(
        # Checking monster line 1 first, as it is more special than the uppermost line
        all(has_monster(k, o, offset) for o in (1, 2, 0))
        for offset in range(max_offset)
        for k in range(len(image) - 1)
    )

def find_rough_waters(image, monster):
    tiles_per_monster = sum(len(m) for m in monster)
    tiles_per_image = sum(r.count("#") for r in image)
    for i in range(3):
        image = rotate(image)
        sea_monsters = find_sea_monster_in_image(image, sea_monster)
        if sea_monsters != 0:
            return tiles_per_image - sea_monsters*tiles_per_monster

    image = flip_y(image)
    for i in range(3):
        image = rotate(image)
        sea_monsters = find_sea_monster_in_image(image, sea_monster)
        if sea_monsters != 0:
            return tiles_per_image - sea_monsters*tiles_per_monster



tiles = parse_input(test)
unvisited = set(tiles)
first = unvisited.pop()
first.pos = (0, 0)
queue = [first]

while queue:
    tile = queue.pop(0)
    unvisited.discard(tile)
    for other in unvisited:
        neighbour = tile.share_edge(other)
        if neighbour is not None and neighbour not in queue:
            queue.append(neighbour)
prod = 1 
for tile in tiles:
    tile.crop_image()
    if len(tile.neighbours) == 2:
        prod *= tile.number
print(f"Part 1:\t{prod}\t({prod == 45443966642567})")
SEA_MONSTER = """\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #    
"""
# Translating the pattern to fields
sea_monster = [tuple(i for i, k in enumerate(line) if k == "#") for line in SEA_MONSTER.splitlines()]

image = assemble_image(tiles)
answer = find_rough_waters(image, sea_monster)
print(f"Part 2:\t{answer}\t\t({answer == 1607})")

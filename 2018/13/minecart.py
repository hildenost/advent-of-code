class Cart:

    def __init__(self, pos, direction):
        self.i, self.j = pos
        self.dir = direction
        self.intersections = 0

    def move(self, track_map):
        if self.dir == ">":
            self.j += 1
        elif self.dir == "<":
            self.j -= 1
        elif self.dir == "^":
            self.i -= 1
        elif self.dir == "v":
            self.i += 1

        ne_sw = {"<": "^", "^": "<", ">": "v", "v": ">"}
        nw_se = {"<": "v", "v": "<", ">": "^", "^": ">"}
        if track_map[self.i][self.j] == "\\":
            self.dir = ne_sw[self.dir]
        elif track_map[self.i][self.j] == "/":
            self.dir = nw_se[self.dir]
        elif track_map[self.i][self.j] == "+":
            if self.intersections % 3 == 1:
                self.dir = self.dir
            elif self.intersections % 3 == 0:
                self.dir = nw_se[self.dir] if self.dir in "<>" else ne_sw[self.dir]
            elif self.intersections % 3 == 2:
                self.dir = ne_sw[self.dir] if self.dir in "<>" else nw_se[self.dir]
            self.intersections += 1
        return self.i, self.j

    def __repr__(self):
        return f"Cart({self.i}, {self.j}, {self.dir})"

    def __eq__(self, other):
        return (self.i, self.j) == (other.i, other.j)

    def __lt__(self, other):
        return (self.i < other.i) or (self.i == other.i and self.j < other.j)


def print_tracks(grid, carts):
    for cart in carts:
        grid[cart.i][cart.j] = cart.dir
    for i, g in enumerate(grid):
        print(
            "".join(g)
            )

def parse_input(filename="test_input.txt"):
    with open(filename) as f:
        return [list(line.strip("\n")) for line in f]


def initialise_carts(grid):
    carts = []
    for i, g in enumerate(grid):
        for j, c in enumerate(g):
            if c in "<>^v":
                carts.append(Cart((i, j), c))
                grid[i][j] = "-" if c in "<>" else "|"
    return grid, sorted(carts)


fyle = "input.txt"

track_map = parse_input(fyle)
track_map, tracks = initialise_carts(track_map)

while len(tracks) > 1:
    crashes = set()

    for i, cart in enumerate(tracks):
        if (cart.i, cart.j) in crashes:
            continue
        new_pos = cart.move(track_map)
        if cart in tracks[:i]+tracks[i+1:]:
            crashes.add(new_pos)

    tracks = [cart for cart in sorted(tracks) if (cart.i, cart.j) not in crashes]

print(tracks)

class Pos:
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps

    def __add__(self, other):
        new_steps = self.steps + abs(other[0]) + abs(other[1])
        return Pos(
            self.x + other[0],
            self.y + other[1],
            new_steps
        )

    def __sub__(self, other):
        return Pos(
            self.x - other[0],
            self.y - other[1],
            self.steps + abs(other[0]) + abs(other[1]),
        )

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __repr__(self):
        return f"Pos({self.x}, {self.y}, {self.steps})"


def parse_input(path):
    steps = path.split(",")
    path = set()
    curr_pos = Pos(0, 0, 0)
    for step in steps:
        no_steps = int(step[1:])
        if step[0] == "R":
            for i in range(no_steps):
                new = curr_pos + (0, i + 1)
                path.add(new)
            curr_pos += (0, no_steps)
        elif step[0] == "L":
            for i in range(no_steps):
                new = curr_pos + (0, -(i+1))
                path.add(new)
            curr_pos += (0, -1 * no_steps)
        elif step[0] == "U":
            for i in range(no_steps):
                path.add(curr_pos + (i + 1, 0))
            curr_pos += (no_steps, 0)
        elif step[0] == "D":
            for i in range(no_steps):
                path.add(curr_pos + (- (i + 1), 0))
            curr_pos -= (no_steps, 0)
    path_dict = {(pos.x, pos.y): pos.steps for pos in path}
    return path_dict


def closest(intersections):
    return min(abs(x) + abs(y) for x, y in intersections)


### VARIOUS INPUTS
wire1 = "R8,U5,L5,D3"
wire2 = "U7,R6,D4,L4"
wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"
wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

### PROBLEM INPUT
with open("input.txt", "r") as f:
   wire1, wire2 = f.readlines()

### Interpreting the routes
path1 = parse_input(wire1.strip())
path2 = parse_input(wire2.strip())

intersections = path1.keys() & path2.keys()

### PART 1
print(closest(intersections))

### PART 2
min_sum = min(path1[key] + path2[key] for key in intersections)
print(min_sum)

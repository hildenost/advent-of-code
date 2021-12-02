instructions = """\
F10
N3
F7
R90
F11
"""

with open("input.txt") as f:
    instructions = f.read()

coords = [(line[0], int(line[1:])) for line in instructions.splitlines()]

class Ship:

    def __init__(self, heading="E"):
        self.heading = heading
        self.pos_x = 0
        self.pos_y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1

    def add_degrees(self, degrees):
        degree_dict = {"N": 0, "E": 90, "S": 180, "W": 270}
        conversions = {0: "N", 90: "E", 180: "S", 270: "W"}
        new_heading = (360 + degree_dict[self.heading] + degrees) % 360
        self.heading = conversions[new_heading]

    def rotate_waypoint(self, degrees):
        degrees = (360 + degrees) % 360
        cos = {0: 1, 90: 0, 180: -1, 270: 0, -90: 0}
        sin = {0: 0, 90: 1, 180: 0, 270: -1, -90: -1}

        x = self.waypoint_x*cos[degrees] - self.waypoint_y*sin[degrees] 
        y = self.waypoint_x*sin[degrees] + self.waypoint_y*cos[degrees] 

        self.waypoint_x = x
        self.waypoint_y = y



    def move2(self, action, value):
        if action == "F":
            self.pos_x += self.waypoint_x * value
            self.pos_y += self.waypoint_y * value

        if action == "N":
            self.waypoint_y += value
        elif action == "S":
            self.waypoint_y -= value
        elif action == "W":
            self.waypoint_x -= value
        elif action == "E":
            self.waypoint_x += value

        elif action in ["R", "L"]:
            sign = -1 if action == "R" else 1
            self.rotate_waypoint(sign * value)

    def move(self, action, value):
        if action == "F":
            action = self.heading

        if action == "N":
            self.pos_y += value
        elif action == "S":
            self.pos_y -= value
        elif action == "W":
            self.pos_x -= value
        elif action == "E":
            self.pos_x += value
        elif action == "R":
            self.add_degrees(value)
        elif action == "L":
            self.add_degrees(-value)
        
    def get_manhattan(self):
        return abs(self.pos_x) + abs(self.pos_y)

    def __repr__(self):
        return f"({self.pos_x}, {self.pos_y}) heading {self.heading} waypoint {self.waypoint_x, self.waypoint_y}"

ship = Ship()
for coord in coords:
    ship.move2(*coord)
print(ship.get_manhattan())

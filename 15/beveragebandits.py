"""Module that sort of solves Day 15 of Advent of Code 2018.

It is messy and buggy, but provides the correct answer for Part 1,
and eventually provides the correct answer for Part 2 after some
false positives.

I was gonna refactor, but then I didn't.
"""

DIRS = ((0, -1), (-1, 0), (1, 0), (0, 1))
class Node:
    def __init__(self, pos, distance=0, parent=None):
        self.parent = parent
        self.pos = pos
        self.distance = distance

    def __repr__(self):
        return {self.pos}

class Unit:
    """Class for all kinds of units involved in the battle."""
    def __init__(self, pos, typ):
        self.x, self.y = pos
        self.typ = typ
        self.power = 3 if self.typ == 'G' else 16
        self.hp = 200
        self.target = None

    def __lt__(self, other):
        """To sort a list of units, they are sorted by position."""
        return self.y < other.y or (self.y == other.y and self.x < other.x)

    def __eq__(self, pos):
        """To check whether a unit exist in on a given position."""
        return (self.x, self.y) == pos

    def __repr__(self):
        """For debugging."""
        return f"{self.typ}({self.x}, {self.y}, {self.hp})"

    def __sub__(self, other):
        """Is this even used?"""
        return (-self.x + other[0], -self.y + other[1])

    def is_enemy(self, other):
        """One simply does not attack one of ones peers!"""
        return self.typ != other.typ

    def move(self, gridmap, units):
        """This method do a tad bit too much, so should consider refactoring.
        First it identifies all enemy units on grid, and then find valid squares
        surrounding these units. <-- This does not have to be a Unit method, it
        should be global.
        If there is an enemy next to the unit, the unit just attacks that one
        instead of exploring paths to the other units.
        If no targets could be reached and there is no target nearby, nothing happens.
        """
        in_range = self._squares_in_range(gridmap, units)
        if not isinstance(in_range, Unit):
            dx, dy = self._reachable_squares(gridmap, units, in_range)
            self.x += dx
            self.y += dy
            in_range = self._find_target(units)

        if in_range:
            if self.target is None:
                self.target = in_range
            self.attack(in_range, units)
        return bool(in_range)

    def attack(self, unit, units):
        """Attacking is deducting hit points from enemy."""
        unit.hp -= self.power
        if unit.hp <= 0:
            # The enemy died :(
            # ! This does not affect the main unit loop !
            units.remove(unit)

    def _reachable_squares(self, gridmap, units, in_range):
        # Have to do breadth-first search
        queue = []
        root = Node((self.x, self.y), distance=0)

        visited = {(self.x, self.y)}
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node.pos in in_range:
                while True:
                    if node.parent == root:
                        return (node.pos[0] - root.pos[0], node.pos[1] - root.pos[1])
                    node = node.parent
                break
            for dx, dy in DIRS:
                next_node = (node.pos[0] + dx, node.pos[1] + dy)
                if next_node not in visited and gridmap[next_node[1]][next_node[0]] == "." and next_node not in units:
                    visited.add(next_node)
                    queue.append(Node(next_node, parent=node, distance=node.distance + 1))
        return (0, 0)

    def _find_target(self, units):
        targets = [(unit.hp, unit)
                   for unit in units
                   for dx, dy in DIRS
                   if (self.x + dx, self.y + dy) == unit and self.is_enemy(unit)
        ]
        return min(targets)[1] if targets else False


    def _squares_in_range(self, gridmap, units):
        # first check whether you're standing next to an enemy

        target = self._find_target(units)
        if target:
            return target

        squares = {
            (unit.x + dx, unit.y + dy)
            for dx, dy in DIRS
            for unit in units
            if self.is_enemy(unit)
            and gridmap[unit.y + dy][unit.x + dx] == "."
            and (unit.x + dx, unit.y + dy) not in units
        }
        return squares


def is_valid_move(step, goal):
    return all(abs(s) <= abs(g) for s, g in zip(step, goal))


def is_valid_square(x, y, gridmap, units):
    return gridmap[y][x] == "." and (x, y) not in units


def initialise_map(input_map):
    grid = input_map.split("\n")
    units = []
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile in "EG":
                units.append(Unit((x, y), tile))
        grid[y] = row.replace("G", ".")
        grid[y] = grid[y].replace("E", ".")
    return units, grid

def print_map(grid, units, hp=False):
    output = []
    for y, row in enumerate(grid):
        line = "".join(
                units[units.index((x, y))].typ
                if (x, y) in units else tile
                for x, tile in enumerate(row)
        )
        if hp:
            line += "\t"
            line += ", ".join(
                f"{units[units.index((x, y))].typ}({str(units[units.index((x, y))].hp)})"
                for x, __ in enumerate(row)
                if (x, y) in units)
        output.append(line)


    print("\n".join(output))

puzzle_input = "\n".join([
    "################################",
    "##################G..###########",
    "#################.....##########",
    "################...##..#########",
    "#####..#####..#######..#########",
    "#####.######....#####....#######",
    "#####.######GG.G.##G.....#######",
    "#####..#####..G.G#...G#.######.#",
    "######.######.......G.#..####..#",
    "####...G######.......EE..E.##..#",
    "####......####.....#.E.........#",
    "#####.....#...G................#",
    "###....####...#####G..........##",
    "##.GG....##..#######.......#..##",
    "##......###.#########.........##",
    "#.....G...#.#########.........##",
    "#...G#......#########.......####",
    "#..G.#......#########.....######",
    "#.G..##.....#########....##.####",
    "#............#######......#E####",
    "#.....#.......#####.......G.####",
    "#...###............G.E...E.#####",
    "#..######...................####",
    "#########.................######",
    "#########...............########",
    "#########..........#.....E######",
    "#########....###...###......####",
    "#########....#####.###......####",
    "#######....#######.....##E.#####",
    "######.....########E.#####.#####",
    "#######..##########...##########",
    "################################",
])

input_map = "\n".join(["#######", "#.G.E.#", "#E.G.E#", "#.G.E.#", "#######"])
input_map = "\n".join(
    ["#######", "#.G...#", "#...EG#", "#.#.#G#", "#..G#E#", "#.....#", "#######"]
)
# input_map = "\n".join(["#######", "#E..G.#", "#...#.#", "#.G.#G#", "#######"])
#input_map = "\n".join(
#    [
#        "#########",
#        "#G..G..G#",
#        "#.......#",
#        "#.......#",
#        "#G..E..G#",
#        "#.......#",
#        "#.......#",
#        "#G..G..G#",
#        "#########",
#    ]
#)
#input_map = "\n".join([
#    "#######",
#    "#G..#E#",
#    "#E#E.E#",
#    "#G.##.#",
#    "#...#E#",
#    "#...E.#",
#    "#######",]
#)
input_map = "\n".join([
    "#######",
    "#E..EG#",
    "#.#G.E#",
    "#E.##E#",
    "#G..#.#",
    "#..E#.#",
    "#######",
])
input_map = "\n".join([
    "#######",
    "#E.G#.#",
    "#.#G..#",
    "#G.#.G#",
    "#G..#.#",
    "#...E.#",
    "#######",
])
input_map = "\n".join([
    "#######",
    "#.E...#",
    "#.#..G#",
    "#.###.#",
    "#E#G#G#",
    "#...#G#",
    "#######",
])
input_map = "\n".join([
    "#########",
    "#G......#",
    "#.E.#...#",
    "#..##..G#",
    "#...##..#",
    "#...#...#",
    "#.G...G.#",
    "#.....G.#",
    "#########",
])
#print(input_map)

units, grid = initialise_map(puzzle_input)
no_elfs = sum(1 for unit in units if unit.typ == 'E')
#units, grid = initialise_map(input_map)

rounds = 1
while True:
    targets = False
    for i, unit in enumerate(sorted(units)):
        if unit.hp <= 0:
            continue
        else:
            targets |= unit.move(grid, units)
        if len({unit.typ for unit in units}) == 1:
            targets = False
            break
    if not targets:
        rounds -= 1
        break
    rounds += 1


print_map(grid, units, hp=True)
print(f"Battle is over after {rounds} rounds!")
print(f"The {'Elfs' if units[0].typ == 'E' else 'Goblins'} won!")
no_elfs_after = sum(1 for unit in units if unit.typ == 'E')
print(f"There were {no_elfs} when battle started, now there's {no_elfs_after} left.")
hitpoints = sum(unit.hp for unit in units)
print(f"Hit point total of {hitpoints}")
print(f"BATTLE OUTCOME: {rounds * hitpoints}")

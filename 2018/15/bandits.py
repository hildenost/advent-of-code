""" Advent of Code 2018. Day 15: Beverage Bandits """

G = "G"
E = "E"

def parse(raw_grid, power=3):
    grid = {} 
    elves = []
    goblins = []
    for y, row in enumerate(raw_grid):
        for x, col in enumerate(row):
            if col == ".":
                grid[(y, x)] = True
            elif col == "E":
                grid[(y, x)] = False
                elves.append(Unit((y, x), col, power=power))
            elif col == "G":
                grid[(y, x)] = False
                goblins.append(Unit((y, x), col))
            # We ignore the walls
    
    return grid, elves, goblins

def manhattan(*ps):
    return sum(abs(a - b) for a, b in zip(*ps))

def get_in_range_squares(units, grid):
    squares = []
    for unit in units:
        y, x = unit.pos
        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            if grid.get((y+dy, x+dx), False):
                squares.append((y+dy, x+dx))
    return squares

class Unit:
    def __init__(self, pos, species, hp=200, power=3):
        self.pos = pos
        self.species = species
        self.hp = hp
        self.power = power

    def __repr__(self):
        return f"{self.species}({self.pos[1]}, {self.pos[0]}, {self.hp})"

    def __lt__(self, other):
        return self.pos < other.pos

    def turn(self, others, grid):
        grid = self.move(others, grid)
        return self.attack(others, grid)

    def move(self, others, grid):
        in_range_squares = get_in_range_squares(others, grid)

        if not in_range_squares:
            return grid

        in_range = [o for o in others
                    if manhattan(o.pos, self.pos) == 1]
        if in_range:
            # Ready to attack
            return grid

        # Ready to move
        # Freeing up the square
        grid[self.pos] = True
        # Move towards closest, reachable square
        self.pos = bfs(grid, self.pos, in_range_squares)

        # Return updated grid
        grid[self.pos] = False
        return grid

    def attack(self, others, grid):
        in_range = [o for o in others
                    if manhattan(o.pos, self.pos) == 1]

        if not in_range:
            return others, grid

        # Select the target with the fewest hp
        # or in case of tie, reading order
        target = min(in_range, key=lambda x: (x.hp, x.pos))

        target.hp -= self.power
        # target dies if hp <= 0
        if target.hp <= 0:
            grid[target.pos] = True
        return [o for o in others if o.hp > 0], grid

def bfs(grid, startnode, goals):
    queue = [startnode]

    dist = {startnode: 0}
    came_from = {startnode: None}

    THRESHOLD = 10000 
    candidates = []

    while queue:
        node = queue.pop(0)

        # We've found our multiple goals, exiting
        if dist[node] > THRESHOLD:
            break

        if node in goals:
            THRESHOLD = dist[node]
            candidates.append(node)
            continue

        # Adding neighbours in reading order
        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            next_pos = (node[0]+dy, node[1]+dx)
            if next_pos not in dist and grid.get(next_pos, False):
                queue.append(next_pos)
                # Track distance
                dist[next_pos] = 1 + dist[node]
                # Track path
                came_from[next_pos] = node 

    if not candidates:
        # Couldn't reach any goals, standing put
        return startnode

    # Select closest goal by reading order
    pos = min(candidates)
    # Tracing back until the square to take first step to
    while came_from[pos] != startnode:
        pos = came_from[pos]
    return pos 

def draw(grid, elves, goblins):
    elves = {elf.pos for elf in elves}
    goblins = {goblin.pos for goblin in goblins}

    xmin = min(x for y, x in grid)
    xmax = max(x for y, x in grid)
    print(xmin, xmax)
    ymin = min(y for y, x in grid)
    ymax = max(y for y, x in grid)
    print(ymin, ymax)
    for y in range(ymin-1, ymax+2):
        row = ""
        for x in range(xmin - 1, xmax +2):
            if (y, x) in elves:
                row += "E"
            elif (y, x) in goblins:
                row += "G"
            elif (y, x) in grid:
                row += "."
            else:
                row += "#"
        print(row)


def battle(grid, elves, goblins):
    n_elves = len(elves)
    rounds = 0
    while elves and goblins:
        for unit in sorted(elves + goblins):
            if not goblins or not elves:
                break

            if unit.hp <= 0:
                # Is dead, bye
                continue

            if unit.species == E:
                goblins, grid = unit.turn(goblins, grid)
            elif unit.species == G:
                elves, grid = unit.turn(elves, grid)
        else:
            # Only count full rounds
            # The else clause only executed when for loop completed
            rounds += 1
    return (rounds * sum(u.hp for u in elves+goblins),
            # Is True when elves won and no elves died
            not goblins and n_elves == len(elves)
    )

def increase_elves_attack(raw_grid):
    power = 3
    elves_win = False
    while not elves_win:
        # Increasing hp
        power += 1
        # Resetting grid
        grid, elves, goblins = parse(raw_grid, power)
        outcome, elves_win = battle(grid, elves, goblins)

    return outcome


with open("input_am.txt") as f:
    raw_grid = f.read().splitlines()

print("Part 1:\t", battle(*parse(raw_grid))[0])
print("Part 2:\t", increase_elves_attack(raw_grid))

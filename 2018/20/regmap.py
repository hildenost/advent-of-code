"""Solution to Day 20: A Regular Map doing some kind of recursive descent."""
import sys
sys.setrecursionlimit(5000)

test1 = "^WNE$"
test2 = "^ENWWW(NEEE|SSE(EE|N))$"
test3 = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
test4 = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
test5 = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
test6 = "^(NNNNNSSSSS|)E$"


class Room:
    def __init__(self, west=None, east=None, north=None, south=None, pos=None):
        self.west = west
        self.east = east
        self.north = north
        self.south = south
        self.pos = pos
        self.doors = 99999999999999

    def __lt__(self, other):
        return self.doors < other.doors

    def __eq__(self, other):
        return self.pos == other.pos

    def __hash__(self):
        return hash(self.pos)


def peek(regex):
    return regex[0]

def eat(regex):
    return regex.pop(0)

def get_steps(regex, room):
    next_c = peek(regex)
    if next_c in "NEWS":
        eat(regex)
        room = go_to_room(next_c, room)
        return next_c + get_steps(regex, room)
    elif next_c == "(":
        left_par = eat(regex)
        left_branch = get_steps(regex, room)
        right_branch = get_steps(regex, room)
        if right_branch == "|":
            get_steps(regex, room)
        get_steps(regex, room)
        return ""
    elif next_c == "|":
        eat(regex)
        return "|"
    elif next_c == ")":
        eat(regex)
        return ""
    elif next_c == "$":
        return ""

def go_to_room(step, room):
    if step == "W":
        new_room = Room(east=room, pos=(room.pos[0]-1, room.pos[1]))
        room.west = new_room
    elif step == "E":
        new_room = Room(west=room, pos=(room.pos[0]+1, room.pos[1]))
        room.east = new_room
    elif step == "N":
        new_room = Room(south=room, pos=(room.pos[0], room.pos[1]-1))
        room.north = new_room
    elif step == "S":
        new_room = Room(north=room, pos=(room.pos[0], room.pos[1]+1))
        room.south = new_room
    return new_room


def map_creator(regex):
    tokens = list(regex)

    start = Room(pos=(0, 0))
    start.doors = 0

    tokens.pop(0)
    get_steps(tokens, start)

    return start

def traverse_map(start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        visited.add(node)
        if node.west is not None and node.west not in visited:
            node.west.doors = min(node.west.doors, node.doors + 1)
            stack.append(node.west)
        if node.east is not None and node.east not in visited:
            node.east.doors = min(node.east.doors, node.doors + 1)
            stack.append(node.east)
        if node.north is not None and node.north not in visited:
            node.north.doors = min(node.north.doors, node.doors + 1)
            stack.append(node.north)
        if node.south is not None and node.south not in visited:
            node.south.doors = min(node.south.doors, node.doors + 1)
            stack.append(node.south)
    return visited

def get_furthest(rooms):
    room_list = list(rooms)
    max_doors = room_list[0].doors
    count = 0
    for room in room_list:
        max_doors = max(max_doors, room.doors)
        if room.doors >= 1000:
            count += 1
    return max_doors, count

def solve(regex):
    start = map_creator(regex)
    rooms = traverse_map(start)
    return get_furthest(rooms)

#assert solve(test1) == 3
#assert solve(test2) == 10
#assert solve(test3) == 18
#assert solve(test4) == 23
#assert solve(test5) == 31

with open("input.txt", "r") as f:
    regex = f.read()
    print(solve(regex))

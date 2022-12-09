""" Advent of Code 2022. Day 9: Rope Bridge """
with open("input.txt") as f:
    moves = f.read().splitlines()

dirs = {
    "R": lambda x, y: (x+1, y),
    "L": lambda x, y: (x-1, y),
    "U": lambda x, y: (x, y+1),
    "D": lambda x, y: (x, y-1),
}

def move_knot(head, tail):
    dx, dy = [abs(a-b)//(a-b) if a!=b else a-b for a, b in zip(head, tail)]
    return (tail[0]+dx, tail[1]+dy)

def touches(head, tail):
    return all(abs(a-b)<2 for a, b in zip(head, tail))

def move_rope(knots):
    visited = {(0, 0)}
    rope = [(0, 0) for __ in range(knots)]
    for move in moves:
        d, steps = move.split()
        for __ in range(int(steps)):
            # Moving the head
            rope[0] = dirs[d](*rope[0])
            # Moving the rest
            for i, j in zip(range(knots), range(1, knots)):
                if touches(rope[i], rope[j]):
                    # If they are touching, then the rest of the knots don't move either
                    break
                rope[j] = move_knot(rope[i], rope[j])
            visited.add(rope[-1])
    return len(visited)
print("Part 1:\t", move_rope(knots=2))
print("Part 2:\t", move_rope(knots=10))

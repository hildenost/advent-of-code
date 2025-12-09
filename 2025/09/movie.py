""" Advent of Code 2025. Day 9: Movie Theater """
 
with open("input.txt") as f:
    tiles = f.read().splitlines()

#tiles = """\
#7,1
#11,1
#11,7
#9,7
#9,5
#2,5
#2,3
#7,3
#""".splitlines()

tiles = [
    tuple(int(n) for n in row.split(","))
    for row in tiles
]

from itertools import combinations

def area(p1, p2):
    return (abs(p2[1]-p1[1])+1) * (abs(p2[0]-p1[0])+1)


part1 = max(area(p1, p2) for p1, p2 in combinations(tiles, 2))
print("Part 1:\t", part1)

areas = [(area(p1, p2), p1, p2) for p1, p2 in combinations(tiles, 2)]

def is_between(a, b, c):
    return (
        (a[1] == c[1] and a[0] < c[0] < b[0]) or
        (a[1] == c[1] and b[0] < c[0] < a[0]) or
        (a[0] == c[0] and a[1] < c[1] < b[1]) or 
        (a[0] == c[0] and b[1] < c[1] < a[1])
    )

def is_green(p):
    """Check inside point of the alleged rectangle is green"""
    # if the point is also in another rectangle
    pass



def is_inside(p1, p2):
    # If any other point A exists
    # so that p1[0] <= A[0] <= p2[0]
    #      or p1[1] <= A[1] <= p2[1]
    # rectangle is not correct
    for A in tiles:
        if A == p1 or A == p2:
            continue
        if is_between(p1, p2, A):
            return True
    return False


for a, p1, p2 in sorted(areas, reverse=True):
    print(a, p1, p2, is_inside(p1, p2))
    if not is_inside(p1, p2):
        print(a)
        input()


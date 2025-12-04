""" Advent of Code 2025. Day 4: Printing Department """

with open("input.txt") as f:
    grid = f.read().splitlines()

paper = set()
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "@":
            paper.add((i, j))

dirs = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0),
    (1,1),
    (1,-1),
    (-1,1),
    (-1,-1)
]


def to_remove(papergrid):
    neighbours = lambda i, j: sum((i+di, j+dj) in papergrid for di, dj in dirs)

    return {
        (i, j)
        for i, j in papergrid
        if neighbours(i, j) < 4
    }

n_paper = len(paper)

candidates = to_remove(paper)
# update paper
paper -= candidates
print("Part 1:\t", len(candidates))

while candidates:
    candidates = to_remove(paper)
    # update paper
    paper -= candidates


n_final = len(paper)
print("Part 2:\t", n_paper-n_final)

 

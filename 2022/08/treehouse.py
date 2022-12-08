""" Advent of Code 2022. Day 8: Treetop Tree House """
from itertools import takewhile

with open("input.txt") as f:
    forest = f.read().splitlines()

trees = set()
height, width = len(forest), len(forest[0])
# Horisontal sightlines
for i in range(height):
    left = forest[i][0]
    right = forest[i][-1]

    trees.add((i, 0))
    trees.add((i, width-1))
    for j in range(1, width):
        if left < forest[i][j]:
            trees.add((i, j))
            left = forest[i][j]
        if right < forest[i][width-j]:
            trees.add((i, width-j))
            right = forest[i][width-j]
# Vertical sightlines
for j in range(width):
    down = forest[0][j]
    up = forest[-1][j]

    trees.add((0, j))
    trees.add((height-1, j))
    for i in range(1, height):
        if down < forest[i][j]:
            trees.add((i, j))
            down = forest[i][j]

        if up < forest[height-i][j]:
            trees.add((height-i, j))
            up = forest[height-i][j]

print("Part 1:\t", len(trees))

## Part 2
highest = 0
for k in range(width):
    for i in range(height):
        # Add all visible trees
        right = len(list(
            takewhile(
                lambda x: x<forest[k][i],
                (forest[k][j] for j in range(i+1, width))
                )
            ))
        left = len(list(
            takewhile(
                lambda x: x<forest[k][i],
                (forest[k][j] for j in range(i-1, -1,-1))
                )
            ))
        down = len(list(
            takewhile(
                lambda x: x<forest[k][i],
                (forest[m][i] for m in range(k+1, height))
                )
            ))
        up = len(list(
            takewhile(
                lambda x: x<forest[k][i],
                (forest[m][i] for m in range(k-1, -1,-1))
                )
            ))

        # Adjust counts
        # Add 1 unless tree is at edge or all trees until edge are visible
        right += (i != width-1 and (width-1-i)!=right)
        left += (i != 0 and i!=left)
        up += (k != 0 and k!=up)
        down += (k != height-1 and (height-1-k)!=down)

        highest = max(highest, right*left*up*down) 

print("Part 2:\t", highest)

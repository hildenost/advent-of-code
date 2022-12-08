""" Advent of Code 2022. Day 8: Treetop Tree House """
from itertools import takewhile

with open("input.txt") as f:
    sample = f.read()

trees = set()
for i, row in enumerate(sample.splitlines()):
    prev = row[0]
    trees.add((i, 0))
    for j, col in enumerate(row[1:]):
        if prev < col:
            trees.add((i, j+1))
            prev = col

    rev = row[::-1]
    prev = rev[0]
    trees.add((i, len(row)-1))
    for j, col in enumerate(rev[1:]):
        if prev < col:
            trees.add((i, len(row)-j-2))
            prev = col

s = sample.splitlines()
for j in range(len(s[0])):
    prev = s[0][j]
    trees.add((0, j))
    for i in range(1, len(s)):
        if prev < s[i][j]:
            trees.add((i, j))
            prev = s[i][j]

    prev = s[-1][j]
    trees.add((len(s)-1, j))
    for i in range(len(s)-2, -1, -1):
        if prev < s[i][j]:
            trees.add((i, j))
            prev = s[i][j]

print("Part 1:\t", len(trees))

## Part 2
highest = 0
for k in range(len(s)):
    for i in range(len(s[k])):
        right = len(list(takewhile(lambda x: x<s[k][i], (s[k][j] for j in range(i+1, len(s[k]))))))
        left = len(list(takewhile(lambda x: x<s[k][i], (s[k][j] for j in range(i-1, -1,-1)))))
        down = len(list(takewhile(lambda x: x<s[k][i], (s[m][i] for m in range(k+1, len(s))))))
        up = len(list(takewhile(lambda x: x<s[k][i], (s[m][i] for m in range(k-1, -1,-1)))))
        right += (i != len(s[k])-1 and (len(s[k])-1-i)!=right)
        left += (i != 0 and i!=left)
        up += (k != 0 and k!=up)
        down += (k != len(s)-1 and (len(s)-1-k)!=down)
        highest = max(highest, right*left*up*down) 

print("Part 2:\t", highest)

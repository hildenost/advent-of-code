""" Advent of Code 2022. Day 4: Camp Cleanup """

sample = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

with open("input.txt") as f:
    sample = f.read()

pairs = [[[
    int(n)
    for n in elf.split("-")]
    for elf in pair.split(",")] 
    for pair in sample.split()
]

def is_within(a, b, x, y):
    return a <= x <= y <= b or x <= a <= b <= y

def is_intersect(a, b, x, y):
    return a <= x <= b <= y or x <= a <= y <= b or is_within(a, b, x, y)


print("Part 1:\t", sum(is_within(*A, *B) for A, B in pairs))
print("Part 2:\t", sum(is_intersect(*A, *B) for A, B in pairs))


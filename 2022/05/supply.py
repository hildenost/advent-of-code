""" Advent of Code 2022. Day 5: Supply Stacks """
import re

with open("input.txt") as f:
    crates, moves = f.read().split("\n\n")

# Parse the crates
crates = crates.splitlines()
poses = [m.start() for m in re.finditer("\d", crates[-1])]

stacks = [[] for __ in poses]
for level in reversed(crates[:-1]):
    for s, i in zip(stacks, poses):
        if level[i].isalpha():
            s.append(level[i])

stacks = [s[::-1] for s in stacks]

# Parse the moves
pattern = r"move (\d+) from (\d) to (\d)"
parsed_moves = [
    [int(n) for n in re.findall(pattern, move)[0]] for move in moves.splitlines()
]


def work(stacks, parsed_moves, reverse=True):
    for number, fro, unto in parsed_moves:
        to_move = stacks[fro - 1][:number]
        if reverse:
            to_move = to_move[::-1]
        stacks[unto - 1] = to_move + stacks[unto - 1]
        stacks[fro - 1] = stacks[fro - 1][number:]
    return "".join(s[0] for s in stacks)


print("Part 1:\t", work(stacks.copy(), parsed_moves))
print("Part 2:\t", work(stacks, parsed_moves, reverse=False))

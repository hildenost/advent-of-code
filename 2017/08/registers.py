""" Advent of Code 2017. Day 8: I Heard You Like Registers """

instructions = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
""".splitlines()

with open("input.txt") as f:
    instructions = f.read().splitlines()

from collections import defaultdict

registers = defaultdict(int)

comparisons = {
    ">": lambda reg, v: registers[reg] > int(v),
    ">=": lambda reg, v: registers[reg] >= int(v),
    "<": lambda reg, v: registers[reg] < int(v),
    "<=": lambda reg, v: registers[reg] <= int(v),
    "==": lambda reg, v: registers[reg] == int(v),
    "!=": lambda reg, v: registers[reg] != int(v),
}

max_value = -10000

for line in instructions:
    reg, adjust, value, __, other_reg, cmp, other_value = line.split()

    if comparisons[cmp](other_reg, other_value):
        registers[reg] += int(value) if adjust == "inc" else -int(value)

    max_value = max(max_value, *registers.values())

print("Part 1:\t", max(registers.values()))
print("Part 2:\t", max_value)

""" Advent of Code 2016. Day 10: Balance Bots """

import re

instructions = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
""".splitlines()
with open("input.txt") as f:
    instructions = f.read().splitlines()

from collections import defaultdict
def parse(instructions):
    bots = defaultdict(list) 
    funcs = {}
    for instruction in instructions:
        res = [(t, int(n)) for t, n in re.findall(r"(\w+) (\d+)", instruction)]
        if len(res) == 2:
            bots[res[1][1]].append(res[0][1])
        else:
            funcs[res[0][1]] = res[1:]
    return bots, funcs


bots, funcs = parse(instructions)
outputs = defaultdict(int)

select = {0: min, 1: max}

while any(bots.values()):
    two_values = {k:v for k, v in bots.items() if len(v) == 2}
    for bot, values in two_values.items():
        if set(values) == {17, 61}:
            print("Part 1:\t",  bot)

        for i, (target, n) in enumerate(funcs[bot]):
            if target == "bot":
                bots[n].append(select[i](values))
            elif target == "output":
                outputs[n] = select[i](values)
        bots[bot] = []

print("Part 2:\t", outputs[0]*outputs[1]*outputs[2])

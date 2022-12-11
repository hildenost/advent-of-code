""" Advent of Code 2022. Day 11: Monkey in the Middle """
import re

with open("input.txt") as f:
    sample = f.read()

monkeys = []
ops = {
    0: lambda x: x+x,
    1: lambda x: x*x,
    2: lambda b: lambda x: x+b,
    3: lambda b: lambda x: x*b,
}

testing = lambda d, a, b: lambda x: b if x%d else a
monkops = []
monktests = []
# Multiplying all test factors together
superfactor = 1

for monkey in sample.split("\n\n"):
    __, items, op, test = monkey.split("\n", 3)

    items = [int(n) for n in re.findall(r"\d+", items)]
    monkeys.append(items)

    op, factor = re.findall(r"Operation: new = old ([+*]) (old|\d+)", op)[0]
    if (op, factor) == ("+", "old"):
        monkops.append(ops[0])
    elif (op, factor) == ("*", "old"):
        monkops.append(ops[1])
    elif op == "+":
        monkops.append(ops[2](int(factor)))
    elif op == "*":
        monkops.append(ops[3](int(factor)))

    dividend, T, F = [int(n) for n in re.findall(r"\d+", test)]
    monktests.append(testing(dividend, T, F))

    # Part 2
    # Multiplying all test factors together
    superfactor *= dividend

def play(ms, rounds=20, factor=3): 
    inspections = [0]*len(ms)
    for r in range(rounds):
        for monkey, items in enumerate(ms):
            while items:
                inspections[monkey] += 1
                item = items.pop(0)
                if factor == 3:
                    worry_level = monkops[monkey](item) // factor
                else:
                    worry_level = monkops[monkey](item) % factor
                to_monkey = monktests[monkey](worry_level)
                ms[to_monkey].append(worry_level)
    first, second = sorted(inspections, reverse=True)[:2]
    return first * second

print("Part 1:\t", play([m.copy() for m in monkeys]))
print("Part 2:\t", play(monkeys, rounds=10000, factor=superfactor))

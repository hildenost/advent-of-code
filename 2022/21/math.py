""" Advent of Code 2022. Day 21: Monkey Math"""
with open("input.txt") as f:
    monkeys = dict(line.split(": ") for line in f.read().splitlines())


ops = {
    "+": lambda a, b: a+b,
    "-": lambda a, b: a-b,
    "/": lambda a, b: a/b,
    "*": lambda a, b: a*b,
}

def dfs(expr, alert=False):
    if expr.isdigit():
        return int(expr)
    
    left, op, right = expr.split()

    if alert and "humn" in (left, right):
        return 

    resleft = dfs(monkeys[left], alert=alert)
    resright = dfs(monkeys[right], alert=alert)

    return ops[op](resleft, resright)
    
opsleft = {
    "+": lambda a, total: total-a,
    "-": lambda a, total: a-total,
    "/": lambda a, total: a/total,
    "*": lambda a, total: total/a,
}
opsright = {
    "+": lambda a, total: total-a,
    "-": lambda a, total: total+a,
    "/": lambda a, total: total*a,
    "*": lambda a, total: total/a,
}

def step(monkey, total):
    left, op, right = monkeys[monkey].split()

    try:
        if left == "humn":
            raise TypeError
        a = dfs(monkeys[left], alert=True)
        total = opsleft[op](a, total)
    except TypeError:
        next_monkey = left

    try:
        if right == "humn":
            raise TypeError
        a = dfs(monkeys[right], alert=True)
        total = opsright[op](a, total)
    except TypeError:
        next_monkey = right
    
    return next_monkey, total

left, op, right = monkeys["root"].split()
# Which side is "humn" hiding?
try:
    total = dfs(monkeys[left], alert=True)
except TypeError:
    next_monkey = left

try:
    total = dfs(monkeys[right], alert=True)
except TypeError:
    next_monkey = right

# Stepping through the expressions one by one
# One factor is solvable, so adjusting the known side accordingly
# as when solving equations by hand
while next_monkey != "humn":
    next_monkey, total = step(next_monkey, total)
# When next_monkey is humn, the answer lies in total

print("Part 1:\t", int(dfs(monkeys["root"])))
print("Part 2:\t", int(total))

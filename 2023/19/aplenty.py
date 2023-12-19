""" Advent of Code 2023. Day 19: Aplenty """
import re

with open("input.txt") as f:
    allrules, parts = f.read().split("\n\n")


def parse_rule(rule):
    m = re.search(
        r"(?P<name>[a-z]+)\{(?P<group>.*)\}",
        rule,
    )
    name = m["name"]

    steps = m["group"].split(",")
    parsed_steps = []
    for step in steps:
        temp = step.split(":")
        if len(temp) > 1:
            parsed_steps.append((temp[0][1], temp[0][0], int(temp[0][2:]), temp[1]))
        else:
            parsed_steps.append(temp)

    return {name: parsed_steps}


rules = dict()
for rule in allrules.splitlines():
    rules.update(parse_rule(rule))


def parse_parts(part):
    return {k: int(v) for k, v in zip("xmas", re.findall(r"\d+", part))}


parts = [parse_parts(part) for part in parts.splitlines()]

compare = {"<": lambda k, v: k < v, ">": lambda k, v: k > v}


def traverse(node, part):
    for check in rules[node]:
        match check:
            case c, k, v, goal:
                if compare[c](part[k], v):
                    if goal in "AR":
                        return goal == "A"
                    else:
                        return traverse(goal, part)
            case "R",:
                return False
            case "A",:
                return True
            case goal,:
                return traverse(goal, part)


total = sum(sum(part.values()) for part in parts if traverse("in", part))

print("Part 1:\t", total)


def compute_combos(xmas):
    n = 1
    for l, u in xmas.values():
        n *= u - l + 1
    return n


def traverse(node, xmas):
    # xmas holds a dict of tuples of inclusive lower and upper bounds
    nodescore = 0
    for check in rules[node]:
        match check:
            case "R",:
                continue
            case "A",:
                nodescore += compute_combos(xmas)
            case goal,:
                nodescore += traverse(goal, xmas)
            case c, k, v, goal:
                lower, upper = xmas[k]

                # Split the ranges
                new = (v + 1, upper) if c == ">" else (lower, v - 1)
                rest = (lower, v) if c == ">" else (v, upper)
                xmas.update({k: rest})

                if goal == "A":
                    nodescore += compute_combos({**xmas, k: new})
                elif goal == "R":
                    continue
                else:
                    nodescore += traverse(goal, {**xmas, k: new})
    return nodescore


bounds = {k: (1, 4000) for k in "xmas"}
total = traverse("in", bounds)
print("Part 2:\t", total)

""" Advent of Code 2023. Day 8: Haunted Wasteland """
from itertools import cycle
import re

with open("input.txt") as f:
    instructions, nodes = f.read().split("\n\n")


nodes = [re.findall(r"[A-Z]{3}", node) for node in nodes.splitlines()]
nodes = {k: {"L": l, "R": r} for k, l, r in nodes}


def traverse(curr, end="ZZZ"):
    s = 0
    for d in cycle(instructions):
        curr = nodes[curr][d]
        s += 1
        if curr.endswith(end):
            return s


start = "AAA"
print("Part 1:\t", traverse(start))

steps = [traverse(node, end="Z") for node in nodes if node.endswith("A")]

from math import gcd


def list_gcd(lst):
    res = gcd(*lst[:2])
    for x in lst[2:]:
        res = gcd(res, x)
    return res


g = list_gcd(steps)

# Multiply the primes together
primes = 1
for f in steps:
    primes *= f // g
# And finally multiply with the greatest common divisor to get
# the FIRST step at which all ends up at a Z node
print("Part 2:\t", primes * g)

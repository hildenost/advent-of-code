""" Advent of Code 2024. Day 21: Keypad Conundrum """
from moves import dirmoves, nummoves

with open("input.txt") as f:
    codes = f.read().splitlines()

A = "A"

from functools import cache


@cache
def dfs(orders, level=1, depth=3):
    if level == depth:
        # We are at my level, return my command
        return len(orders)

    # We always start at A
    poscode = A + orders
    mov = 0
    for a, b in zip(poscode, poscode[1:]):
        if a == b:
            # Same button, just submit
            mov += 1
            continue
        queue = []
        for option in dirmoves[(a, b)]:
            s = dfs(option + A, level + 1, depth)
            queue.append(s)

        mov += min(queue)

    return mov


def get_sequence(code, depth=3):
    poscode = [int(c) if c.isdigit() else c for c in "A" + code]
    cmd = 0
    for a, b in zip(poscode, poscode[1:]):
        queue = []
        for option in nummoves[(a, b)]:
            s = dfs(option + A, depth=depth)
            queue.append(s)
        cmd += min(queue)
    return cmd


# codes = ["029A", "980A", "179A", "456A", "379A"]
ans = sum(get_sequence(code, depth=3) * int(code[:-1]) for code in codes)
print("Part 1:\t", ans)

ans = sum(get_sequence(code, depth=26) * int(code[:-1]) for code in codes)
print("Part 2:\t", ans)

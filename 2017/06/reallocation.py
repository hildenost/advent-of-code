""" Advent of Code 2017. Day 6: Memory Reallocation """
import numpy as np

banks = np.array([0, 2, 7, 0])

banks = np.array([4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5])

seen = {tuple(banks)}
n = 0
seen_once = None
while True:
    n += 1

    i = banks.argmax()
    to_redistribute = banks[i]
    banks[i] = 0

    per_bank = to_redistribute // len(banks)
    modulo = to_redistribute % len(banks)

    new_blocks = np.full_like(banks, per_bank)

    if modulo != 0:
        # right hand side
        # overflowing indices are ignored
        new_blocks[i + 1 : i + 1 + modulo] += 1
        if i + modulo >= len(banks):
            # left hand side if overflowing
            new_blocks[: i + 1 + modulo - len(banks)] += 1

    banks += new_blocks

    if tuple(banks) not in seen:
        seen.add(tuple(banks))
    elif seen_once is None:
        seen_once = tuple(banks)
        print("Part 1:\t", n)
        n = 0
    elif tuple(banks) == seen_once:
        print("Part 2:\t", n)
        break


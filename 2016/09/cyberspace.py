""" Advent of Code 2016. Day 9: Explosives in Cyberspace """

import re

def decompress(line, nest=False):
    i = 0
    length = 0
    for m in re.finditer(r"\((\d+)x(\d+)\)", line):
        if i > m.start():
            # Match was nested
            continue
        A, B = [int(n) for n in m.groups()]
        # Adding the characters before decompressing command
        length += m.start() - i
        # Skipping until end of parentheses pair
        i = m.end()
        length += B * (A if not nest else decompress(line[i:i+A], nest=True))
        # Skipping past the decompressed word
        i += A

    # Adding the last characters
    return length + len(line[i:])

def find_length(lines, nest=False):
    return sum(decompress(line, nest) for line in lines)

assert 6 == decompress("ADVENT")
assert 7 == decompress("A(1x5)BC")
assert 9 == decompress("(3x3)XYZ")
assert 11 == decompress("A(2x2)BCD(2x2)EFG")
assert 6 == decompress("(6x1)(1x3)A")
assert 18 == decompress("X(8x2)(3x3)ABCY")
assert 9 == decompress("(3x3)XYZ", nest=True)
assert 20 == decompress("X(8x2)(3x3)ABCY", nest=True)
assert 241920 == decompress("(27x12)(20x12)(13x14)(7x10)(1x12)A", nest=True)
assert 445 == decompress("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", nest=True)

with open("input.txt") as f:
    lines = f.read().splitlines()

print("Part 1:\t", find_length(lines))
print("Part 2:\t", find_length(lines, nest=True))

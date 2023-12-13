""" Advent of Code 2023. Day 13: Point of Incidence """

with open("input.txt") as f:
    patterns = [pattern.splitlines() for pattern in f.read().split("\n\n")]


def transpose(pattern):
    return list(map(list, zip(*pattern)))


def find_reflection(pattern, old=None):
    """Returns -1 if no reflection found"""
    for row, (a, b) in enumerate(zip(pattern, pattern[1:]), 1):
        ok = False
        if a == b:
            # Reflection!
            # But is it valid?
            ok = all(
                pattern[i] == pattern[j]
                for i, j in zip(range(row - 1, -1, -1), range(row, len(pattern)))
            )
        # We short circuit here
        if ok and (old is None or row != old):
            return row
    return -1


def find_number(pattern, old=None):
    # test horisontal reflection
    row = find_reflection(pattern)
    if row > 0:
        # Found a horizontal reflection
        return 100 * row

    # Test vertical reflection
    pattern = transpose(pattern)
    return find_reflection(pattern)


oldies = {n: find_number(pattern) for n, pattern in enumerate(patterns)}

print("Part 1:\t", sum(oldies.values()))

total = 0
for n, pattern in enumerate(patterns):
    # Let's make it mutable MUHAHAHA
    pattern = [list(row) for row in pattern]

    # Create smudges
    ijs = ((i, j) for i in range(len(pattern)) for j in range(len(pattern[0])))
    value = 0
    for i, j in ijs:
        p = [
            [
                cell if (k, l) != (i, j) else ".#"[cell == "."]
                for l, cell in enumerate(row)
            ]
            for k, row in enumerate(pattern)
        ]

        oldrow = oldies[n] // 100 if oldies[n] >= 100 else None

        # test horisontal reflection
        row = find_reflection(p, oldrow)
        if row > 0:  # and oldies[n] != 100 * row:
            # Found a horizontal reflection
            # print("SMUDGE ", i, j, "\t ROW:", 100 * row, oldies[n], oldrow)
            value = 100 * row
            break

        oldcol = oldies[n] if oldies[n] < 100 else None
        # Test vertical reflection
        # Apparently there was no valid horizontal reflection
        p = transpose(p)
        col = find_reflection(p, oldcol)
        if col > 0:  # and oldies[n] != col:
            # Found a vertical reflection
            # print("SMUDGE ", i, j, "\t COL", col, oldies[n], oldcol)
            value = col
            break
    total += value
print("Part 2:\t", total)

""" Advent of Code 2025. Day 5: Cafeteria """

with open("input.txt") as f:
    ranges, ids = f.read().split("\n\n")

ranges = [tuple(int(n) for n in r.split("-")) for r in ranges.splitlines()]

n_fresh = sum(
    # Using any to avoid double and triple etc counting
    any(l <= int(i) <= u for l, u in ranges)
    for i in ids.splitlines())
print("Part 1:\t", n_fresh)


ranges = sorted(ranges)
merged = set()

while ranges:
    l, u = ranges.pop()

    new_merged = merged

    for a, b in sorted(merged):
        if a <= l <= u <= b:
            # New range included in tracked range
            break
        elif l <= a <= b <= u:
            # New range enclosing tracked range
            new_merged.remove((a, b))
            new_merged.add((l, u))
            break
        elif a <= l <= b:
            # Lower boundary in tracked range
            new_merged.remove((a, b))
            new_merged.add((a, u))
            break
        elif a <= u <= b:
            # Upper boundary in tracked range
            new_merged.remove((a, b))
            new_merged.add((l, b))
            break
    else:
        # If for loop not ended with break
        # range outside of tracked ranges
        new_merged.add((l, u))


    merged = new_merged


print("Part 2:\t", sum(u-l+1 for l, u in merged))

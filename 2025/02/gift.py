""" Advent of Code 2025. Day 2: Gift Shop """

ranges = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""

with open("input.txt") as f:
    ranges = f.read()


ids = ranges.strip().split(",")

idsum = 0

for id in ids:
    lower, upper = id.strip().split("-")
    # If both first and last has odd number of digits
    # id is not fake
    # Not needed for correctness, just speed
    if len(lower) % 2 and len(upper) % 2:
        continue

    # The limit with even number of digits
    # decides how many digits the repeated sequence should be
    if len(lower) % 2:
        id_len = len(upper) // 2
    else:
        id_len = len(lower) // 2

    a = int(lower[:-id_len]) if id_len < len(lower) else 0
    b = int(upper[:-id_len])

    l, u = int(lower), int(upper)

    for n in range(a, b+1):
        # Constructing a potential fake
        potential_fake = int(str(n)+str(n))
        # If within range, label as fake
        if l <= potential_fake <= u:
            idsum += potential_fake
print("Part 1:\t", idsum)

fakes = set()
idsum = 0
for id in ids:
    lower, upper = id.strip().split("-")

    # The limit with even number of digits
    # decides how many digits the repeated sequence should be
    if len(lower) % 2:
        id_len = len(upper) // 2
    else:
        id_len = len(lower) // 2

    a = int(lower) // (10**id_len)
    b = int(upper) // (10**id_len)
    l, u = int(lower), int(upper)

    fakes |= {
        int(r*str(n)[:i])
        for n in range(a, b+1)
        for i in range(1, len(str(n))+1)
        for r in (len(lower) // i, len(upper) // i)
        if r > 1 and l <= int(r*str(n)[:i]) <= u
    }

print("Part 2:\t", sum(fakes))

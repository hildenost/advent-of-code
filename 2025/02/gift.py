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


idsum = 0

fakes = set()
for id in ids:
    print(f"======{id}=====")
    lower, upper = id.strip().split("-")

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
            fakes.add(potential_fake)

        if len(str(n)) == 1:
            i = 1
            x, y = len(lower) // i, len(upper) // i
            
            # In this case, if the potential fake has length 1,
            # it is not a fake

            potential_fake = int(x*str(n)[:i])
            if x > 1 and l <= potential_fake <= u:
                print("Fake: \t", potential_fake)
                fakes.add(potential_fake)
            if x != y:
                potential_fake = int(y*str(n)[:i])
                if l <= potential_fake <= u:
                    print("Fake: \t", potential_fake)
                    fakes.add(potential_fake)


        # There can be more fakes
        for i in range(1, len(str(n))):
            x, y = len(lower) // i, len(upper) // i
            potential_fake = int(x*str(n)[:i])
            if l <= potential_fake <= u:
                print("Fake: \t", potential_fake)
                fakes.add(potential_fake)
            if x != y:
                potential_fake = int(y*str(n)[:i])
                if l <= potential_fake <= u:
                    print("Fake: \t", potential_fake)
                    fakes.add(potential_fake)
print(fakes)

print("Part 2:\t", sum(fakes))


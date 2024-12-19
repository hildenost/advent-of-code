""" Advent of Code 2024. Day 19: Linen Layout """


(
    towels,
    designs,
) = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".split(
    "\n\n"
)

with open("input.txt") as f:
    towels, designs = f.read().split("\n\n")

towels = [t.strip() for t in towels.split(",")]
designs = designs.splitlines()

cache = {}

for towel in towels:
    cache[towel] = True


def search(word):
    if cache.get(word) is not None:
        return cache[word]

    if len(word) == 1:
        cache[word] = False
        return cache[word]

    # Split search
    for p in range(1, len(word)):
        left = search(word[:p])
        if not left:
            continue

        right = search(word[p:])
        if not right:
            continue

        # Both values found
        cache[word] = True
        break
    else:
        cache[word] = False

    return cache[word]


total = 0
for design in designs:
    total += search(design)
print("Part 1:\t", total)


def search2(word):
    if cache.get(word) is not None:
        return cache[word]

    if len(word) == 1:
        cache[word] = 0
        return cache[word]

    # Split search
    count = 0
    for p in range(1, len(word)):
        if word[:p] not in towels:
            continue

        right = search2(word[p:])
        if not right:
            continue

        # Both sides valid
        count += right

    cache[word] = count

    return cache[word]


# Create initial cache of towels
# Check the multiletter towels whether they can be decomposed
cache = {}

for towel in sorted(towels, key=len):
    cache[towel] = 1
    # Split search for alternatives
    for p in range(1, len(towel) + 1):
        if towel[:p] not in towels:
            continue

        right = search2(towel[p:])
        if not right:
            continue

        # Both values found
        cache[towel] += right

total = 0
for design in designs:
    res = search2(design)
    total += res
print("Part 2:\t", total)

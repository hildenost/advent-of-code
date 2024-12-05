""" Advent of Code 2024. Day 5: Print Queue """

with open("input.txt") as f:
    rules, updates = f.read().split("\n\n")

# Parse rules
from collections import defaultdict

r = defaultdict(set)
for rule in rules.splitlines():
    a, b = rule.split("|")
    r[a].add(b)
rules = r


def is_valid(page, after):
    # If the after pages is a subset of the rules
    # Then it's OK
    return set(after) <= rules[page]


def is_update_valid(pages):
    return all(is_valid(page, after=pages[i + 1 :]) for i, page in enumerate(pages))


ok_total = 0
wrong_total = 0
for update in updates.splitlines():
    pages = update.split(",")

    if is_update_valid(pages):
        ok_total += int(pages[len(pages) // 2])

    if not is_update_valid(pages):
        # Do error checking
        i = 0
        while i < len(pages):
            wrongs = set(pages[i + 1 :]) - rules[pages[i]]
            if wrongs:
                # We swap places with the worst offender
                swap_to = max(pages.index(w) for w in wrongs)
                pages[i], pages[swap_to] = pages[swap_to], pages[i]
                continue
            i += 1

        wrong_total += int(pages[len(pages) // 2])
print("Part 1:\t", ok_total)
print("Part 2:\t", wrong_total)

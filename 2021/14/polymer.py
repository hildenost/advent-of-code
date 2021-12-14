""" Advent of Code 2021. Day 14: Extended Polymerization """

template = "NNCB"
rules = """CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".splitlines()

with open("input.txt") as f:
    template, rules = f.read().split("\n\n")  
    rules = rules.splitlines()

def parse(rules):
    return dict(rule.split(" -> ") for rule in rules)

rules = parse(rules)

from collections import Counter


def pair_insertion(days):
    # Initializing the pair counter
    c = Counter([a+b for a, b in zip(template, template[1:])])

    for __ in range(days):
        new_c = Counter()
        for p in c:
            new_c.update({p[0]+rules[p]: c[p], rules[p]+p[1]: c[p]})
        c = new_c

    # Converting the counts back to individual elements
    final = Counter()
    for (a, b), n in c.items():
        final[a] += n
        final[b] += n

    most, *__, least = final.most_common()

    # The element count is half the total count, as BN and NC is counted
    # twice for N
    # Must add 1 if the element is at either end
    a = most[1] // 2 + 1 if most[0] in (template[0], template[-1]) else most[1] // 2
    b = least[1] // 2 + 1 if least[0] in (template[0], template[-1]) else least[1] // 2
    return a - b

print("Part 1:\t", pair_insertion(10))
print("Part 2:\t", pair_insertion(40))

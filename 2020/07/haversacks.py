import re


test_ruleset = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""
second_testset = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

with open("07/input.txt") as f:
    ruleset = f.read()

pattern = re.compile(r"(?P<number>\d+)?(?: )?(?P<colour>[a-z]+ [a-z]+) bag[s]?")


def parse_ruleset(ruleset):
    rules = {}
    for rule in ruleset.splitlines():
        parent, *children = pattern.finditer(rule)
        rules[parent["colour"]] = {
            child["colour"]: int(child["number"])
            if child["number"] is not None
            else None
            for child in children
        }

    return rules


def search_shiny_gold(graph, bag):
    if "shiny gold" in graph[bag]:
        return True
    if "no other" in graph[bag]:
        return False

    return any(search_shiny_gold(graph, child) for child in graph[bag])


def count_bags_in_shiny_gold(graph, bag):
    if "no other" in graph[bag]:
        return 0
    return sum(
        number + number * count_bags_in_shiny_gold(graph, child)
        for child, number in graph[bag].items()
    )


graph = parse_ruleset(ruleset)

### PART 1
print(sum(search_shiny_gold(graph, bag) for bag in graph))

### PART 2
print(count_bags_in_shiny_gold(graph, "shiny gold"))

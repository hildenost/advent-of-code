from collections import defaultdict
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

with open("07/input.txt") as f:
    ruleset = f.read()

pattern = re.compile(r"([a-z]+ [a-z]+) bag[s]?")


def parse_ruleset(ruleset):
    rules = defaultdict(set)
    for rule in ruleset.splitlines():
        parent, *children = pattern.findall(rule)
        rules[parent].update(children)
    return rules


def search_shiny_gold(visited, graph, bag):
    if bag not in visited:
        visited.add(bag)
        if "shiny gold" in graph[bag]:
            return True
        if "no other" in graph[bag]:
            return False

        return any(
            search_shiny_gold(visited, graph, children) for children in graph[bag]
        )
    return False


graph = parse_ruleset(test_ruleset)
graph = parse_ruleset(ruleset)

print(sum(search_shiny_gold(set(), graph, bag) for bag in graph))


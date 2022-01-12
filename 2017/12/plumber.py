""" Advent of Code 2017. Day 12: Digital Plumber """
import re

with open("input.txt") as f:
    programs = f.read().splitlines()

graph = {}
for program in programs:
    node, *children = re.findall(r"\d+", program)
    graph[node] = set(children)

# let's traverse!
def dfs(startnode):
    stack = [startnode]
    seen = set()
    while stack:
        node = stack.pop()
        seen.add(node)
        stack.extend(list(graph[node] - seen))
    return seen

group_0 = dfs("0")
print("Part 1:\t", len(group_0))

ungrouped_programs = set(graph) - group_0
count = 1
while ungrouped_programs:
    # Pop some random program not grouped already
    node = ungrouped_programs.pop()

    ungrouped_programs -= dfs(node)
    count += 1
print("Part 2:\t", count)










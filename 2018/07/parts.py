""" Advent of Code 2018. Day 7: The Sum of Its Parts """

with open("input.txt") as f:
    instructions = f.read().splitlines()

#instructions = """Step C must be finished before step A can begin.
#Step C must be finished before step F can begin.
#Step A must be finished before step B can begin.
#Step A must be finished before step D can begin.
#Step B must be finished before step E can begin.
#Step D must be finished before step E can begin.
#Step F must be finished before step E can begin.
#""".splitlines()

import re

from collections import defaultdict

children = defaultdict(set) 
parents = defaultdict(set)
for line in instructions:
    first, later = re.findall(r"\b[A-Z]\b", line)

    children[first].add(later)
    parents[later].add(first)

def topological_sort(children, parents):
    # The nodes without incoming edges
    queue = sorted(set(children) - set(parents))
    L = []
    while queue:
        queue.sort()
        n = queue.pop(0) 

        L.append(n)

        for child in children[n]:
            parents[child].discard(n)
            if not parents[child]:
                queue.append(child)
    return "".join(L)

def construct(children, parents, n_workers=5, delta=60):
    n_nodes = len(set(children).union(set(parents)))
    finished = set()
    # The first nodes without incoming edges
    queue = sorted(set(children) - set(parents))
    busy = {}
    sec = 0
    while queue or busy:

        # If there is capacity and there's a queue
        # assign tasks
        queue.sort()
        while len(busy) < n_workers and queue:
            n = queue.pop(0) 
            busy[n] = delta + ord(n) - 64

        busy = {n: t-1 for n, t in busy.items() if t > 0}
        for n, t in busy.items():
            if t == 0:
                # Task complete
                finished.add(n)

                for child in children[n]:
                    parents[child].discard(n)
                    if not parents[child] and child not in finished and child not in queue and child not in busy: 
                        queue.append(child)
        busy = {n: t for n, t in busy.items() if t > 0}

        sec += 1

        if len(finished) == n_nodes:
            return sec


print("Part 1:\t", topological_sort(children, parents))
children = defaultdict(set) 
parents = defaultdict(set)
for line in instructions:
    first, later = re.findall(r"\b[A-Z]\b", line)

    children[first].add(later)
    parents[later].add(first)
print("Part 2:\t", construct(children, parents, delta=60))




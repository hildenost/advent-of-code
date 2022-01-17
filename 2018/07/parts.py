""" Advent of Code 2018. Day 7: The Sum of Its Parts """

with open("input.txt") as f:
    instructions = f.read().splitlines()

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

def construct(children, parents, delta=60):
    # The nodes without incoming edges
    queue = sorted(set(children) - set(parents))
    finished = set()
    busy = {}
    workers = [0]*5
    for s in range(15):
        print(workers)
        popped = []
        for j, w in enumerate(workers):
            if w > 0:
                continue
            print("WORKER AVAILABLE!!!")
            # Selecting a task
            queue.sort()
            print(queue)
            n = queue.pop(0) 
            print("Worker should start work on ", n)
            popped.append(n)

#            for child in children[n]:
#                parents[child].discard(n)
#                if not parents[child] and child not in finished:
#                    queue.append(child)

            workers[j] = delta + ord(n) - 64

        workers = [w-1 if w > 0 else 0 for w in workers]


print("Part 1:\t", topological_sort(children, parents))
print("Part 2:\t", construct(children, parents))




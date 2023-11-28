diagram = "".join(open("input.txt").read().split())
# 173 fordi lengden er 172 + newline
def f(pos):return pos // 172, pos % 172
start = diagram.find("S")
print(start)
goal = diagram.find("E")
candidates = [i for i,a in enumerate(diagram) if a in "aS"]

def expand(pos):
    queue = []
    for dx in [1, -1, 172, -172]:
        x1 = pos+dx
        if 0<=x1<len(diagram) and diagram[x1]!="\n":
            if x1==goal and diagram[pos] in "yz":
                queue.append(x1)
            elif x1 == goal:
                continue
            elif ord(diagram[x1]) <= ord(diagram[pos]) + 1:
                queue.append(x1)
            elif x1==start and diagram[x1] in "ab":
                queue.append(x1)
    return queue

def heuristic(x):
    return ord("z") - ord(diagram[x])

from heapq import heappush
from heapq import heappop

def astar(starts):
    queue = []
    cost = dict()

    for start in starts:
        heappush(queue, (0, start))
        cost[start] = 0

    while queue:
        __, pos = heappop(queue)

        if pos == goal:
            return cost[pos]
        
        for n in expand(pos):
            if n not in cost or cost[pos] + 1 < cost[n]:
                cost[n] = cost[pos]+1
                priority = cost[pos]+1 + heuristic(n)
                heappush(queue, (priority, n))

print("Part 1:\t", astar([start]))
print("Part 2:\t", astar(candidates))

""" Advent of Code 2022. Day 16: Proboscidea Volcanium """

sample = """\
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""

#with open("input.txt") as f:
    #sample = f.read() 

import re

flowrates = [int(n) for n in re.findall(r"\d+", sample)]

valves = {}
rates = {}
for rate, line in zip(flowrates, sample.splitlines()):
    valve, *neighbours = re.findall(r"[A-Z]{2}", line)
    valves[valve] = neighbours
    rates[valve] = rate

print(valves)
print(rates)
vertices = {v for v in valves if rates[v] > 0}
print(len(vertices), len(rates))

def write_dot(valves):
    with open("dot.txt", "w") as f:
        msg = ""
        for v in valves:
            msg += f"{v} -- {{"
            for n in valves[v]:
                msg += f"{n} "
            msg += "};\n"
            if rates[v] == 0:
                msg += f"{v}[style=filled]\n"
        f.write(msg)

# The graph can be simplified.
# Let's create a proper adjacency matrix with costs in moving between
# valves with rate > 0
#def bfs(start):
#    seen = {start}
#    queue = [(start, 0)]
#
#    costs = {}
#
#    while queue:
#        node, dist = queue.pop(0)
#
#        for v in valves[node]:
#            if v not in seen:
#                queue.append((v, dist+1))
#                seen.add(v)
#
#                if rates[v] > 0:
#                    costs[v] = dist+1
#    return costs
#
#dists = {v: bfs(v) for v in vertices}
#print(dists)

from heapq import heappush
from heapq import heappop

# Let's start with simple bfs
# What determines the states?
# (current, t, opened)

to_open = {v for v in valves if rates[v] > 0}
potentials = {v for v in valves if rates[v] > 0}
opened = set()

init_state = (0, 0, "AA", tuple(sorted(to_open))) 
queue = []
queue.append(init_state)

visited = set()
visited.add((0, 0, "AA", tuple(sorted(to_open))))
#visited = {}
#visited[(0, "AA", len(to_open))] = 0
#seen = set()
#seen.add("AA")

max_round = sum(rates.values())

maxes = 0
new_states = {(0, "AA", tuple(sorted(to_open)))}
visited = new_states
for t in range(30):
    print(f" == Minute {t+1} == ")
    print(len(new_states))
    if t > 5:
        states = sorted(new_states, key=lambda x: -x[0])[:20000]
        states = set(states)
    else:
        states = new_states.copy()
    new_states = set()
    for pressure, current, to_open in states:
        round_pressure = sum(rates[v] for v in potentials if v not in to_open) 
        new_pressure = pressure + round_pressure
        remains = (30 - t) * round_pressure

        max_possible = pressure + (30-t)*max_round
        print(pressure, max_possible, len(to_open))

        if (pressure + (30-t)*max_round) < maxes:
            continue

        if len(to_open) == 0:
            print(t, round_pressure)
            print(maxes, new_pressure, remains, pressure+remains)
            maxes = max(maxes, pressure+remains) 
            print(maxes)
            input()
            continue
    
        # If opening current valve
        if current in to_open and rates[current] > 0:
            new_open = set(to_open).copy()
            new_open.remove(current)
            temp = (new_pressure, current)
            new_state = temp + (tuple(sorted(new_open)),)
            if new_state not in visited:
                new_states.add(new_state)
                visited.add(new_state)

        # If moving to new valve
        for neighbour in valves[current]:
            new_state = (new_pressure, neighbour, tuple(sorted(to_open)))
            if new_state not in visited:
                new_states.add(new_state)
                visited.add(new_state)

    # Prune
    #if t > 15:
        #queue = sorted(queue, key=lambda x: -x[1])[:2000]
print(maxes) #=1000
print(max(new_states))
exit()

# Want to reduce problem
# The 0 rate valves (except root) can be merged
# But then the cost should be +1 for moving
#print(len(valves))
#for v, rate in rates.items():
#    if rate == 0 and v != "AA":
#        left, right = valves[v]
#        valves[left].remove(v)
#        valves[left].append(right)
#        valves[right].remove(v)
#        valves[right].append(left)
#        del valves[v]
#
#print(len(valves))
#input()

#def expand(x, y):
#    queue = []
#    for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
#        x1, y1 = x+dx, y+dy
#
#        if 0<=x1<len(diagram) and 0<=y1<len(diagram[0]):
#            if (x1, y1) == goal and diagram[x][y] in "yz":
#                queue.append((x1,y1))
#            elif (x1, y1) == goal and diagram[x][y] != "z":
#                continue
#            elif ord(diagram[x1][y1]) <= ord(diagram[x][y]) + 1:
#                # Can move here
#                queue.append((x1,y1))
#            elif diagram[x][y] == "S" and diagram[x1][y1] == "a":
#                # Can move here
#                queue.append((x1, y1))
#    return queue

def heuristic(x, y, goal):
    return abs(goal[0]-x) + abs(goal[1]-y)

from heapq import heappush
from heapq import heappop

def astar(start):
    queue = []
    cost = dict()

    heappush(queue, (0, 0, start, 0, set()))
    cost[(start, 0, ())] = 0

    potentials = {valve for valve, rate in rates.items() if rate > 0}
    print(potentials)
    length = len(potentials) 

    all_pressure = sum(rates.values())

    maxes = 0
    while queue:
        *__, pos, t, openv = heappop(queue)
        print(len(queue), "\t", len(cost), "\t", len(potentials), len(openv), len(rates))
        key = (pos, t, tuple(sorted(openv)))

        round_pressure = sum(rates[v] for v in openv) 
        new_pressure = cost[key] + round_pressure 
#        print(f"""\
#        == Minute {t + 1} ==
#        We are at {pos}, with tunnels to {valves[pos]}.
#        {openv} valves are open.
#        with pressure {new_pressure} released
#        """)
        #print(pos, len(openv), cost[(pos, t)], round_pressure, all_pressure)
        remains = (30 - t) * round_pressure
        #print("Potential left:\t", remains)

        if t == 30:
            continue

        if openv == potentials:
            print(openv)
            print(potentials)
            print(remains + cost[key])
            maxes = max(maxes, remains+cost[key])
            print(maxes)
            input()
            continue

        
        # Opening valve
        if rates[pos] > 0 and pos not in openv:
            cost[(pos, t+1, tuple(sorted(openv | {pos})))] = cost[key] + round_pressure
            priority = t+1 + length - len(openv) - 1 # Extra minus because opening 1 more
            heappush(queue, (priority, -round_pressure, pos, t+1, {pos} | {v for v in openv}))

        # Moving to valve
        for valve in valves[pos]:
            if (valve, t+1, tuple(sorted(openv))) not in cost or cost[key] + round_pressure > cost[(valve, t+1, tuple(sorted(openv)))]:
                cost[(valve, t+1, tuple(sorted(openv)))] = cost[key] + round_pressure
                priority = t+1 + length - len(openv)
                heappush(queue, (priority, -round_pressure, valve, t+1, {v for v in openv}))
    return maxes

start = "AA"
print("Part 1:\t", astar(start))

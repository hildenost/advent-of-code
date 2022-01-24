""" Advent of Code 2018. Day 20: A Regular Map """

from collections import defaultdict

dirs = {
    "N": lambda x, y: (x, y+1),
    "S": lambda x, y: (x, y-1),
    "E": lambda x, y: (x+1, y),
    "W": lambda x, y: (x-1, y),
}


def create_graph(regex):
    regex = list(regex[::-1])
    graph = defaultdict(list)
    last_pos = []
    pos = (0, 0)
    while regex:
        d = regex.pop()

        if d == "^":
            continue
        elif d == "$":
            break
        elif d == "(":
            last_pos.append(pos)
        elif d == ")":
            pos = last_pos.pop()
        elif d == "|":
            pos = last_pos[-1]
        else:
            new_pos = dirs[d](*pos)
            graph[pos].append(new_pos)
            pos = new_pos
    return graph

def bfs(graph, startnode):
    from heapq import heappush
    from heapq import heappop

    queue = [startnode]
    explored = set() 
    dist = {startnode: 0}
    while queue:
        pos = heappop(queue)
        if pos in explored:
            continue

        explored.add(pos)

        for child in graph[pos]:
            if child not in dist:
                dist[child] = dist[pos] + 1
                heappush(queue, child)
    return dist

with open("input.txt") as f:
    regex = f.read().strip()

graph = create_graph(regex)
distances = bfs(graph, startnode=(0, 0))

print("Part 1:\t", max(distances.values()))
print("Part 2:\t", sum(v >= 1000 for v in distances.values()))


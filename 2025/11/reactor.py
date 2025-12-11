""" Advent of Code 2025. Day 11: Reactor """

with open("input.txt") as f:
    lines = f.read().splitlines()


graph = {}
for line in lines:
    node, children = line.split(":")
    children = children.split()
    graph[node] = children


start = "you"
stack = [start]
paths = 0
while stack:
    node = stack.pop()

    if node == "out":
        paths += 1
        continue

    stack.extend(graph[node])

print("Part 1: \t", paths)

start = "svr"
stack = [(start, (start,))]
visited = set()
paths = 0
while stack:
    print(len(stack))
    node, path = stack.pop()
    #print(node, path)

    visited.add(path)

    if node == "out":
        print(path)


        if "dac" in path and "fft" in path:
            paths += 1

        #input()
        continue

    for child in graph[node]:
        #print(path, (child, ))
        #print(path + (child, ))
        new_path = path + (child, )
        if new_path in visited:
            print("BEEN")
            input()
            continue
        stack.append((child, new_path))

print("Part 2: \t", paths)


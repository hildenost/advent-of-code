from input_prog import input_program
from intcode import run


moves = {
    1: lambda x, y: (x, y - 1),
    2: lambda x, y: (x, y + 1),
    3: lambda x, y: (x - 1, y),
    4: lambda x, y: (x + 1, y)
}

dirs = {
    1: "north",
    2: "south",
    3: "west",
    4: "east"
}

opposites = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

def move_droid(repair, i):
    next(repair)
    return repair.send(i)

def dfs(repair, find_oxygen=True):
    node = (0, 0)
    seen = {node}

    hallways = {node}

    breadcrumbs = []
    status = 1
    #while status != 2:
    start = True
    while breadcrumbs or start:
        start = False
        prev = node
        for i in (1, 2, 3, 4):
            # Getting the absolute position
            node = moves[i](*prev)
            if node not in seen:
                # Adding the position to our seen set
                seen.add(node)
                # Then we move the droid
                status = move_droid(repair, i)

                # If status is 0, do nothing
                if status == 0:
                    continue

                # Else, we add the move to our breadcrumps
                # and break the for loop to move on
                hallways.add(node)
                breadcrumbs.append(i)

                if status == 2 and find_oxygen:
                    return len(breadcrumbs), node

                break
        # If for loop didn't break, we end up in the
        # else-statement
        else:
            # All neighbours seen and no way ahead
            # Backtracking one step
            # First picking up our breadcrumb
            i = breadcrumbs.pop()
            node = moves[opposites[i]](*prev)
            # Then moving the droid in the opposite
            # direction
            move_droid(repair, opposites[i])

    return hallways

def bfs(explore, hallways, start):
    depths = {start: 0}
    seen = {start}
    queue = [start]
    while queue:
        parent = queue.pop(0)

        children = [
            moves[i](*parent) for i in (1, 2, 3, 4)
            if moves[i](*parent) in hallways
            and moves[i](*parent) not in seen
        ]
        seen.update(children)
        depths.update(
            {child: depths[parent] + 1 for child in children}
        )
        queue.extend(children)
    return max(depths.values())


### PART 1
repair = run(input_program + [0]*100)
answer, start_node = dfs(repair)
print(answer)

### PART 2
explore = run(input_program + [0]*100)
hallways = dfs(explore, find_oxygen=False)
oxygen_spread = run(input_program + [0]*100)
print(bfs(oxygen_spread, hallways, start_node))


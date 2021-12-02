# route = ">"
# route = "^>v<"
# route = "^v^v^v^v^v"

with open("03/input.txt") as f:
    route = f.read()


def traverse(moves):
    curr_pos = (0, 0)
    houses = {curr_pos}
    for stop in moves:
        if stop == ">":
            curr_pos = (curr_pos[0] + 1, curr_pos[1])
        elif stop == "^":
            curr_pos = (curr_pos[0], curr_pos[1] - 1)
        elif stop == "<":
            curr_pos = (curr_pos[0] - 1, curr_pos[1])
        elif stop == "v":
            curr_pos = (curr_pos[0], curr_pos[1] + 1)
        houses.add(curr_pos)
    return houses


### PART 1
print(len(traverse(route)))

### PART 2
santa_route = route[::2]
robo_route = route[1::2]

print(len(traverse(santa_route) | traverse(robo_route)))

""" Advent of Code 2023. Day 21: Step Counter """


with open("input.txt") as f:
    tiles = f.read().splitlines()

rocks = set()
for i, line in enumerate(tiles):
    for j, cell in enumerate(line):
        if cell == "#":
            rocks.add((i, j))
        elif cell == "S":
            start = (i, j)


width = len(tiles)


def bfs(steps, store=None):
    queue = {start}
    prev = dict()
    for t in range(steps):
        queue = {
            (i + di, j + dj)
            for i, j in queue
            for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]
            if ((i + di) % width, (j + dj) % width) not in rocks
        }

        if store is not None and (t + 1) % width == store:
            prev[t + 1] = len(queue)
    return len(queue) if store is None else prev


print("Part 1:\t", bfs(steps=64))

STEPS = 26501365

# PART 2
# Since the map is repeating itself, it may be that also the extra number of tiles
# reached fall into a predictable pattern.
# Expansion of roughly 4 times the width of the map seems enough.
# The approach will be to:
#   0.  Find the modulus of STEPS on width
modulus = STEPS % width
#   1.  Run the stupid bfs for 4 times the width,
#       storing the length of the reached tiles per timestep with the same
#       modulus as STEPS
times = bfs(steps=4 * width, store=modulus)
#   2.  Compute the differences between the number of tiles reached for the
#       stored timesteps
milestones = list(times.keys())
deltas = [times[u] - times[t] for t, u in zip(milestones, milestones[1:])]
deltadeltas = [u - t for t, u in zip(deltas, deltas[1:])]

#   3.  Compute the n remaining cycles
n = (STEPS - max(times)) // width


#   4.  The answer for the final reached number of tiles after STEPS steps,
#       is current + k * delta[current] + sum_all_numbers to k * deltadelta[current]
#       where k is the remanining number of cycles until STEPS
def extrapolate(current, delta, deltadelta, k):
    return current + k * delta + k * (k + 1) // 2 * deltadelta


print(
    "Part 2:\t",
    extrapolate(max(times.values()), deltas[-1], deltadeltas[-1], n),
)

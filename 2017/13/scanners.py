""" Advent of Code 2017. Day 13: Packet Scanners """
import re

raw_scanners = """0: 3
1: 2
4: 4
6: 4
""".splitlines()

with open("input.txt") as f:
    raw_scanners = f.read().splitlines()

scanners = {}
for line in raw_scanners:
    k, v = re.findall(r"\d+", line)
    scanners[int(k)] = int(v)

# We don't need to know each scanner's exact placement at all times
# Only the times they are at top layer
def top_layer(time):
    # The number of picoseconds between each time the
    # top layer is visited, is the even number sequence.
    #        range | 2 3 4  5  6  7 ... r
    # time between | 4 6 8 10 12 14 ... 2*(r-1)
    return {k for k, v in scanners.items() if not time % (2 * (v - 1))}


def get_severity(delay=0):
    return sum(t * r for t, r in scanners.items() if t in top_layer(t + delay))


def is_caught(delay=0):
    return any(t in top_layer(t + delay) for t in scanners)


def find_delay():
    delay = 0
    while is_caught(delay):
        delay += 1
    return delay


print("Part 1:\t", get_severity())
print("Part 2:\t", find_delay())


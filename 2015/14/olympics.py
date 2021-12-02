""" Advent of Code 2015. Day 14: Reindeer Olympics """

TOTALTIME = 2503

reindeer = """Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds."""

# reindeer = """Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds."""

import re

reindeer_stats = [
    (int(s), int(t), int(u))
    for s, t, u in re.findall(r"(\d+) .* (\d+) .* (\d+)", reindeer)
]


def travel(time, speed, speedtime, resttime):
    km_per_cycle = speed * speedtime
    cycle_time = speedtime + resttime

    full_cycles = time // cycle_time

    full_cycles_distance = full_cycles * km_per_cycle

    remaining_time = time - cycle_time * full_cycles

    remaining_distance = (
        km_per_cycle if remaining_time >= speedtime else speed * remaining_time
    )

    return full_cycles_distance + remaining_distance


part1 = max(travel(TOTALTIME, *deer) for deer in reindeer_stats)

print("Part 1: ", part1)


def turn(time, points, reindeer_stats):
    poses = [travel(time, *deer) for deer in reindeer_stats]
    farthest = max(poses)
    return [x if pos != farthest else x + 1 for x, pos in zip(points, poses)]


reindeer_points = [0] * len(reindeer_stats)
for t in range(1, TOTALTIME + 1):
    reindeer_points = turn(t, reindeer_points, reindeer_stats)
print("Part 2: ", max(reindeer_points))


""" Advent of Code 2018. Day 4: Repose Record """
import re
from datetime import datetime

with open("input.txt") as f:
    raw_log = f.read().splitlines()

pattern = re.compile(
    r"\[\d+-(\d+)-(\d+) (\d+):(\d+)\].+?(wakes up|falls asleep|\d+)")


log = []
for l in raw_log:
    *times, mode = re.match(pattern, l).groups()
    times = tuple(int(t) for t in times)
    log.append((*times, mode))

from collections import defaultdict
from collections import Counter
guards = defaultdict(list)
for *__, minute, mode in sorted(log):
    if mode.isdigit():
        on_duty = mode
    elif mode == "falls asleep":
        start_min = minute
    elif mode == "wakes up":
        minutes_asleep = list(range(start_min, minute + 1))
        guards[on_duty].extend(minutes_asleep)

most_asleep, minutes = max(guards.items(), key=lambda x: len(x[1]))
print("Part 1:\t", int(most_asleep) * Counter(minutes).most_common(1)[0][0])

counters = {
    # most_common() returns tuples of (value, freq)
    # I want the reverse order to use pythons tuple ordering
    Counter(m).most_common(1)[0][::-1]: guard
    for guard, m in guards.items()}
print("Part 2:\t", int(counters[max(counters)]) * (max(counters)[1] - 1))

""" Day 4: Repose Record Part 1.

Finding the minute between 0.00 and 1.00 when a guard
is most likely to be asleep.

"""
from collections import defaultdict
from datetime import datetime

from operator import itemgetter
import re

def clean_record(record):
    """Takes one line of input and splits into a date and a message."""
    # Splitting record by nonword-characters, but only the first
    # 6 splits to avoid splitting the message
    splitted = re.split(r"\W", record, 6)

    # Then the date parts are turned into integers.
    dateparts = [int(splitted[d]) for d in range(1, 6)]
    date = datetime(*dateparts)

    return date, splitted[-1].strip()

def sort_records(records):
    """Returns chronologically sorted records."""
    return sorted([clean_record(record) for record in records], key=itemgetter(0))

def find_guard_id(msg):
    """ Return the guard which is on shift. """
    return re.search(r"\d+", msg).group(0)

def process_message(msg, guard_id):
    """ Return True if asleep, False if awake, and new guard id if shift."""
    if msg == "falls asleep":
        return guard_id, True
    if msg == "wakes up":
        return guard_id, False

    return find_guard_id(msg), False


# First, let's sort out the data
with open("input.txt") as f:
    chronological_records = sort_records(f.readlines())

stats = defaultdict(lambda: defaultdict(int))
guard = None
d_old_min = 0
is_old_asleep = False
for d, msg in chronological_records:
    guard, is_asleep = process_message(msg, guard)
    stats[guard][d.minute] += is_asleep

[print(c) for c in chronological_records]
for guard, mins in stats.items():
    print()
    print(guard, ":\n\t", mins)

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

def interpret_records(records):
    """ Interpret the chronologically sorted records.

    Return a statistics dictionary.

    """

    stats = defaultdict(lambda: defaultdict(int))

    guard = None
    prev_minute = 0
    prev_asleep = False
    for date, message in records:
        guard, is_asleep = process_message(message, guard)

        for minute in range(prev_minute, date.minute):
            stats[guard][minute] += prev_asleep

        prev_minute, prev_asleep = date.minute, is_asleep

    return stats

def process_input():
    """ Clean, sort, and count the sleeping minutes by guard id.

    First, let's sort out the data. Then a count of every time
    a given guard is asleep is stored.

    stats is a nested defaultdict that holds the statistics of every
    guards' sleepy times.

    """

    with open("input.txt") as fyle:
        chronological_records = sort_records(fyle.readlines())

    return interpret_records(chronological_records)


def sleepiest_guard(stats):
    """ Finding the guard that sleeps the most minutes. """
    sleep_sum = {guard: sum(mins.values()) for guard, mins in stats.items()}
    return max(sleep_sum.keys(), key=(lambda k: sleep_sum[k]))

def sleepiest_minute(stats):
    """ Finding the minute where a given guard sleeps most often. """
    guard = stats[sleepiest_guard(stats)]
    return int(max(guard.keys(), key=(lambda k: guard[k])))

def guard_by_minute():
    """ Finding the sleepiest guard id multiplied by the minute he's most likely asleep. """
    stats = process_input()
    return int(sleepiest_guard(stats))*sleepiest_minute(stats)

if __name__ == "__main__":
    print(guard_by_minute())

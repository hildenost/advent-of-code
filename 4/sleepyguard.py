""" Day 4: Repose Record Part 1.

Finding the minute between 0.00 and 1.00 when a guard
is most likely to be asleep.

"""

from datetime import datetime

from operator import itemgetter
import re

import pandas as pd

# First, let's sort out the data
with open("input.txt") as f:
    records = f.readlines()


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

def process_message(msg):
    """ Return True if asleep, False if awake, and guard id if shift."""
    if msg == "falls asleep":
        return True
    elif msg == "wakes up":
        return False
    else:
        return find_guard_id(msg)

chronological_records = sort_records(records)

for d, msg in chronological_records:
    print(d, "\t", msg, "\t", process_message(msg))

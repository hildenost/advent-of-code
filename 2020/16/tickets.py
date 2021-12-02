import re

test = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

test = """\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""


range_pattern = re.compile(r"([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)")

with open("16/input.txt") as f:
    test = f.read()


def get_valid_ranges(defs):
    valid_ranges = dict()

    for line in defs.splitlines():
        m = range_pattern.match(line)
        field, lower1, upper1, lower2, upper2 = m.groups()

        valid_ranges[field] = set(range(int(lower1), int(upper1) + 1))
        valid_ranges[field].update(range(int(lower2), int(upper2) + 1))

    return valid_ranges


def find_invalid_values(tickets, valid_ranges):
    valid_ranges = set.union(*[v for v in valid_ranges.values()])

    invalid = []
    valid_tickets = []
    for line in tickets.splitlines()[1:]:
        ticket = []
        for n in line.split(","):
            if int(n) not in valid_ranges:
                invalid.append(int(n))
                break
        else:
            valid_tickets.append([int(n) for n in line.split(",")])

    return valid_tickets, invalid


def determine_fields(valid_tickets, valid_ranges):
    candidates = {k: set(range(len(valid_tickets[0]))) for k in valid_ranges}
    for ticket in valid_tickets:
        for i, v in enumerate(ticket):
            for field in valid_ranges:
                if v not in valid_ranges[field]:
                    candidates[field].remove(i)
    # sorting dict by length of candidate fields
    chosen = set()
    for field in dict(sorted(candidates.items(), key=lambda pair: len(pair[1]))):
        while len(candidates[field]) > 1:
            candidates[field] -= chosen
        chosen.update(candidates[field])
    candidates = {c: v.pop() for c, v in candidates.items()}
    return candidates


ranges, my_ticket, tickets = test.split("\n\n")

valid = get_valid_ranges(ranges)

valid_tickets, invalid_values = find_invalid_values(tickets, valid)
print("Part 1: ", sum(invalid_values))

fields = determine_fields(valid_tickets, valid)

my_values = [int(v) for line in my_ticket.splitlines()[1:] for v in line.split(",")]
departures = [my_values[v] for c, v in fields.items() if c.startswith("departure")]
answer = 1
for d in departures:
    answer *= d
print("Part 2: ", answer)


""" Advent of Code 2019. Day 25: Cryostasis """

from intcode import run


def to_ascii(string):
    return [ord(c) for c in string] + [10]


with open("input.txt") as f:
    program = [int(n) for n in f.read().strip().split(",")]

# From trial and error and manually navigating the ship
pickup_path = [
    "west",
    "north",
    # "take dark matter",
    "south",
    "east",
    "north",
    "west",
    # "take planetoid",
    "west",
    "take spool of cat6",
    "east",
    "east",
    "south",
    "east",
    "north",
    "take sand",
    "west",
    # "take coin",
    "north",
    "take jam",
    "south",
    "west",
    "south",
    # "take wreath",
    "west",
    "take fuel cell",
    "east",
    "north",
    "north",
    "west",
    # enter the cockpit
    "south",
]

items = [
    "dark matter",
    "planetoid",
    "spool of cat6",
    "sand",
    "coin",
    "jam",
    "wreath",
    "fuel cell",
]

####
# IF BRUTE FORCING ALL COMBOS
#
from itertools import combinations

all_combos = [set(x) for n in range(8, -1, -1) for x in combinations(items, n + 1)]


def generate_commands(all_combos, items):
    items = set(items)

    # First drop the not needed ones
    tests = []
    for combo in all_combos:
        takes = [f"take {item}" for item in combo]
        drops = [f"drop {item}" for item in items - combo]
        tests.append(takes + drops)
    return tests


tests = generate_commands(all_combos, items)
#
### BRUTE FORCE PREP DONE


def run_script(program):
    b = run(program + [0] * 1000)
    next(b)

    msg = []
    while True:
        try:
            output = next(b)

            if output is None:
                string = "".join(msg)
                print(string)

                msg = []

                if pickup_path:
                    cmd = pickup_path.pop(0)
                else:
                    cmd = input()

                for c in to_ascii(cmd):
                    b.send(c)

            elif output is not None:
                msg += chr(output)

        except StopIteration:
            break

    string = "".join(msg)
    print(string)


run_script(program)

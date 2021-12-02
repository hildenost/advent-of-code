import re
from itertools import product
from collections import defaultdict

test = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

with open("14/input.txt") as f:
    test = f.read()


def parse_program(program):
    mask_pattern = re.compile(r"mask = (?P<mask>[X10]{36})")
    mem_pattern = re.compile(r"mem\[(?P<address>\d+)\] = (?P<value>\d+)")
    parsed_program = []
    largest_address = 0
    for line in program.splitlines():
        m = mask_pattern.match(line)
        if m:
            parsed_program.append(m["mask"])
            continue
        m = mem_pattern.match(line)
        if m:
            parsed_program.append((int(m["address"]), int(m["value"])))
            largest_address = max(largest_address, int(m["address"]))
    return parsed_program


def part1(instructions):
    parsed_program = parse_program(instructions)
    memory = defaultdict(int)

    for instruction in parsed_program:
        if isinstance(instruction, str):
            mask = [
                (bit, int(val))
                for bit, val in enumerate(instruction[::-1])
                if val in "01"
            ]
            continue

        address, value = instruction

        memory[address] = update_number(value, mask)

    print(sum(memory.values()))


def change_bit(position, number, mode):
    return number | 1 << position if mode else number & ~(1 << position)


def update_number(value, instructions):
    for bit, val in instructions:
        value = change_bit(bit, value, val)
    return value


def part2(instructions):
    parsed_program = parse_program(instructions)
    memory = defaultdict(int)

    for instruction in parsed_program:
        if isinstance(instruction, str):
            bitmask_1 = [bit for bit, val in enumerate(instruction[::-1]) if val == "1"]
            bitmask_x = [bit for bit, val in enumerate(instruction[::-1]) if val == "X"]
            continue

        address, value = instruction

        for bit in bitmask_1:
            address |= 1 << bit

        floats = product([0, 1], repeat=len(bitmask_x))

        addresses = (update_number(address, zip(bitmask_x, combo)) for combo in floats)

        for address in addresses:
            memory[address] = value
    print(sum(memory.values()))


part1(test)
test2 = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""
part2(test2)
part2(test)


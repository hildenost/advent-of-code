import re
from operator import inv, and_, or_, lshift, rshift

example = """\
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
""".splitlines()

with open("07/input.txt") as f:
    example = f.read().splitlines()

functions = {
        "AND": and_,
        "OR": or_,
        "NOT": inv,
        "LSHIFT": lshift,
        "RSHIFT": rshift
        }

circuit = {}
def convert_to_int(var):
    return int(var) if var.isdigit() else var

def parse_line(line):
    instructions = line.split()
    wire = instructions.pop()
    instructions.pop()
    if len(instructions) == 1:
        a, = instructions
        circuit[wire] = convert_to_int(a) 
    elif len(instructions) == 2:
        # Can only be the bitwise complement
        op, b = instructions
        circuit[wire] = (functions[op], b)
    else:
        # Remaining are either
        # wire1 AND | OR wire 2
        # wire1 LSHIFT | RSHIFT INT
        a, op, b = instructions 
        a = convert_to_int(a)
        b = convert_to_int(b)
        circuit[wire] = (functions[op], a, b)
    

for line in example:
    parse_line(line)

def sort_out_command(func, *args):
    if isinstance(func, int):
        return func
    elif isinstance(func, str):
        return sort_out_command(*circuit[func])
    elif len(args) == 2:
        a, b = args
        if func in {lshift, rshift}:
            if isinstance(circuit[a], int):
                temp = sort_out_command(circuit[a]) if not isinstance(a, int) else a
            else:
                temp = sort_out_command(*circuit[a]) if not isinstance(a, int) else a
            circuit[a] = temp
            return func(circuit[a], b)
        elif func in {and_, or_}:
            if isinstance(a, int):
                temp_a = a
            elif isinstance(circuit[a], int):
                temp_a = sort_out_command(circuit[a]) if not isinstance(a, int) else a
                circuit[a] = temp_a
            else:
                temp_a = sort_out_command(*circuit[a]) if not isinstance(a, int) else a
                circuit[a] = temp_a
            if isinstance(circuit[b], int):
                temp = sort_out_command(circuit[b]) if not isinstance(b, int) else b
            else:
                temp = sort_out_command(*circuit[b]) if not isinstance(b, int) else b
            circuit[b] = temp
            return func(temp_a, temp)

    elif len(args) == 1:
        a, = args
        circuit[a] = sort_out_command(*circuit[a])
        return int("".join("1" if x == "0" else "0" for x in f"{circuit[a]:016b}"), 2)


circuit["b"] = 46065
circuit["a"] = sort_out_command(circuit["a"])
print(circuit["a"]) # PART 1 = 46065


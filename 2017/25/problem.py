""" Advent of Code 2017. Day 25: The Halting Problem """

tape = set() 
states = {
    "A": lambda p: (1, p-1, "E") if p in tape else (1, p+1, "B"),
    "B": lambda p: (1, p+1, "F") if p in tape else (1, p+1, "C"),
    "C": lambda p: (0, p+1, "B") if p in tape else (1, p-1, "D"),
    "D": lambda p: (0, p-1, "C") if p in tape else (1, p+1, "E"),
    "E": lambda p: (0, p+1, "D") if p in tape else (1, p-1, "A"),
    "F": lambda p: (1, p+1, "C") if p in tape else (1, p+1, "A")
}

STEPS = 12459852
state = "A"
p = 0
for step in range(STEPS):
    value, new_p, state = states[state](p)
    if value:
        tape.add(p)
    else:
        tape.discard(p)

    p = new_p
print("Part 1:\t", len(tape))

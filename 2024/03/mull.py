"""Advent of Code 2024. Day 3: Mull It Over """


with open("input.txt") as f:
    memory = f.read()


def digit(memory, i):
    a = ""
    while memory[i].isdigit():
        a += memory[i]

        i += 1
    if a:
        a = int(a)
    return a, i


total = 0
i = 0
while i < len(memory):
    if memory[i : i + 3] == "mul":
        i += 3
        if memory[i] == "(":
            i += 1
            a, i = digit(memory, i)
            if memory[i] == ",":
                i += 1
                b, i = digit(memory, i)
                if memory[i] == ")":
                    total += a * b

    i += 1
print("Part 1:\t", total)

total = 0
i = 0
do = True
while i < len(memory):
    if memory[i : i + 4] == "do()":
        do = True
        i += 4
    if memory[i : i + 7] == "don't()":
        do = False
        i += 7
    if memory[i : i + 3] == "mul":
        i += 3
        if memory[i] == "(":
            i += 1
            a, i = digit(memory, i)
            if memory[i] == ",":
                i += 1
                b, i = digit(memory, i)
                if memory[i] == ")" and do:
                    total += a * b

    i += 1
print("Part 2:\t", total)

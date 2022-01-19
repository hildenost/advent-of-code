""" Advent of Code 2018. Day 14: Chocolate Charts """

NUMBER = "047801"

scoreboard = "37"
elf_1 = 0
elf_2 = 1
while len(scoreboard) < int(NUMBER) + 10:
    new = int(scoreboard[elf_1]) + int(scoreboard[elf_2])

    first, second = new // 10, new % 10
    if first > 0:
        scoreboard += str(first)
    scoreboard += str(second)

    elf_1 = (elf_1 + 1 + int(scoreboard[elf_1])) % len(scoreboard)
    elf_2 = (elf_2 + 1 + int(scoreboard[elf_2])) % len(scoreboard)

print("Part 1:\t", scoreboard[int(NUMBER) : int(NUMBER) + 10])

while True:
    new = int(scoreboard[elf_1]) + int(scoreboard[elf_2])
    first, second = new // 10, new % 10
    if first > 0:
        scoreboard += str(first)
        if scoreboard[-len(NUMBER) :] == NUMBER:
            to_the_left = len(scoreboard) - len(NUMBER)
            break

    scoreboard += str(second)
    if scoreboard[-len(NUMBER) :] == NUMBER:
        to_the_left = len(scoreboard) - len(NUMBER)
        break

    elf_1 = (elf_1 + 1 + int(scoreboard[elf_1])) % len(scoreboard)
    elf_2 = (elf_2 + 1 + int(scoreboard[elf_2])) % len(scoreboard)

print("Part 2:\t", to_the_left)


""" Advent of Code 2025. Day 1: Secret Entrance """


with open("input.txt") as f:
    rotations = f.read().splitlines()
    # convert to negative/positive steps
    rotations = [+int(r[1:]) if r[0] == "R" else -int(r[1:]) for r in rotations]



def find_password1(rotations):
    dial = 50

    password = 0

    for r in rotations:
        dial += r
        dial %= 100

        if dial == 0:
            password += 1
    return password

print("Part 1:\t", find_password1(rotations))

def find_password2(rotations):
    dial = 50
    password = 0

    for r in rotations:
        while abs(r) > 100:
            password += 1

            if r > 0:
                r -= 100
            else:
                r += 100

        prev_dial = dial
        dial += r
        dialmod = dial % 100

        if dialmod == 0:
            password += 1
        elif dialmod != dial and prev_dial != 0:
            password += 1
        dial = dialmod
    return password

print("Part 2:\t", find_password2(rotations))

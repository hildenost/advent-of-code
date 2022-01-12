""" Advent of Code 2017. Day 9: Stream Processing """


def parse(stream):
    level = 0
    group_score = 0
    garbage_size = 0

    i = 0
    is_garbage = False
    while i < len(stream):

        if stream[i] == "!":
            # Skip next char
            i += 1
        elif stream[i] == "<" and not is_garbage:
            is_garbage = True
        elif stream[i] == ">":
            is_garbage = False
        elif stream[i] == "{" and not is_garbage:
            level += 1
            group_score += level
        elif stream[i] == "}" and not is_garbage:
            level -= 1
        elif is_garbage:
            garbage_size += 1

        i += 1
    return group_score, garbage_size


with open("input.txt") as f:
    stream = f.read()

score, garbage = parse(stream)
print("Part 1:\t", score)
print("Part 2:\t", garbage)

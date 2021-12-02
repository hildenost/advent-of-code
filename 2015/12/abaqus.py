""" Advent of Code 2015. Day 12: JSAbaqusFramework.io """
import re

test = "[1,22,-3]"
test = '[1,{"c":{"d":"red","b":2},"d":40},3]'
# test = '{"d":"red","e":[1,2,3,4],"f":5}'
# test = '[1,"red",5]'

# PART 2: Ignore any object (not arrays) with the value "red"
with open("12/input.txt") as f:
    test = f.read()

pattern = r"(-?\d+)"
sum_of_all_numbers = sum(int(n) for n in re.findall(pattern, test))

print("Part 1: ", sum_of_all_numbers)

queue = list(test)
depth = 0
object_stack = [0]
is_red = False
while queue:
    curr = queue.pop(0)
    if curr == "{":
        depth += 1
        object_stack.append(0)
    elif curr == "}":
        if is_red:
            # Remove the accumulated sum of this object
            object_stack.pop()
            is_red = False
        else:
            object_stack[depth - 1] += object_stack.pop()
        depth -= 1

    elif curr == ":" and "".join(queue[1:4]) == "red":
        is_red = True

        # Skipping ahead, locating the closing bracket
        # of the current object
        d = 1
        for i, char in enumerate(queue):
            if char == "{":
                d += 1
            elif char == "}":
                d -= 1
            if d == 0:
                break
        queue = queue[i:]

    elif curr == "-" or curr.isdigit():
        while queue[0].isdigit():
            curr += queue.pop(0)

        object_stack[depth] += int(curr)

answer = object_stack[0]
print("Part 2: ", answer)

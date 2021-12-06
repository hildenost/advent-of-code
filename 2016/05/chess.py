""" Advent of Code 2016. Day 5: How About a Nice Game of Chess """

from hashlib import md5

door_id = "abc"

i = 0
password = ""
while len(password) < 8:
    string = f"{door_id}{i}"
    hashed = md5(string.encode()).hexdigest()

    if hashed[:5] == "0"*5:
        password += hashed[5]
    i += 1

print("Part 1:\t", password)

# PART 2
i = 0
password = [""]*8
while len("".join(password)) < 8:
    string = f"{door_id}{i}"
    a, b, c, d, e, pos, value, *_ = md5(string.encode()).hexdigest()

    if a+b+c+d+e == "0"*5 and pos in "01234567" and not password[int(pos)]:
        password[int(pos)] = value
    i += 1

print("Part 2:\t", "".join(password))

""" Advent of Code 2020 Day 2: Password Philosophy """
import re
from operator import xor


def parser(rule):
    lower, upper, char, password = re.split("-| |: ", rule)
    return int(lower), int(upper), char, password


def check_password_1(rule):
    lower, upper, char, password = parser(rule)
    return lower <= password.count(char) <= upper


def check_password_2(rule):
    lower, upper, char, password = parser(rule)
    # Using xor because the two Boolean values should not be equal according to the rules
    return xor(char == password[lower - 1], char == password[upper - 1])


def count_valid_passwords(password_list, part=2):
    check_password = check_password_1 if part == 1 else check_password_2
    return sum(check_password(password) for password in password_list)


test = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
print(count_valid_passwords(test, part=1))
print(count_valid_passwords(test, part=2))

with open("02\password_list.txt") as f:
    passwords = f.readlines()
print(count_valid_passwords(passwords, part=1))
print(count_valid_passwords(passwords, part=2))

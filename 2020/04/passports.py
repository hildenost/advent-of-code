""" Advent of Code 2020 Day 4: Passport Processing """
import re


def validate_height(height):
    valid_cm = height[-2:] == "cm" and 150 <= int(height[: len(height) - 2]) <= 193
    valid_in = height[-2:] == "in" and 59 <= int(height[: len(height) - 2]) <= 76
    return valid_cm or valid_in


REQUIRED_FIELDS = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: validate_height(x),
    "hcl": lambda x: bool(re.fullmatch(r"^#[0-9a-f]{6}$", x)),
    "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda x: bool(re.fullmatch(r"^[0-9]{9}$", x)),
}
OPTIONAL_FIELDS = {"cid"}


def passport_parser(passport):
    fieldpairs = [field.split(":") for field in passport.split()]
    return {k: v for k, v in fieldpairs}


def is_passport_valid(fieldspairs):
    if not set(REQUIRED_FIELDS.keys()) <= fieldspairs.keys():
        return False

    # For PART 1, replace the final return statement with a simple `return True`
    return all(REQUIRED_FIELDS[k](fieldspairs[k]) for k in REQUIRED_FIELDS)


test = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

passports = test.split("\n\n")

with open("04/passports.txt") as f:
    passports = f.read().split("\n\n")

number_of_valid_passports = sum(
    is_passport_valid(passport_parser(passport)) for passport in passports
)

print(number_of_valid_passports)

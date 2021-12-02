def check_vowels(string):
    return sum(string.count(vowel) for vowel in "aeiou") >= 3


def check_twice_in_a_row(string):
    return any(a == b for a, b in zip(string, string[1:]))


def check_no_forbidden_strings(string):
    return not any(forbidden in string for forbidden in {"ab", "cd", "pq", "xy"})


def check_pair(string):
    return any(string.find(string[i : i + 2], i + 2) != -1 for i in range(len(string)))


def check_twice_inbetween(string):
    return any(a == b for a, b in zip(string, string[2:]))


def check_strings(strings, requirements):
    return sum(all(check(string) for check in requirements) for string in strings)


with open("05/input.txt") as f:
    strings = f.read().splitlines()


### PART 1
requirements = [check_no_forbidden_strings, check_twice_in_a_row, check_vowels]
nice_strings = check_strings(strings, requirements)
print(nice_strings)

### PART 2
requirements = [check_pair, check_twice_inbetween]
nice_strings = check_strings(strings, requirements)
print(nice_strings)


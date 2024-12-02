""" Advent of Code 2024. Day 2: Red-Nosed Reports """

with open("input.txt") as f:
    reports = [[int(n) for n in l.split()] for l in f.read().splitlines()]

# reports = [
#    [7, 6, 4, 2, 1],
#    [1, 2, 7, 8, 9],
#    [9, 7, 6, 2, 1],
#    [1, 3, 2, 4, 5],
#    [8, 6, 4, 4, 1],
#    [1, 3, 6, 7, 9],
# ]


safe = 0
for report in reports:
    is_incr = None
    for m, n in zip(report, report[1:]):
        incr = n - m > 0
        if is_incr is None:
            is_incr = incr
        elif incr != is_incr:
            # Unsafe, abort this report
            break

        diff = abs(n - m)
        if 1 <= diff <= 3:
            continue
        else:
            # Unsafe, abort this report
            break
    # if not unsafe (no breaks)
    else:
        safe += 1

print("Part 1:\t", safe)


def is_safe(report):
    is_incr = None
    for m, n in zip(report, report[1:]):
        incr = n - m > 0
        if is_incr is None:
            is_incr = incr
        elif incr != is_incr:
            # Unsafe, abort this report
            return False

        diff = abs(n - m)
        if 1 <= diff <= 3:
            continue
        else:
            # Unsafe, abort this report
            return False
    return True


from itertools import combinations

sumsafe = 0
for report in reports:
    print(report)
    is_incr = None
    safe = True
    for m, n in zip(report, report[1:]):
        incr = n - m > 0
        if is_incr is None:
            is_incr = incr
        elif incr != is_incr:
            # Unsafe, abort this report
            # Unless it can be fixed

            safe = any(is_safe(l) for l in combinations(report, len(report) - 1))
            break

        diff = abs(n - m)
        if 1 <= diff <= 3:
            continue
        else:
            # Unsafe, abort this report
            safe = any(is_safe(l) for l in combinations(report, len(report) - 1))
            break
    sumsafe += safe

print("Part 1:\t", sumsafe)

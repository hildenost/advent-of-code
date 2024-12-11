""" Advent of Code 2024. Day 11: Plutonian Pebbles """
with open("input.txt") as f:
    pebbles = f.read().split()

memory = dict()


def blink(stone, n=1):
    if count := memory.get((stone, n), False):
        return count

    if n == 0:
        return 1

    # Get rids of leading zeros
    stone = str(int(stone))

    if stone == "0":
        res = blink("1", n - 1)
    elif len(stone) % 2:
        res = blink(str(int(stone) * 2024), n - 1)
    else:
        res = blink(stone[: len(stone) // 2], n - 1) + blink(
            stone[len(stone) // 2 :], n - 1
        )

    # Stuffing it in memory for later use
    memory[(stone, n)] = res
    return res


print("Part 1:\t", sum(blink(stone, 25) for stone in pebbles))
print("Part 2:\t", sum(blink(stone, 75) for stone in pebbles))

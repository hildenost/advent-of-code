""" Advent of Code 2020 Day 5: Binary Boarding """

with open("05/input.txt") as f:
    boarding_passes = f.read().splitlines()


def convert_to_binary(string):
    # This is the core of the puzzle: recognizing that the upper/lower half
    # partitioning is really just binary numbers

    # First, I replace all occurrences of the various letters with 0 (lower half)
    # or 1 (upper half)
    out = string.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0")

    # I then convert the binary number to integer, but of course only after
    # splitting the string to row and columns
    return int(out[:7], 2), int(out[7:], 2)


def get_seat_id(row, column):
    return row * 8 + column


all_seat_ids = {
    get_seat_id(*convert_to_binary(boarding_pass)) for boarding_pass in boarding_passes
}

### PART 1
print(max(all_seat_ids))


### PART 2
possible_seats = set(range(max(all_seat_ids) + 1))

# I did solve the final part visually, printing out all missing
# seat IDs, and the actual seat was easy to spot
print(possible_seats - all_seat_ids)

# But it can be done programmatically as well
your_seat_id = {
    seat_id
    for seat_id in possible_seats - all_seat_ids
    if seat_id + 1 in all_seat_ids and seat_id - 1 in all_seat_ids
}

print(your_seat_id)

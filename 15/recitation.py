starting_numbers = [14, 8, 16, 0, 1, 17]
end_1 = 2020
end_2 = 30000000


def get_number(n, numbers):
    spoken, last_number = {k: v + 1 for v, k in enumerate(numbers[:-1])}, numbers[-1]

    for i in range(len(numbers), n):
        # New number is difference between turns,
        # but make sure it's 0 when not seen before
        new_number = i - spoken.get(last_number, i)
        # Update the last position of number
        spoken[last_number] = i
        # And now we can utter the new number!
        last_number = new_number

    return last_number


print(f"The {end_1}th spoken number: ", get_number(end_1, starting_numbers))
print(f"The {end_2}th spoken number: ", get_number(end_2, starting_numbers))

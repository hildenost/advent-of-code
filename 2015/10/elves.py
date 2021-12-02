""" Advent of Code 2015. Day 10: Elves Look, Elves Say """

def look_and_say(digits, rounds):
  for r in range(rounds):
    i = 0
    new = ""
    while i < len(digits):
      current_digit = digits[i]
      count = 1
      while i+1 < len(digits) and current_digit == digits[i+1]:
        count += 1
        i += 1
      i += 1
      new += str(count) + str(current_digit)
    digits = new
  return new

puzzle_input = "3113322113"

rounds = 40 
result = look_and_say(puzzle_input, rounds)
print("Part 1: ", len(result))
additional_rounds = 10
result = look_and_say(result, additional_rounds)
print("Part 2: ", len(result))

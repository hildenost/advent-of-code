""" Advent of Code 2015. Day 25: Let It Snow """

# Noticed the top row increments as the triangular numbers
# 0 1 3 6 10 etc
def triangular(n):
  return n * (n + 1) // 2

def get_code_number(row, col):
  return triangular(col) + sum(col + r for r in range(row-1))

# Test cases
assert 19 == get_code_number(3, 4)
assert 23 == get_code_number(6, 2)
assert 8 == get_code_number(3, 2)
assert 18 == get_code_number(4, 3)

number = get_code_number(row=2947, col=3029)

def generate_code(start):
  return start * 252533 % 33554393


code = 20151125
for i in range(number - 1):
  code = generate_code(code)

print("Part 1:\t", code)



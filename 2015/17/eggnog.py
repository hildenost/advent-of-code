""" Advent of Code 2015. Day 17: No Such Thing as Too Much """

containers = [20, 15, 10, 5, 5]
to_store = 25

containers = sorted([
  33,
  14,
  18,
  20,
  45,
  35,
  16,
  35,
  1,
  13,
  18,
  13,
  50,
  44,
  48,
  6,
  24,
  41,
  30,
  42,
], reverse=True)

to_store = 150


# Store the depths here
constant = []

def trace_depths(leftovers, remains, depth=0):
  if not leftovers:
    return 0

  next_bin = leftovers.pop(0)
  new_remains = remains - next_bin

  if new_remains == 0:
    # Adding this particular depth to the tracing
    constant.append(depth)
    return 1 + trace_depths(leftovers, remains, depth)

  if sum(leftovers) < new_remains:
    return 0

  if new_remains < 0:
    return 0


  new_leftovers = [c for c in leftovers if c <= new_remains]
  return trace_depths(leftovers, remains, depth) + trace_depths(new_leftovers, new_remains, depth+1)
  

combos = trace_depths(containers, to_store)
print("Part 1:\t", combos)

from collections import Counter
answer = Counter(constant)
print("Part 2:\t", answer[min(answer)])


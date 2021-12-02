""" Advent of Code 2015. Day 15: Science for Hungry People """

from collections import namedtuple
import re

ingredients = """Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1"""

Ingredient = namedtuple("Ingredient", "cap dur fla tex cal")

all_ingredients = [
    Ingredient(*(int(x) for x in re.findall(r"(-?\d+)", line)))
    for line in ingredients.splitlines()
]


def score(recipe):
    score = [0] * 4
    for i, ingredient in enumerate(all_ingredients):
        score[0] += recipe[i] * ingredient[0]
        score[1] += recipe[i] * ingredient[1]
        score[2] += recipe[i] * ingredient[2]
        score[3] += recipe[i] * ingredient[3]

    # Convert to zero score if negative
    score = [s if s > 0 else 0 for s in score]
    return score[0] * score[1] * score[2] * score[3]


def calories(recipe):
    return sum(recipe[i] * ing.cal for i, ing in enumerate(all_ingredients))


# generate all possible combinations of teaspoons
combos = [
    [cap, dur, fla, 100 - fla - dur - cap]
    for cap in range(101)
    for dur in range(101 - cap)
    for fla in range(101 - dur)
]


def find_highest(part=1):
    return (
        max(score(w) for w in combos)
        if part == 1
        # Filtering all 500 calories solutions
        else max(score(w) for w in combos if calories(w) == 500)
    )


print("PART 1:\t", find_highest())
print("PART 2:\t", find_highest(part=2))

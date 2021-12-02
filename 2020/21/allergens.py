import re
from collections import defaultdict

test = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

with open("21/input.txt") as f:
    test = f.read()

allergens = defaultdict(list)
ingredient_list = []

for line in test.splitlines():
    word_type = "ingredient"
    food = set()
    for word in line.split():
        if word == "(contains":
            word_type = "allergen"

        elif word_type == "allergen":
            allergens[word.strip(" ,)")].append(set(food))
        else:
            food.add(word)
    ingredient_list.extend(food)


allergens = {
    allergen: set.intersection(*foods) for allergen, foods in allergens.items()
}

cannot_contain_allergen = set(ingredient_list) - set.union(*allergens.values())

total = sum(ingredient_list.count(allergen) for allergen in cannot_contain_allergen)
print("Part 1:\t", total)

decided = {}
while allergens:
    # Get the allergen with only 1 possible ingredient
    # (I know it's only 1, but what if there were several)
    test = {key: min(value) for key, value in allergens.items() if len(value) == 1}
    decided.update(test)

    # Remove the decided ingredients from the other allergens
    # and remove the decided allergens as well
    allergens = {
        k: ingrs - set(test.values()) for k, ingrs in allergens.items() if k not in test
    }

canonical_dangerous_ingredient_list = ",".join(v for k, v in sorted(decided.items()))
print("Part 2:\t", canonical_dangerous_ingredient_list)

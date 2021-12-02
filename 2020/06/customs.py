""" Advent of Code 2020 Day 6: Custom Customs """
with open("06/forms.txt") as f:
    groups = f.read().split("\n\n")

# The test input
# groups = ["abc", "a\nb\nc", "ab\nac", "a\na\na\na", "b"]

### PART 1
# Reducing all groups to a set and take the length of that set, provides the answer
counts = sum(len(set(answers.replace("\n", ""))) for answers in groups)
print(counts)

### PART 2
# Here we need info about the group length (number of members of group)
# and which letter are represented
groups = [group.split("\n") for group in groups]
# This ginormous list comprehension checks whether the number of
# times that particular letter was found in the group equals
# the number of group members, and sums it all up
print(
    sum(
        sum("".join(group).count(l) == len(group) for l in set("".join(group)))
        for group in groups
    )
)

""" Advent of Code Day 2: I Was Told There Would Be No Math """


def surface_area(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * h * l


### PART 1
def paper_required(l, w, h):
    return surface_area(l, w, h) + min(l * w, w * h, h * l)


### PART 2
def ribbon_required(l, w, h):
    return l * w * h + 2 * min(l + w, l + h, h + w)


with open("02/input.txt") as f:
    all_presents = [[int(d) for d in dims.split("x")] for dims in f.read().splitlines()]

# Just summing all paper requirements per present
for func in {paper_required, ribbon_required}:
    print(sum(func(*dims) for dims in all_presents))


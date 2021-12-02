""" Solution to Day 1: The Tyranny of the Rocket Equation.

Part 2 is solved by recursion.
"""
def fuel_required(mass):
    return mass // 3 - 2

def fuels_fuel(mass):
    fuel = fuel_required(mass)
    if fuel <= 0:
        return 0
    return fuel + fuels_fuel(fuel)


### TESTS
assert 2 == fuel_required(12)
assert 2 == fuel_required(14)
assert 654 == fuel_required(1969)
assert 33583 == fuel_required(100756)

assert 2 == fuels_fuel(14)
assert 966 == fuels_fuel(1969)
assert 50346 == fuels_fuel(100756)

### Read input
with open("input.txt", "r") as f:
    modules = f.readlines()

### PART 1
fuel_requirements = sum([fuel_required(int(mass.strip())) for mass in modules])
print(f"PART 1 solution: {fuel_requirements}")

### PART 2
total_fuel_requirements = sum([fuels_fuel(int(mass.strip())) for mass in modules])
print(f"PART 2 solution: {total_fuel_requirements}")

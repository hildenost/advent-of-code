""" Advent of Code 2023. Day 20: Pulse Propagation """

with open("input.txt") as f:
    modules = f.read().splitlines()

HIGH = "high"
LOW = "low"
ON = 1
OFF = 0


from collections import defaultdict

destinations = defaultdict(list)
inputs = defaultdict(list)
flipflops = set()
conjunctions = set()

# Let's parse
for module in modules:
    name, __, *dests = module.split()
    if name == "broadcaster":
        moduletype = "broadcaster"
    elif name.startswith("%"):
        moduletype = "flipflop"
        name = name[1:]
        flipflops.add(name)
    elif name.startswith("&"):
        moduletype = "conjunction"
        name = name[1:]
        conjunctions.add(name)

    for dest in dests:
        destinations[name].append(dest.strip(","))
        inputs[dest.strip(",")].append(name)


def pushbutton(n, monitored):
    start = "broadcaster"
    queue = [(start, LOW, "button")]

    counts = {LOW: 0, HIGH: 0}

    factors = dict()

    while queue:
        module, pulse, origin = queue.pop(0)

        counts[pulse] += 1

        if module == "broadcaster":
            outpulse = pulse
        elif module in flipflops:
            if pulse == HIGH:
                continue

            if states[module] == ON:
                outpulse = LOW
                states[module] = OFF
            else:
                outpulse = HIGH
                states[module] = ON

        elif module in conjunctions:
            pulses[origin] = pulse

            if all(pulses[p] == HIGH for p in inputs[module]):
                outpulse = LOW
            else:
                outpulse = HIGH

        for destination in destinations[module]:
            queue.append((destination, outpulse, module))

        if module in monitored and outpulse == HIGH:
            # Store the nth time the button has been pressed and that
            # this monitored module emitted a HIGH pulse
            factors[module] = n
    return counts, factors


# Note for Part 2:
# Some manual inspection is required
# rx depends on a conjunction module that depends on 4 other conjunction modules (in my input)
# So, for the closest conjunction module to emit a LOW pulse, all the 4 input modules need to be HIGH
# Let's check how often those modules are HIGH

parent = inputs["rx"][0]
grandparents = inputs[parent]

pulses = defaultdict(lambda: LOW)
states = defaultdict(lambda: OFF)
total = {LOW: 0, HIGH: 0}
total_factors = dict()
i = 0
while True:
    i += 1
    c, factors = pushbutton(i, grandparents)
    total_factors.update(factors)

    if set(grandparents) == total_factors.keys():
        # We've found all the values we need
        # Let's quit and do the math
        break

    if i <= 1000:
        total[LOW] += c[LOW]
        total[HIGH] += c[HIGH]

print("Part 1:\t", total[LOW] * total[HIGH])

from math import lcm

print("Part 2:\t", lcm(*total_factors.values()))

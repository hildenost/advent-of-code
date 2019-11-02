def parse_input(filepath):
    with open(filepath) as f:
        initial_state = f.readline().split(":")[1].strip()
        f.readline()
        rules = dict([line.strip().split(" => ") for line in f])
    return initial_state, rules

def pprint(plants):
    sorted_plants = sorted(plants)
    print(''.join(plants[p] for p in sorted_plants))

def grow_one_generation(plants, rules):
    order = []
    for p in plants:
        if p - 1 not in plants:
            pots = ['..'] + [plants[i] for i in [p, p+1, p+2]]
            order.append([p-1, '.'])
        elif p - 2 not in plants:
            pots = ['.'] + [plants[i] for i in [p-1, p, p+1, p+2]]
            order.append([p-2, '.'])
        elif p + 1 not in plants:
            pots = [plants[i] for i in [p-2, p-1, p]] + ['..']
            order.append([p+1, '.'])
        elif p + 2 not in plants:
            pots = [plants[i] for i in [p-2, p-1, p, p+1]] + ['.']
            order.append([p+2, '.'])
        else:
            pots = [plants[i] for i in [p-2, p-1, p, p+1, p+2]]
        arrangement = ''.join(pots)
        if arrangement in rules:
            order.append([p, rules[arrangement]])
        else:
            order.append([p, '.'])
    for p, rule in order:
        plants[p] = rule
    return plants

def run_simulation(initial_state, rules, time):
    plants = dict(zip(range(len(initial_state)), initial_state))

    for time in range(20):
        plants = grow_one_generation(plants, rules)

    keys = [k for k in plants if plants[k] == '#']
    return sum(keys)

initial_state, rules = parse_input('input.txt')

result = run_simulation(initial_state, rules, time=20)
print(result)

######
# 2nd half
#####
# After running a trial simulation with time = 200, I noticed
# a linear pattern in the key sums.
# They increased by 86 from time 133 and onwards.
# The sum then was 11873.

time_first = 133
first_convergence = 11873
delta_t = 50000000000 - time_first - 1
assumed_sum = first_convergence + 86*delta_t

print(assumed_sum)

from collections import deque
import re
test = """\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""
with open("input.txt") as f:
    test = f.read()

raw_rules, message = test.split("\n\n")

def parse_rules(rules):
    rule_dict = {}
    endpoints = []
    for line in rules.splitlines():
        k, v = line.split(":")
        k = int(k)
        v = v.split("|")
        if len(v) == 2:
            v = {tuple(int(r) for r in d.split()) for d in v}
        else:
            temp = v[0].split()
            if len(temp) == 1:
                v = temp[0].strip('"')
                if v.isdigit():
                    v = int(v)
                else:
                    endpoints.append(k)
            else:
                v = tuple(int(t) for t in temp)
        rule_dict[k] = v
    return rule_dict, endpoints

rules, endpoints = parse_rules(raw_rules)
MAX_DEPTH = max(len(line) for line in message.splitlines())
#By trial and error, this works
MAX_DEPTH /= 2

def unnest_with_regex(nodes, depth=0):
    if depth > MAX_DEPTH:
        return ""
    if isinstance(nodes, int):
        return unnest_with_regex(rules[nodes], depth+1)
    elif isinstance(nodes, set):
        a, b = nodes 
        return "(" + unnest_with_regex(a, depth+1) + "|" + unnest_with_regex(b, depth+1) + ")"
    elif isinstance(nodes, tuple):
        return "".join(rules[a] if a in endpoints else unnest_with_regex(a, depth+1) for a in nodes)


pattern = r"^" + unnest_with_regex(rules[0]) + r"$"
print("Part 1: ", sum(re.match(pattern, s) is not None for s in message.splitlines()))

rules[8] = {42, (42, 8)}
rules[11] = {(42, 31), (42, 11, 31)}
pattern = r"^" + unnest_with_regex(rules[0]) + r"$"
print("Part 2: ", sum(re.match(pattern, s) is not None for s in message.splitlines()))

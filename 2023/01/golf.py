f = open("a").read()
for i, t in enumerate("one two three four five six seven eight nine".split(), 1):
    f = f.replace(t, t + str(i) + t)
for m in (open("a"), f.splitlines()):
    print(sum(int(d[0] + d[-1]) for d in ([c for c in j if c.isdigit()] for j in m)))

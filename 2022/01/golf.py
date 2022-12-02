a=sorted(sum(map(int,e.split())) for e in open("a").read().split("\n\n"))
print(a[-1],sum(a[-3:]))

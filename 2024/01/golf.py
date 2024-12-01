import re
s=sorted
i=int
l=re.findall("\d+",open("a").read())
f=l[::2]
g=l[1::2]
print(sum(abs(i(a)-i(b))for a,b in zip(s(f),s(g))),sum(i(n)*g.count(n)for n in f))

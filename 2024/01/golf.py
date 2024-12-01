s=sorted
l=[int(n)for n in open("a").read().split()]
f=s(l[::2])
g=s(l[1::2])
print(sum(abs(a-b)for a,b in zip(f,g)),sum(n*g.count(n)for n in f))

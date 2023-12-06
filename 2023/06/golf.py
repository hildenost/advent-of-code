t,r=[l.split()[1:]for l in open("a")]
s=lambda z,v:sum((int(z)-x)*x>int(v)for x in range(int(z)))
w=1
for u,v in zip(t,r):w*=s(u,v)
print(w,s("".join(t),"".join(r)))

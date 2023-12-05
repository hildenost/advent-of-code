z=min
s,*i=open("a").read().split("\n\n")
i=[sorted([[int(n)for n in l.split()]for l in m.splitlines()[1:]],key=lambda x:x[1])for m in i]
l=m=[int(a)for a in s.split()[1:]]
def f(v,n,d,s,o):
 l=max(v,s)
 r=z(v+n,s+o)
 return(0,0)if r<l else(d+(l-s),r-l)
for x in i:l=[n if n else v for v,n in[(v,sum(f(v,0,*line)[0]for line in x))for v in l]]
y=[]
for s in zip(m[::2],m[1::2]):
 r={s}
 for x in i:
  t=[]
  for v,n in r:
   u={f(v,n,*i)for i in x}-{(0,0)}
   w=sum(b for _,b in u)
   if w<n:u|={(v,n-w)}
   t+=u
  r=t
 y+=[z(r)[0]]
print(z(l),z(y))

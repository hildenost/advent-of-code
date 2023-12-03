import re
f=open("a").readlines()
w=len(f[0])
a=(-1,1,-w,w,-w-1,-w+1,w-1,w+1)
f="".join(f)
p=lambda n:{i for i,s in enumerate(f)if s in n}
r=p("=-&$+/@*%#")
print(sum(int(m[0])for m in re.finditer("\d+",f)if any(k+b in r for k in range(*m.span())for b in a)))
q={k:int(m[0])for m in re.finditer("\d+",f)for k in range(*m.span())}
def c(i):
 n={q[i+b]for b in a if i+b in q}
 x,y=n if len(n)==2 else(0,0)
 return x*y
print(sum(c(j)for j in p("*")))

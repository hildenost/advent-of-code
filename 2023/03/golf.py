import re
f=open("a").readlines()
w=len(f[0])
a=(-1,1,-w,w,-w-1,-w+1,w-1,w+1)
f="".join(f)
def p(n):return{i for i,s in enumerate(f)if s in n}
parts={k:int(m[1])for m in re.finditer(r"(\d+)",f)for k in range(*m.span())}
r=p("=-&$+/@*%#")
print(sum(int(m[1])for m in re.finditer(r"(\d+)",f)if any(k+b in r for k in range(*m.span())for b in a)))
def c(i):
 n={parts[i+b] for b in a if i+b in parts}
 x,y=n if len(n)==2 else(0,0)
 return x*y
print(sum(c(j)for j in p("*")))

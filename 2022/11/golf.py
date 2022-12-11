import re
a=re.findall
q=int
s=open("a").read()
o=[(lambda x:x*x)if f=="o"else(lambda b:lambda x:x+b)(q(f))if o=="+"else(lambda b:lambda x:x*b)(q(f))for o,f in a("([+*]) (o|\d+)",s)]
s=s.split("\n")
m=[[q(n)for n in a("\d+",m)]for m in s[1::7]]
f=1
for v in s[3::7]:f*=q(v.split()[-1])
t=[(lambda d,a,b:lambda x:b if x%d else a)(*[q(l.split()[-1])for l in s[i:i+3]])for i in range(3,len(s),7)]
def p(m,s=20,f=0): 
 c=[0]*len(m)
 for r in range(s):
  for l,i in enumerate(m):
   c[l]+=len(i)
   while i:x=i.pop();w=o[l](x)%f if f else o[l](x)//3;m[t[l](w)]+=[w]
 f,s=sorted(c)[-2:]
 print(f*s)
p([r.copy()for r in m])
p(m,10000,f)

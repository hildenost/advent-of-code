c,m=open("a").read().split("\n\n")
def w(r=1):
 s=[[l[i] for l in c.split("\n")[:-1]if l[i]!=" "]for i in range(1,34,4)]
 for n,f,t in (map(int,d.split()[1:6:2])for d in m.split("\n")):
  l,s[f-1]=s[f-1][:n],s[f-1][n:]
  s[t-1]=[l,l[::-1]][r]+s[t-1]
 return "".join(a[0]for a in s)
print(w(),w(r=0))

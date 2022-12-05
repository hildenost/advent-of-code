import re
c,m=open("a").read().split("\n\n")
c,p=c.splitlines(),range(1,34,4)
def w(r=1):
    s = [[l[i] for l in c[:-1] if l[i]!= " "] for i in p]
    for n,f,t in (map(int, re.findall(r"move (\d+) from (\d) to (\d)", d)[0]) for d in m.splitlines()):
        l,s[f-1]=s[f-1][:n],s[f-1][n:]
        s[t-1]=[l,l[::-1]][r]+s[t-1]
    return "".join(a[0]for a in s)
print(w(), w(r=0))

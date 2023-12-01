import re
l=open("a").read()
n=["_","one","two","three","four","five","six","seven","eight","nine"]
print([sum(int(g[0]+g[-1])for g in[re.sub("\D","",c)for c in p.split("\n")])for p in(l,re.sub("(?=("+"|".join(n)+"))",lambda m:str(n.index(m[1]))+m[1][-1],l))])

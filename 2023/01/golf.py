import re
l=open("a").read().split("\n")
n=[0,"one","two","three","four","five","six","seven","eight","nine"]
g=[re.sub("(?=("+"|".join(n[1:])+"))",lambda m:str(n.index(m[1]))+m[1][-1],c)for c in l]
print([sum(int(re.sub("\D","",c)[0]+re.sub("\D","",c)[-1])for c in p)for p in (l,g)])

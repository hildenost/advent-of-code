import re
*_,a=open("a").read().split("\n\n")
a=[[int(n)for n in re.findall(r"\d+",t)]for t in a.splitlines()]
print(sum(t[0]*t[1]>=9*sum(t[2:])for t in a))

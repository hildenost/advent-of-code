import math,re
i,n=open("a").read().split("\n\n")
n={k:v for k,*v in(re.findall("\w+",a)for a in n.split("\n"))}
def t(c,e,s=0):
 for d in 99*i:
  c=n[c][d=="R"];s+=1
  if c[-e:]=="Z"*e:return s
print(t("AAA",3),math.lcm(*[t(a,1)for a in n if a[-1]=="A"]))

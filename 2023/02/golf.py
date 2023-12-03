import re
a=b=0
for n,s in enumerate(open("a"), 1):
 p=o=1
 for c,l in zip("rgb",(12,13,14)):k=max(int(i)for i in re.findall("(\d+) "+c,s));p*=k;o&=k<=l
 a+=n*o
 b+=p
print(a,b)

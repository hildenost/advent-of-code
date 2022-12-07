s,c,t={},[],0
for l in open("a"):
 x,y,*z=l.split()
 if y=="cd":
  if z[0]=="..":
   r=s[tuple(c)]
   if r<=100000:t+=r
   c.pop()
  else:
   c.append(*z)
   s[tuple(c)]=0
 if x.isdigit():
  for i in range(len(c)):s[tuple(c[:i+1])]+=int(x)
print(t,min(s[n]for n in s if s[n]>s[("/",)]-4e7))

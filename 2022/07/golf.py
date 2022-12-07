s,c,t={},(),0
for l in open("a"):
 x,y,*z=l.split()
 if y=="cd":
  if z[0]=="..":
   r=s[c]
   if r<=1e5:t+=r
   c=c[:-1]
  else:
   c+=(*z,)
   s[c]=0
 if x.isdigit():
  for i in range(len(c)):s[c[:i+1]]+=int(x)
print(t,min(s[n]for n in s if s[n]>s[("/",)]-4e7))

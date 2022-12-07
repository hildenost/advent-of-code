s={}
c=()
for l in open("a"):
 x,y,*z=l.split()
 if y=="cd":c=c[:-1]if l[5]=="."else(*c,*z)
 if x.isdigit():
  for i in range(len(c)):s[c[:i+1]]=int(x)+s.get(c[:i+1],0)
print(sum(s[n]for n in s if s[n]<1e5),min(s[n]for n in s if s[n]>s[("/",)]-4e7))

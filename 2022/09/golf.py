for k in 2,10:
 v=set() 
 r=[(0,0)]*k
 for m in open("a"):
  for _ in range(int(m[2:])):
   d=m[0]
   r[0]=(r[0][0]+(d=="R")-(d=="L"),r[0][1]+(d=="U")-(d=="D"))
   for i in range(1,k):
    if all(-2<a-b<2 for a,b in zip(r[i-1],r[i])):break
    dx,dy=[max(-1,min(a-b,1))for a,b in zip(r[i-1],r[i])]
    r[i]=(r[i][0]+dx,r[i][1]+dy)
   v|={r[-1]}
 print(len(v))

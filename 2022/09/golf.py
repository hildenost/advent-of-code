for k in 2,10:
 h=set() 
 r=[(0,0)]*k
 for m in open("a"):
  for _ in range(int(m[2:])):
   d,x,y=m[0],*r[0]
   r=[(x+(d=="R")-(d=="L"),y+(d=="U")-(d=="D")),*[(x+(v>x)-(v<x),y+(w>y)-(w<y))if not(-2<v-x<2 and-2<w-y<2)else(x,y)for(x,y),(v,w)in zip(r[1:],r)]]
   h|={r[-1]}
 print(len(h))

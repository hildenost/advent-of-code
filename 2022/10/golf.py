p=list(open("a"))
X=1
C=0
n=0
s=0
i=0
t=""
q=range
while p:
 if i in q(20,221,40):s+=i*X
 if C<1:
  X+=n
  r=p.pop(0)
  C,n=(1,int(r[5:]))if r[0]=="a"else(0,0)
 else:C=0
 t+="█"if i%40 in q(X-1,X+2)else" "
 i+=1
print(s)
[print(t[i:i+40])for i in q(0,240,40)]

p=lambda s:ord(s)-(96,38)[ord(s)<96]
r=open("a").read().split()
print(sum(p((set(l[len(l)//2:])&set(l[:len(l)//2])).pop()) for l in r),sum(p((set(r[i])&set(r[i+1])&set(r[i+2])).pop()) for i in range(0,len(r),3)))

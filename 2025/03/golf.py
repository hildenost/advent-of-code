j=lambda n:sum(int(f(n,b))for b in open("a"))
def f(n,b):
 if n<1:return""
 m=max(b)
 l,r=b.split(m,1)
 if n<=len(r)+1:return m+f(n-1,r)
 return f(n-len(r)-1,l)+m+r
print(j(2),j(12))

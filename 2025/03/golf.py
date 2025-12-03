j=lambda n:sum(int(f(n,b))for b in open("a"))
def f(n,b):m=max(b);l,r=b.split(m,1);return m if n<2 else m+f(n-1,r)if n<=len(r)+1 else f(n-len(r)-1,l)+m+r
print(j(2),j(12))

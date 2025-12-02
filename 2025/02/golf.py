d=[l.split("-")for l in open("a").read().split(",")]
r=range
i=int
p=lambda n,j:n*j[:len(j)//n]==j
print(sum(j for l,u in d for j in r(i(l),i(u)+1)if p(2,str(j))),sum({j for l,u in d for j in r(i(l),i(u)+1)for n in r(2,len(u)+1)if p(n,str(j))}))

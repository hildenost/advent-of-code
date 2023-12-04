w=[len(set(a[2:12])&set(a[13:]))for a in[l.split()for l in open("a")]]
c=[1]*len(w)
for i,b in enumerate(w):
 for j in range(b):c[j+i+1]+=c[i]
print(sum(2**b//2 for b in w),(sum(c)))

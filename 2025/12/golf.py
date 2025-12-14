i=int
print(sum(i(x[:2])*i(x[3:5])>=9*sum(map(i,x[7:].split()))for x in open("a")if "x" in x))

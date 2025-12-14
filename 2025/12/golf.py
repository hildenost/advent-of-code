i=int
print(sum(i(x[:2])*i(x[3:5])>=9*sum(i(r)for r in x[7:].split())for x in open("a").read().split("\n")if "x" in x))

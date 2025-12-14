import re
print(sum(map(lambda x:x[0]*x[1]>=9*sum(x[2:]),[list(map(int,re.findall(r"\d+",t)))for t in open("a").read().split("\n")if"x"in t])))

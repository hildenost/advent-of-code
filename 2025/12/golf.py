import re
print(sum(x[0]*x[1]>=9*sum(x[2:])for x in [list(map(int,re.findall(r"\d+",t)))for t in open("a").read().split("\n")if"x"in t]))

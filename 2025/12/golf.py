print(sum(int(x[:2])*int(x[3:5])>=9*sum(map(int,x[7:].split()))for x in open("a")if"x"in x))

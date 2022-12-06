m=open("a").read()
for c in 4,14:print([i+c for i in range(len(m))if len(set(m[i:i+c]))==c][0])

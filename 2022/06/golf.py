m=open("a").read()
def f(c):
 for i in range(len(m)):
  t=m[i:i+c]
  if len(t)==len(set(t)):return i+c
print(f(4),f(14))

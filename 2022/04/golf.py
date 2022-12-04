import re
print(*map(sum,zip(*[[a<=x<=y<=b or x<=a<=b<=y,b>=x and y>=a]for a,b,x,y in[map(int,re.split("\D",r,3)) for r in open("a")]])))


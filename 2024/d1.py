# this should of been read from a file
x="""
"""

l=[]
r=[]
ls = x.strip().split("\n")

for ln in ls:
  n1,n2=map(int,ln.split())
  l.append(n1)
  r.append(n2)

t=0
l.sort()
r.sort()
for x,y in zip(l,r):
  t+=abs(x-y)
print(t)

t=0
for i in range(len(l)):
  t+=l[i]*r.count(l[i])

print(t)

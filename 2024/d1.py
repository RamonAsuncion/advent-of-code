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
# should be using zip
for i in range(len(l)):
  # should of sorted the list
  lm=min(l)
  rm=min(r)
  t+=abs(lm-rm)
  l.remove(lm)
  r.remove(rm)

print(t)

# wouldn't have needed this if it was sorted
for ln in ls:
  n1,n2=map(int,ln.split())
  l.append(n1)
  r.append(n2)

t=0
for i in range(len(l)):
  # i probably could of used collection Counter
  t+=l[i]*r.count(l[i])

print(t)

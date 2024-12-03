import re
x="""
"""
total=0
r = re.findall(r"mul\(\d+(?:,\d+)*\)|don't\(\)|do\(\)",x)
no=False
for i in r: 
  if "don't" in i:
    print(i, "no")
    no=True
  elif "don't" not in i and "do" in i:
    no=False
  if not no and "do" not in i:
    product=1
    ds = re.findall(r"\d+", i)
    print(i, "yes", ds)
    for d in ds:
      product*=int(d)
    total+=product
print(total)



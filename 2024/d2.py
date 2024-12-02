x="""
"""

import builtins

class AOCList(list):
  def differ_by(self, diff):
      return all(abs(x - y) in diff for x, y in zip(self, self[1:]))

  def to_int(self):
    return list(map(int,self))

  def strictly_increasing(self):
    return all(x<y for x, y in zip(self, self[1:]))

  def strictly_decreasing(self):
    return all(x>y for x, y in zip(self, self[1:]))

  def strictly_monotonic(self):
    return self.strictly_increasing() or self.strictly_decreasing()

builtins.list = AOCList

lines = x.strip().split('\n')

def check(l):
  return l.strictly_monotonic() and l.differ_by({1,2,3})

def part1():
  t=0
  for line in lines:
    line=AOCList(line.split()).to_int()
    if check(line):
      t+=1
  print(t)

def part2():
  t=0
  for line in lines:
    line=AOCList(line.split()).to_int()
    if check(line) or any(check(AOCList(line[:i]+line[i+1:])) for i in range(len(line))):
      t+=1
  print(t)

part1()
part2()

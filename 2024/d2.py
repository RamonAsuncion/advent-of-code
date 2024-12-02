def differ_by(l, diff):
    return all(abs(x - y) in diff for x, y in zip(l, l[1:]))

def monotonic(l):
    return (all(x < y for x, y in zip(l, l[1:])) or all(x > y for x, y in zip(l, l[1:])))

def check(l):
    return monotonic(l) and differ_by(l, {1, 2, 3})

def part1():
    count = 0
    for line in lines:
        line = list(map(int, line.split()))
        if check(line):
            count += 1
    print(count)

def part2():
    count = 0
    for line in lines:
        line = list(map(int, line.split()))
        if check(line) or any(check(line[:i] + line[i+1:]) for i in range(len(line))):
            count += 1
    print(count)

x = """
"""

lines = x.strip().split('\n')

part1()
part2()

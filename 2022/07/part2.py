from sys import stdin


pwd = ROOT = {}
stack = []
for line in stdin:
    line = line.strip()
    if line.startswith("$"):
        if line.startswith("$ cd"):
            d = line[5:]
            if d == "/":
                pwd = ROOT
                stack = []
            elif d == "..":
                pwd = stack.pop()
            else:
                if d not in pwd:
                    pwd[d] = {}
                stack.append(pwd)
                pwd = pwd[d]
    else:
        x, y = line.split()
        if x == "dir":
            if y not in pwd:
                pwd[y] = {}
        else:
            pwd[y] = int(x)


def size(directory = ROOT):
    if type(directory) == int:
        return directory
    return sum(map(size, directory.values()))


TOTAL_SIZE = size() - 40000000


def solve(directory = ROOT):
    output = float("inf")
    if size(directory) >= TOTAL_SIZE:
        output = size(directory)
    for d in directory.values():
        if type(d) == int:
            continue
        i = solve(d)
        output = min(output, i)
    return output


print(solve())

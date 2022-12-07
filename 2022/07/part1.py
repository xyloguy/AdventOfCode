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


def solve(directory = ROOT):
    if type(directory) == int:
        return (directory, 0)

    total_size = 0
    output = 0
    for d in directory.values():
        i, n = solve(d)
        total_size += i
        output += n

    if total_size <= 100000:
        output += total_size

    return (total_size, output)


print(solve()[1])

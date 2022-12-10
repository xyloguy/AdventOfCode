from sys import stdin
x = 1
ins = []

for line in stdin:
    if line == "noop\n":
        ins.append(x)
    else:
        ins.append(x)
        ins.append(x)
        x += int(line.split()[1])

for i in range(0, len(ins), 40):
    l = ""
    for j in range(40):
        l += "#" if abs(ins[i + j] - j) <= 1 else "."
    print(l)

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

print(sum(x * y + y for x, y in list(enumerate(ins))[19::40]))

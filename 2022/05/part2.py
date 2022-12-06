from sys import stdin


# read in crate input
crate_lines = []
for line in stdin:
	if line.rstrip() == "":
		break
	else:
		crate_lines.append(line)

# create stacks
stacks = [[] for _ in crate_lines.pop().split()]

for _ in range(len(crate_lines)):
	line = crate_lines.pop()
	line = line.replace('[', ' ')
	line = line.replace(']', ' ')
	cols = list(zip(*(iter(line),) * 4))

	index = 0
	for col in cols:
		p = "".join(col).strip()
		if len(p) > 0:
			stacks[index].append(p)
		index += 1


# read in and do moves
for line in stdin:
	line = line.rstrip()
	_, move, _, start, _, end = line.split()
	move, start, end = int(move), int(start) - 1, int(end) -1
	
	crates = stacks[start][-move:]
	for _ in range(move):
		stacks[start].pop()
	stacks[end] += crates


out = ""
for stack in stacks:
	out += stack.pop()

print(out)

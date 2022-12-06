from sys import stdin

totals = []
total = 0

for line in stdin:
	v = line.rstrip()
	if line.rstrip() == "":
		totals.append(total)
		total = 0
	else:
		total += int(v)

totals.sort()
print(sum(totals[::-1][:3]))

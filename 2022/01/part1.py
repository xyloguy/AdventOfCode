from sys import stdin

largest = 0
total = 0

for line in stdin:
	v = line.rstrip()
	if line.rstrip() == "":
		if total > largest:
			largest = total
		total = 0
	else:
		total += int(v)

print(largest)

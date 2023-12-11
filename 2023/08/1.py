lines = [line for line in open(0)]
sequence = lines.pop(0).rstrip()
lines.pop(0)
steps = {line[:3]:{'L': line[7:10], 'R': line[12:15]} for line in lines}

c = 0
step = 'AAA'
while step != 'ZZZ':
	d = sequence[c % len(sequence)]
	step = steps[step][d]
	c += 1
print(c)

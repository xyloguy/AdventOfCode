from math import lcm

lines = [line for line in open(0)]
sequence = lines.pop(0).rstrip()
lines.pop(0)
steps = {line[:3]:{'L':line[7:10], 'R':line[12:15]} for line in lines}

c = 0
t = {}
pos = [line[:3] for line in lines if line[2] == 'A']
while len(t) != len(pos):
	np = []
	d = sequence[c % len(sequence)]
	for step in pos:
		p = steps[step][d]
		if p.endswith('Z'):
			t[step] = c + 1
		np.append(p)
	pos = np
	c += 1
print(lcm(*t.values()))

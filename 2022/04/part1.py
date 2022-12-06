from sys import stdin

def in_range(a, b):
	return a[0] >= b[0] and a[0] <= b[1] and a[1] >= b[0] and a[1] <= b[1]

full_overlaps = 0

for line in stdin:
	line = line.rstrip()
	a,b = line.split(',')

	a = tuple(map(int, a.split('-')))
	b = tuple(map(int, b.split('-')))

	if in_range(a, b) or in_range(b, a):
		full_overlaps += 1

print(full_overlaps)

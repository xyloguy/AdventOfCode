
transform = {
	(0, "-"): 0,
	(0, "7"): 1,
	(0, "J"): 3,
	(2, "-"): 2,
	(2, "F"): 1,
	(2, "L"): 3,
	(1, "|"): 1,
	(1, "L"): 0,
	(1, "J"): 2,
	(3, "|"): 3,
	(3, "F"): 0,
	(3, "7"): 2,
}
grid = [line.rstrip() for line in open(0)]
rows = len(grid)
cols = len(grid[0])

sy = -1
sx = -1
for y, row in enumerate(grid):
	for x, col in enumerate(row):
		if col == "S":
			sy = y
			sx = x
			break
	else:
		continue
	break

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
e = ["-7J", "|LJ", "-FL", "|F7"]
s = []
for i, pos in enumerate(d):
	y = sy + pos[0]
	x = sx + pos[1]
	if all([y >= 0, y <= rows, x >= 0, x <= cols, grid[y][x] in e[i]]):
		s.append(i)

c = s[0]
y = sy + d[c][0]
x = sx + d[c][1]
l = 1
while (y, x) != (sy, sx):
	l += 1
	c = transform[(c, grid[y][x])]
	y += d[c][0]
	x += d[c][1]
print(l // 2)

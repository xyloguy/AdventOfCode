from sys import stdin

points = [(0,0) for _ in range(2)]
min_x = max_x = min_y = max_y = 0

grid = set()
grid.add(points[-1])

def update_p2(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	if abs(x1-x2) > 1:
		if y1 > y2:
			y2 += 1
		elif y2 > y1:
			y2 -= 1
		if x1 > x2:
			x2 += 1
		elif x2 > x1:
			x2 -= 1
	elif abs(y1-y2) > 1:
		if x1 > x2:
			x2 += 1
		elif x2 > x1:
			x2 -= 1
		if y1 > y2:
			y2 += 1
		elif y2 > y1:
			y2 -= 1
	return (x2, y2)


for line in stdin:
	d, c = line.split()
	for _ in range(int(c)):
		hx, hy = points[0]
		if d == "R":
			# right
			hx += 1
		if d == "L":
			#left
			hx -= 1

		if d == "U":
			#up
			hy -= 1

		if d == "D":
			#down
			hy += 1

		points[0] = (hx,hy)

		for i in range(len(points)-1):
			p1 = points[i]
			p2 = points[i+1]
			p2 = update_p2(p1, p2)
			points[i+1] = p2

		tx, ty = points[-1]
		min_x = min(min_x, tx)
		max_x = max(max_x, tx)
		min_y = min(min_y, ty)
		max_y = max(max_y, ty)
		grid.add(points[-1])


# for y in range(min_y, max_y+1):
# 	l = ""
# 	for x in range(min_x, max_x+1):
# 		if (x,y) in grid:
# 			l += "#"
# 		else:
# 			l += "."
# 	print(l)

print(len(grid))

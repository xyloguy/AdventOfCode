from sys import stdin

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


def print_grid(grid, points, line=None, show_start=True, show_tail=False, show_knots=True):
	min_x = max_x = min_y = max_y = 0
	for i in range(len(grid)):
		for x, y in grid[i]:
			min_x = min(min_x, x)
			min_y = min(min_y, y)
			max_x = max(max_x, x)
			max_y = max(max_y, y)
	for y in range(min_y, max_y + 1):
		l = ""
		for x in range(min_x, max_x + 1):
			c = None
			if show_knots:
				for i in range(len(points)):
					x1, y1 = points[i]

					if x == x1 and y == y1:
						c = str(i)
						if i == 0:
							c = "H"
						break
			if show_start and (x,y) == (0,0) and c is None:
				c = "s"
			if show_tail and (x,y) in grid[-1] and c is None:
				c = "#"
			l += c or "."
		print(l)

	print()
	if line is not None:
		print(f"== {line.rstrip()} ==")
	print()


def main():
	p = (0,0)
	knots = 10
	points = [p for _ in range(knots)]
	grid = [{p} for _ in range(knots)]

	for line in stdin:
		d, c = line.split()
		#print_grid(grid, points, line)
		for _ in range(int(c)):
			hx, hy = points[0]
			if d == "R":
				hx += 1
			if d == "L":
				hx -= 1
			if d == "U":
				hy -= 1
			if d == "D":
				hy += 1

			points[0] = (hx,hy)
			grid[0].add((hx,hy))

			for i in range(len(points)-1):
				p1 = points[i]
				p2 = points[i+1]
				p2 = update_p2(p1, p2)
				points[i+1] = p2
				grid[i+1].add(p2)
		

	#print_grid(grid, points)
	#print_grid(grid, points, show_start=True, show_knots=False, show_tail=True)

	print(len(grid[-1]))

if __name__ == "__main__":
	main()

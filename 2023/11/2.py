grid = [line.rstrip() for line in open(0)]
width = len(grid[0])
height = len(grid)

galaxy=[]
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == '#':
            galaxy.append((x, y))

gx = set([x for x, y in galaxy])
gy = set([y for x, y in galaxy])
ecols = [1 if x not in gx else 0 for x in range(width)]
erows = [1 if y not in gy else 0 for y in range(height)]

def distance(a, b):
    x1, x2 = min(a[0], b[0]), max(a[0], b[0])
    y1, y2 = min(a[1], b[1]), max(a[1], b[1])
    ydiff = (y2 - y1) + sum(erows[y1:y2]) * 999999
    xdiff = (x2 - x1) + sum(ecols[x1:x2]) * 999999
    return xdiff + ydiff

dist = 0
for i in range(len(galaxy)):
    for j in range(i + 1, len(galaxy)):
        dist += distance(galaxy[i], galaxy[j])

print(dist)

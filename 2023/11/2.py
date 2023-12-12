grid = [line.rstrip() for line in open(0)]
galaxies = [(x, y) for y, line in enumerate(grid) for x, c in enumerate(line) if c == "#"]
gx = set([x for x, y in galaxies])
gy = set([y for x, y in galaxies])
ecols = [1 if x not in gx else 0 for x in range(len(grid[0]))]
erows = [1 if y not in gy else 0 for y in range(len(grid))]

def distance(a, b):
    x1, x2 = min(a[0], b[0]), max(a[0], b[0])
    y1, y2 = min(a[1], b[1]), max(a[1], b[1])
    ydiff = (y2 - y1) + sum(erows[y1:y2]) * 999999
    xdiff = (x2 - x1) + sum(ecols[x1:x2]) * 999999
    return xdiff + ydiff

print(sum([distance(galaxies[i], galaxies[j]) for i in range(len(galaxies)) for j in range(i + 1, len(galaxies))]))

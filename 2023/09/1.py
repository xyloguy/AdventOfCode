t = 0
for line in open(0):
    grid = [list(map(int, line.rstrip().split()))]
    while len(set(grid[-1])) > 1:
        grid.append([grid[-1][i + 1] - grid[-1][i] for i in range(len(grid[-1]) - 1)])
    
    c = grid[-1][0]
    for i in range(len(grid) - 2, -1, -1):
        c += grid[i][-1]
    t += c
print(t)

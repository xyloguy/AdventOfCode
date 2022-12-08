from sys import stdin
grid = [list(map(int, line.rstrip())) for line in stdin]
best_view = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        current_tree = grid[y][x]
        up = down = left = right = 0
        for i in range(y - 1, -1, -1):
            up += 1
            if grid[i][x] >= current_tree:
                break
        for i in range(y + 1, len(grid)):
            down += 1
            if grid[i][x] >= current_tree:
                break
        for i in range(x - 1, -1, -1):
            left += 1
            if grid[y][i] >= current_tree:
                break
        for i in range(x + 1, len(grid[y])):
            right += 1
            if grid[y][i] >= current_tree:
                break
        best_view = max(best_view, up * down * left * right)
print(best_view)

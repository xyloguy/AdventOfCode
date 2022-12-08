from sys import stdin
grid = [list(map(int, line.rstrip())) for line in stdin]
visible_trees = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        current_tree = grid[y][x]
        if (
            all(grid[y][i] < current_tree for i in range(x))  # left
            or all(grid[y][i] < current_tree for i in range(x + 1, len(grid[y])))  # right
            or all(grid[i][x] < current_tree for i in range(y))  # up
            or all(grid[i][x] < current_tree for i in range(y + 1, len(grid)))  # down
        ):
            visible_trees += 1
print(visible_trees)

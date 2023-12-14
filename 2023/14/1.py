grid = [line.rstrip() for line in open(0)]
grid = list(map("".join, zip(*grid)))
grid = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in grid]
grid = list(map("".join, zip(*grid)))

print(sum([row.count("O") * (len(grid) - r) for r, row in enumerate(grid)]))

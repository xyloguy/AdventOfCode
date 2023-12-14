grid = tuple(line.rstrip() for line in open(0))

def cycle(g):
    for _ in range(4):
        g = tuple(map("".join, zip(*g)))
        g = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in g)
        g = tuple(row[::-1] for row in g)
    return g

seen = {grid}
array = [grid]

i = 0
while True:
    i += 1
    grid = cycle(grid)
    if grid in seen:
        break
    seen.add(grid)
    array.append(grid)
    
first = array.index(grid)
    
grid = array[(1000000000 - first) % (i - first) + first]

print(sum([row.count("O") * (len(grid) - r) for r, row in enumerate(grid)]))

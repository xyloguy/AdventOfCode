import math
print(math.prod([sum([1 for s in range(a) if s * (a - s) > b]) for a, b in zip(*[list(map(int, line.split()[1:])) for line in open(0)])]))

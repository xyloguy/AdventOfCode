def mirror(puzzle):
    for i in range(1, len(puzzle)):
        r1 = puzzle[:i][::-1]
        r2 = puzzle[i:]
        if sum([sum([0 if a == b else 1 for a, b in zip(x, y)]) for x, y in zip(r1, r2)]) == 1:
            return i
    return 0

puzzles = [puzzle.splitlines() for puzzle in open(0).read().split("\n\n")]

t = 0
for puzzle in puzzles:
    y = mirror(puzzle)
    t += y * 100

    x = mirror(list(zip(*puzzle)))
    t += x
print(t)

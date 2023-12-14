def mirror(puzzle):
    for i in range(1, len(puzzle)):
        r1 = puzzle[:i][::-1]
        r2 = puzzle[i:]
        size = min(len(r1), len(r2))
        if r1[:size] == r2[:size]:
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

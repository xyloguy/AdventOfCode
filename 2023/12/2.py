import functools

@functools.lru_cache(maxsize=None)
def solve(r, s):
    if r == "":
        return 1 if s == () else 0

    if s == ():
        return 0 if "#" in r else 1

    t = 0
    if r[0] in ".?":
        t += solve(r[1:], s)
    if r[0] in "#?":
        if s[0] <= len(r) and "." not in r[:s[0]] and (s[0] == len(r) or r[s[0]] != "#"):
            t += solve(r[s[0] + 1:], s[1:])
    return t

total = 0
for line in open(0):
    records, springs = line.split()
    springs = tuple(map(int, springs.split(",")))
    records = "?".join([records] * 5)
    springs *= 5
    total += solve(records, springs)
print(total)

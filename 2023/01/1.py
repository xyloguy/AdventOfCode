t = 0

for line in open(0):
    digits = [ch for ch in line if ch.isdigit()]
    t += int(digits[0] + digits[-1])

print(t)


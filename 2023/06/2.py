# brute force (high memory usage)
# t, r = [int("".join(line.split()[1:])) for line in open(0)]
# print(len([s for s in range(t) if s * (t-s) > r]))


# brute force
# t = int("".join(input().split()[1:]))
# r = int("".join(input().split()[1:]))
# print(sum([1 for s in range(t) if s * (t-s) > r]))


# optimized
# t, r = [int("".join(line.split()[1:])) for line in open(0)]
# print(sum([1 for s in range((t + 1) // 2) if s * (t - s) > r]) * 2)


# single line
# print(sum([(sum([1 for s in range((a + 1) // 2) if s * (a - s) > b]) * 2) for a, b in [[int("".join(line.split()[1:])) for line in open(0)]]]))


# binary search
# t, r = [int("".join(line.split()[1:])) for line in open(0)]
# if t % 2 == 0:
# 	m = t//2
# else:
# 	m = (t+1)//2
# l = 0
# h = m
# d = l + (h-l)//2
# od = d
# a = d * (t-d)
# while a != r:
# 	if r < a:
# 		h = d
# 	elif r > a:
# 		l = d
# 	od = d
# 	d = l + (h-l)//2
# 	if d == od:
# 		break
# 	a = d * (t-d)
# a = max(d, l, h)
# print((m-a)*2)


# quadratic
import math
time, distance = [int("".join(line.split()[1:])) for line in open(0)]
low1 = (time + math.sqrt((time ** 2) - (4 * distance))) / (2)
low2 = (time - math.sqrt((time ** 2) - (4 * distance))) / (2)
print(time - (2 * math.ceil(min(low1, low2))) + 1)




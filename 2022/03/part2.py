from sys import stdin
from string import ascii_letters as letters

def priority(char):
	return letters.index(char) + 1

def rstrip(s):
	return s.rstrip()

total = 0
s = map(rstrip, stdin.readlines())
groups = zip(*(iter(s),) * 3)

for a, b, c in groups:
	for char in a:
		if char in b and char in c:
			total += priority(char)
			break

print(total)

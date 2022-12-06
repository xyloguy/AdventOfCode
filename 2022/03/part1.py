from sys import stdin
from string import ascii_letters as letters


def priority(char):
	return letters.index(char) + 1

total = 0
for rucksack in stdin:
	rucksack = rucksack.rstrip()
	l = len(rucksack) // 2
	for char in rucksack[:l]:
		if char in rucksack[l:]:
			total += priority(char)
			break
print(total)

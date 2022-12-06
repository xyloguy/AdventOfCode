string = input()

size = 14
for i in range(0, len(string)-size):
	if len(set(string[i:i+size])) == size:
		print(i + size)
		exit()

string = input(); size = 14; l = [(i + size) for i in range(0, len(string)-size) if len(set(string[i:i+size])) == size]; print(l[0])

from sys import stdin

class H:
	def __init__(self, shape):
		self.shape = {
			'A': 'rock',
			'rock': 'rock',
			'B': 'paper',
			'paper': 'paper',
			'C': 'scissors',
			'scissors': 'scissors',
		}[shape]

		self.value = {
			'rock': 1,
			'paper': 2,
			'scissors': 3,
		}[self.shape]

	def win(self):
		return H({
			'rock': 'paper',
			'paper': 'scissors',
			'scissors': 'rock',
		}[self.shape])

	def draw(self):
		return H(self.shape)

	def lose(self):
		return H({
			'paper': 'rock',
			'scissors': 'paper',
			'rock': 'scissors',
		}[self.shape])

	def __eq__(self, other):
		return self.shape == other.shape

	def __gt__(self, other):
		if self == other:
			return False

		a = self.shape
		b = other.shape
		if a == 'rock' and b == 'scissors':
			return True

		elif a == 'paper' and b == 'rock':
			return True

		elif a == 'scissors' and b == 'paper':
			return True
		return False

	def __lt__(self, other):
		return other > self

class O:
	def __init__(self, you, other):
		self.value = you.value
		if you > other:
			self.value += 6
		elif you == other:
			self.value += 3
		elif you < other:
			self.value += 0

def score(shape, outcome):
	return shape.value + outcome.value


total = 0
for line in stdin:
	x,y = line.rstrip().split()
	h = H(x)
	s = {'X': h.lose(), 'Y': h.draw(), 'Z': h.win()}[y]
	outcome = O(s, h)
	total += outcome.value

print(total)

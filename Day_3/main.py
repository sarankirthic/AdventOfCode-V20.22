filename = "input.txt"
def count(b):
	letter_dict = {}
	for i in b:
		letter_dict[i] = letter_dict.get(i,0)+1
	return letter_dict


def task_1(b1, b2, m):
	letter_dict1 = count(b1)
	letter_dict2 = count(b2)
	for i in set(letter_dict1.keys()).intersection(letter_dict2.keys()):
		if i.islower():
			return i, ord(i) - ord('a') + 1
		else:
			return i, ord(i) - ord('A') + 27


def spliting(b):
	a, total = [], 0
	for i in b:
		n = len(i)
		m = int(n/2)
		b1, b2 = i[0:m], i[m:n]
		j, k = task_1(b1, b2, m)
		a.append(k)
	for i in a:
		total += i
	return total


def task_2(b):
	total = 0
	for i in range(0,len(b),3):
		x, y, z = b[i], b[i+1], b[i+2]
		a1, a2, a3 = count(x), count(y), count(z)
		for i in set(a1.keys()).intersection(a2.keys(), a3.keys()):
			if i.islower():
				i = ord(i) - ord('a') + 1
			else:
				i = ord(i) - ord('A') + 27
			total += i
	return total

if __name__ == "__main__":
	with open(filename, "r") as file:
		b = []
		for i in file:
			i = i.rstrip()
			b.append(i)
			# spliting into containers
		print(spliting(b))
		print(task_2(b))
			
# ['pqgZZSZgcZJqpz', 'BbqTbbLjBDBLhB']

"""
{'p': 2, 'q': 3, 'g': 2, 'Z': 4, 'S': 1, 'c': 1, 'J': 1, 'z': 1, 'B': 4, 'b': 3, 'T': 1, 'L': 2, 'j': 1, 'D': 1, 'h': 1} 
{'w': 1, 'H': 3, 'p': 1, 't': 3, 'F': 4, 's': 1, 'L': 1, 'M': 1, 'D': 2, 'Q': 1, 'T': 1, 'b': 2, 'j': 1} 
{'f': 4, 'V': 1, 'v': 1, 's': 2, 't': 1, 'w': 3, 'P': 1, 'H': 2, 'N': 2, 'G': 1, 'W': 2, 'R': 1, 'S': 2, 'n': 1, 'l': 2, 'p': 1, 'C': 3, 'c': 1, 'J': 1, 'z': 2, 'd': 4, 'r': 1, 'g': 1}
"""


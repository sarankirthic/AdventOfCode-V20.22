def input_formating(filename):
	lines, matrix = [], []
	count = 0
	a = ''
	with open(filename, "r") as file:
		for i, line in enumerate(file):
			if i>=10:
				line = line.rstrip().split(' ')
				lines.append([line[1],line[3],line[5]])
	return lines


def invertrowcolumn(matrix):
	for i in range(len(matrix)):
		for j in range(len(i)):
			print(i, j, matrix[i][j])


def task_1(lines, matrix):
	for i in range(len(lines)):
		for j in range(lines[i][0]):
			print("hello")
			break



if __name__ == "__main__":
	a = []
	position = input_formating("input.txt")
	matrix = [	'0 0 Q B 0 0 H 0 0',
				'0 F W D Q 0 S 0 0',
				'0 D C N S G F 0 0',
				'0 R D L C N Q 0 R',
				'V W L M P S M 0 M',
				'J B F P B B P F F',
				'B V G J N D B L V',
				'D P R W H R Z W S']
	for i in matrix:
		i = i.split(" ")
		a.append(i)
	for i in a:
		print(i)
	invertrowcolumn(a)
	a = task_1(a)

"""
		[Q] [B]         [H]        
	[F] [W] [D] [Q]     [S]        
	[D] [C] [N] [S] [G] [F]        
	[R] [D] [L] [C] [N] [Q]     [R]
[V] [W] [L] [M] [P] [S] [M]     [M]
[J] [B] [F] [P] [B] [B] [P] [F] [F]
[B] [V] [G] [J] [N] [D] [B] [L] [V]
[D] [P] [R] [W] [H] [R] [Z] [W] [S]

[[0, 0, Q, "B", 0, 0, "H", 0, 0]]

"""
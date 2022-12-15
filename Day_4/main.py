def input_formating(filename):
	a, b, e = [], [], []
	with open(filename, "r") as file:
		for i in file:
			i = i.rstrip()
			i = i.split(',')
			x, y = i[0].split('-'), i[1].split('-')
			e.append([int(x[0]), int(x[1]), int(y[0]), int(y[1])])
	return e

def task_1(a):
	count = 0
	for i in range(len(a)):
		if a[i][0]>=a[i][2] and a[i][1]<=a[i][3]:
			count += 1
		elif a[i][0]<=a[i][2] and a[i][1]>=a[i][3]:
			count += 1
	return count


def task_2(a):
	c, d = [], []
	count = 0
	for i in a:
		print(i)
		c, d = range(i[0], i[1] + 1), range(i[2], i[3] + 1)
		if set(c).intersection(set(d)):
			count += 1
	return count


if __name__ == "__main__":
	a = input_formating("input.txt")
	print(task_1(a))
	print(task_2(a))
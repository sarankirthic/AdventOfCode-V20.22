filename = "input.txt"
a, b, c, d, e = [], [], [], [], []
def wonorlost(n):
	a, b, c, d, e = [], [], [], [], []
	for i in range(n):
		if a[i] == "X":
			if b[i] == "C":
				c.append(1)
				d.append(6)
				e.append("L")
			elif b[i] == "A":
				c.append(1)
				d.append(3)
				e.append("L")
			elif b[i] == "B":
				c.append(1)
				d.append(0)
				e.append("L")
		elif a[i] == "Y":
			if b[i] == "A":
				c.append(2)
				d.append(6)
				e.append("D")
			elif b[i] == "B":
				c.append(2)
				d.append(3)
				e.append("D")
			elif b[i] == "C":
				c.append(2)
				d.append(0)
				e.append("D")
		elif a[i] == "Z":
			if b[i] == "B":
				c.append(3)
				d.append(6)
				e.append("W")
			elif b[i] == "C":
				c.append(3)
				d.append(3)
				e.append("W")
			elif b[i] == "A":
				c.append(3)
				d.append(0)
				e.append("W")
	return a,b,c,d,e

def winorlose(n):
	c, d = [], []
	for i in range(n):
		if a[i] == "X":
			# I need to lose
			if b[i] == "A":
				c.append(0)
				d.append(3)
			elif b[i] == "B":
				c.append(0)
				d.append(1)
			elif b[i] == "C":
				c.append(0)
				d.append(2)
		elif a[i] == "Y":
			# I need to draw
			if b[i] == "A":
				c.append(3)
				d.append(1)
			elif b[i] == "B":
				c.append(3)
				d.append(2)
			elif b[i] == "C":
				c.append(3)
				d.append(3)
		elif a[i] == "Z":
			if b[i] == "A":
				c.append(6)
				d.append(2)
			elif b[i] == "B":
				c.append(6)
				d.append(3)
			elif b[i] == "C":
				c.append(6)
				d.append(1)
			# I need to win
	return c,d


with open(filename, "r") as file:
	for i in file:
		i = i.rstrip()
		a.append(i[2])
		b.append(i[0])

n = len(a)
# c,d = wonorlost(n)
c,d = winorlose(n)
points = 0
for i in range(n):
	round_points = c[i] + d[i]
	print(c[i], d[i], round_points)
	points = points + round_points
print(points)
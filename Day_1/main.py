filename = "input.txt"
a, b, c= [], [], []

def sort(li):
	less = []
	equal = []
	greater = []

	if len(li) > 1:
		pivot = li[0]
		for x in li:
			if x > pivot:
				less.append(x)
			elif x == pivot:
				equal.append(x)
			elif x < pivot:
				greater.append(x)
		# Don't forget to return something!
		return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
	# Note that you want equal ^^^^^ not pivot
	else: 
		return li

with open(filename, "r") as file:
	for i in file:	
		i = i.rstrip()
		if (i==""):
			b.append(a)
			a = []
		else:
			a.append(i)
for i in b:
	su = 0
	for j in i:
		su = su + int(j)
	c.append(su)

li = sort(c)
print(li[0]+li[1]+li[2])

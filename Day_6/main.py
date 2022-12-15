signal = []
def subroutine(signal):
	i = 0
	part_1 = 4
	part_2 = 14
	while len(set(signal[:part_1])) != part_1:
		signal = signal[1:]
		i += 1
	print(i+part_1)
	while len(set(signal[:part_2])) != part_2:
		signal = signal[1:]
		i += 1
	print(i+part_2)


with open("input.txt", "r") as file:
	for i in file:
		signal = i.rstrip()
		subroutine(signal)
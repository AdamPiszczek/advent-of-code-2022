def part1():
	with open("day_6.txt") as file:
		line = file.readline()
		amount = 0
		for i in range(0,len(line) - 4):
			current_chars = line[i:i+4]
			if len(set(current_chars)) == len(current_chars): # every set element is unique (no duplicates)
				amount = i + 4
				break

		print(amount)


def part2():
	with open("day_6.txt") as file:
		line = file.readline()
		amount = 0
		for i in range(0,len(line) - 14):
			current_chars = line[i:i+14]
			if len(set(current_chars)) == len(current_chars): # every set element is unique (no duplicates)
				amount = i + 14
				break

		print(amount)


part1()
part2()



def part1():
	with open('input.txt') as file:
		priorities = 0
		for line in file.readlines():
			first_part, secon_dpart = line[:len(line)//2], line[len(line)//2:]
			flag = None
			for char in first_part:
				if char in secon_dpart:
					if char.islower():
						priorities += ord(char) - ord('a') + 1
						flag = True
					elif char.isupper():
						priorities += ord(char) - ord('A') + 27
						flag = True
				if flag == True:
					flag = False
					break
	print(priorities)

def part2():
	priorities = 0
	with open('input.txt') as file:
		rucksack = list()
		counter = 0
		line_counter = 0
		rucksack.append(list())
		for line in file.readlines():
			line = line.split('\n')[0]
			rucksack[counter].append(line)
			line_counter += 1
			if line_counter == 3:
				line_counter = 0
				counter += 1
				rucksack.append(list())
		for lists in rucksack:
			if len(lists) == 3:
				flag = False
				for char in lists[0]:
					if char in lists[1]:
						if char in lists[2]:
							if char.islower():
								priorities += ord(char) - ord('a') + 1
								flag = True
							elif char.isupper():
								priorities += ord(char) - ord('A') + 27
								flag = True
					if flag == True:
						flag = False
						break

		print(priorities)

part1()
part2()

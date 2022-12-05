def part1():
	lines = list()
	with open('day_5.txt') as file:
		for line in file:
			lines.append(line + " ")

		queues = list()
		for i in range(0,9):
			queues.append(list())

		j = 1
		for counter in range(0,9):
			for i in range(0,8):
				if lines[i][j].isupper():
					queues[counter].append(lines[i][j])
			j += 4

		for i in range(0,9):
			queues[i].reverse()

		for i in range(10,len(lines)):
			_, first, _, second, _, third = lines[i].strip().split(' ')
			first = int(first)
			second = int(second)
			third = int(third)

			for i in range(0, first):
				last_element = queues[second-1].pop()
				queues[third-1].append(last_element)

		string = ""
		for i in range(0,9):
			if len(queues[i]) > 0:
				string += queues[i].pop()

		print(string)


def part2():
	lines = list()
	with open('day_5.txt') as file:
		for line in file:
			lines.append(line + " ")

		queues = list()
		for i in range(0,9):
			queues.append(list())

		j = 1
		for counter in range(0,9):
			for i in range(0,8):
				if lines[i][j].isupper():
					queues[counter].append(lines[i][j])
			j += 4

		for i in range(0,9):
			queues[i].reverse()

		for i in range(10,len(lines)):
			_, first, _, second, _, third = lines[i].strip().split(' ')
			first = int(first)
			second = int(second)
			third = int(third)

			temp = list()
			for i in range(0, first):
				last_element = queues[second-1].pop()
				temp.append(last_element)
			temp.reverse()
			for element in temp:
				queues[third-1].append(element)

		string = ""
		for i in range(0,9):
			if len(queues[i]) > 0:
				string += queues[i].pop()

		print(string)


part1()
part2()
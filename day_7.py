with open("day_7.txt") as file:
	dirs = dict() # saving each directory with its corresponding size
	path = list() # setting the path in each iteration

	for line in file.readlines():
		current_command = line.split()
		if current_command[0] == "$":
			if current_command[1] == "cd":
				if current_command[2] == "..":
					path.pop()
				elif current_command[2] == "/":
					path = ["/"]
				else:
					path.append(current_command[2])
		else:
			if current_command[0] != "dir":
				current_path = ""
				for dir in path:
					if current_path != "/" and dir != "/":
						current_path += "/"
					current_path += dir
					dirs[current_path] = dirs.get(current_path, 0) + int(current_command[0])

sum_of_values = 0
for _, value in dirs.items():
	if value < 100_000:
		sum_of_values += value

print(sum_of_values)

search_values = list()
occupied_space = int(dirs.get("/"))
needed_space = 30_000_000 - (70_000_000 - occupied_space)
for _, value in dirs.items():
	if value >= needed_space:
		search_values.append(value)

print(min(search_values))
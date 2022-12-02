me = list()
oponent = list()

with open('input') as file:
    for line in file.readlines():
        oponent_selection = line.split(" ")[0]
        my_choice = line.split(" ")[1].split('\n')[0]
        me.append(my_choice)
        oponent.append(oponent_selection)

def part1():
    points = 0
    for i in range(0,2500):
        if me[i] == 'X': # rock
            points += 1
            if oponent[i] == "A": # rock
                points += 3
            elif oponent[i] == "C": # scissors
                points += 6
        if me[i] == 'Y': # paper
            points += 2
            if oponent[i] == "B": # paper
                points += 3
            elif oponent[i] == "A": # rock
                points += 6
        elif me[i] == 'Z': # scissors
            points += 3
            if oponent[i] == "C": # scissors
                points += 3
            elif oponent[i] == "B": # paper
                points += 6
    print(points)

def part2():
    points = 0
    for i in range(0,2500):
        if me[i] == 'X': # rock
            if oponent[i] == "A": # rock
                points += 3
            elif oponent[i] == "B": # paper
                points += 1
            elif oponent[i] == "C": # scissors
                points += 2
        if me[i] == 'Y': # paper
            if oponent[i] == "A": # rock
                points += 4
            elif oponent[i] == "B": # paper
                points += 5
            elif oponent[i] == "C": # scissors
                points += 6
        elif me[i] == 'Z': # scissors
            if oponent[i] == "A": # rock
                points += 8
            elif oponent[i] == "B": # paper
                points += 9
            elif oponent[i] == "C": # scissors
                points += 7
    print(points)

part1()
part2()

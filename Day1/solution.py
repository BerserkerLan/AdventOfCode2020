with open('input.txt', 'r') as input_file:
    data = input_file.read()
lines_split = data.split('\n')
for i in range(0, len(lines_split)):
    for j in range(i, len(lines_split)):
        if (int(lines_split[i]) + int(lines_split[j]) == 2020):
            print("Part 1: Found an {} and {} for 2020, solution is {}".format(lines_split[i], lines_split[j], int(lines_split[i]) * int(lines_split[j])))

for i in range(0, len(lines_split)):
    for j in range(i, len(lines_split)):
        for k in range(j, len(lines_split)):
            if (int(lines_split[i]) + int(lines_split[j]) + int(lines_split[k]) == 2020):
                print("Part 2: Found an {} and {} and {} for 2020, solution is {}".format(lines_split[i], lines_split[j], lines_split[k], int(lines_split[i]) * int(lines_split[j]) * int(lines_split[k])))



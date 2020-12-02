with open('input.txt', 'r') as input_file:
    data = input_file.read()

lines_split = data.split('\n')
valid_passwords = []

def count_chars(str, char):
    count = 0
    for character in str:
        if character == char:
            count = count + 1
    return count

for line in lines_split:
    if (len(line) == 0):
        continue
    segmented_line = line.split(' ')

    occurances = segmented_line[0].split('-')
    min_occ = int(occurances[0])
    max_occ = int(occurances[1])

    character_to_check = segmented_line[1][0]

    password = segmented_line[2]

    if (count_chars(password, character_to_check) >= min_occ and count_chars(password, character_to_check) <= max_occ):
        valid_passwords.append(password)

print(len(valid_passwords))

# End of Part 1

valid_passwords.clear()
for line in lines_split:
    if (len(line) == 0):
        continue
    segmented_line = line.split(' ')

    positions = segmented_line[0].split('-')
    first_pos = int(positions[0]) - 1
    second_pos = int(positions[1]) - 1

    character_to_check = segmented_line[1][0]

    password = segmented_line[2]

    if ((password[first_pos] == character_to_check or password[second_pos] == character_to_check) and not(password[first_pos] == character_to_check and password[second_pos] == character_to_check)):
        valid_passwords.append(password)

print(len(valid_passwords))
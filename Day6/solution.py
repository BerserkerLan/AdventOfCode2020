from collections import Counter

with open('input.txt', 'r') as input_file:
    data = input_file.read()


groups_list = data.split('\n\n')

sum_of_unique_answers = 0

for group in groups_list:
    unique_answers_in_group = set()
    for person_answer in group:
        for answer in person_answer:
            if not(answer == '\n'): unique_answers_in_group.add(answer)
    sum_of_unique_answers = sum_of_unique_answers + len(unique_answers_in_group)

print(sum_of_unique_answers)

#Part 2

def remove_new_lines_in_list(the_list):
    new_list = []
    for item in the_list:
        if not(item == '\n' or item == ''):
            new_list.append(item)
    return new_list

sum_of_unique_answers_per_group = 0

for group in groups_list:
    answers_in_group = []
    for person_answer in group:
        for answer in person_answer:
            if not(answer == '\n'): answers_in_group.append(answer)
    count_of_answer = Counter(elem[0] for elem  in answers_in_group)
    print(count_of_answer)
    for counts in count_of_answer:
        something = group.split('\n')
        print(remove_new_lines_in_list(something))
        split_group = remove_new_lines_in_list(group.split('\n'))
        if (count_of_answer[counts] == len(split_group)):
            sum_of_unique_answers_per_group = sum_of_unique_answers_per_group + 1


print(sum_of_unique_answers_per_group)
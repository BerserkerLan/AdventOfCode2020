with open('input.txt', 'r') as input_file:
    data = input_file.read()

def determine_row(boarding_pass_seat, upper_bound, lower_bound):
    if (boarding_pass_seat is None or boarding_pass_seat == ''):
        return lower_bound
    if (boarding_pass_seat[0] not in ['F', 'B']):
        return lower_bound # In this case, upper and lower bound will be the same, so we just return any one of them
    if (boarding_pass_seat[0] == 'F'):
        return determine_row(boarding_pass_seat[1:], (upper_bound + lower_bound - 1)/2, lower_bound)
    elif (boarding_pass_seat[0] == 'B'):
        return determine_row(boarding_pass_seat[1:], upper_bound, (upper_bound + lower_bound + 1)/2)

def determine_column(boarding_pass_seat, upper_bound, lower_bound):
    if (boarding_pass_seat is None or boarding_pass_seat == ''):
        return upper_bound
    if (boarding_pass_seat[0] == 'L'):
        return determine_column(boarding_pass_seat[1:], (upper_bound + lower_bound - 1)/2, lower_bound)
    elif (boarding_pass_seat[0] == 'R'):
        return determine_column(boarding_pass_seat[1:], upper_bound, (upper_bound + lower_bound + 1)/2)

# print(determine_row("BFFFFFFRLL", 127, 0))
# print(determine_column("BFFFFFFRLL"[7:], 7, 0))

boarding_pass_list = data.split('\n')
seat_id_list = []

for boarding_pass in boarding_pass_list:
    seat_id_list.append((int(determine_row(boarding_pass, 127, 0)) * 8) + int(determine_column(boarding_pass[7:], 7, 0)))

print(max(seat_id_list))

# Part 2

def find_gap_in_seat_list(seat_list):
    for i in range(0, len(seat_list)):
        if i != (len(seat_list) - 1):
            if (not(seat_list[i+1] - seat_list[i] == 1)):
                return seat_list[i] + 1

seat_id_list.sort()
unique_seat_ids = list(dict.fromkeys(seat_id_list))

print(find_gap_in_seat_list(unique_seat_ids))
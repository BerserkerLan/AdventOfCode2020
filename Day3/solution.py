with open('input.txt', 'r') as input_file:
    data = input_file.read()

def get_trees_encountered(map, right_step, bottom_step):
    # [row, column]
    current_coord = [0,0]
    reached_end = False
    trees_encountered = 0
    while not reached_end:
        current_coord[0] = current_coord[0] + bottom_step
        current_coord[1] = (current_coord[1] + right_step) % (len(map[0]))
        if (current_coord[0] >= (len(map) - 1) or current_coord[1] >= len(map[0])):
            reached_end = True
            continue
        if (map[ (current_coord[0]) ][ (current_coord[1]) ] == '#' ):
            trees_encountered = trees_encountered + 1
    return trees_encountered

#Part 1
print(get_trees_encountered(data.split('\n'), 3, 1))

# Part Two (Actually make part 1 a function, makes sense to do so)
print(
    get_trees_encountered(data.split('\n'), 1, 1) *
    get_trees_encountered(data.split('\n'), 3, 1) *
    get_trees_encountered(data.split('\n'), 5, 1) *
    get_trees_encountered(data.split('\n'), 7, 1) *
    get_trees_encountered(data.split('\n'), 1, 2)
)

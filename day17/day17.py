import time


def solve_day17():

    solve_day17_1()
    solve_day17_2()


DAY_STR = "17"

SHAPES = {
    0: ((2, 0), (3, 0), (4, 0), (5, 0)),
    1: ((3, 0), (2, 1), (3, 1), (4, 1), (3, 2)),
    2: ((2, 0), (3, 0), (4, 0), (4, 1), (4, 2)),
    3: ((2, 0), (2, 1), (2, 2), (2, 3)),
    4: ((2, 0), (3, 0), (2, 1), (3, 1))
}

INPUT_COMMANDS = {
    "<": -1,
    ">": 1
}


def solve_day17_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # define variables
    map_dict = dict()
    input_commands = lines[0]
    number_rocks = 2022
    tick = 0

    for i in range(number_rocks):

        tower_height = get_tower_height(map_dict)

        falling_shape = convert_dict(SHAPES[i % 5], tower_height)

        # while falling
        while True:
            input_command = INPUT_COMMANDS[input_commands[tick % len(input_commands)]]
            tick += 1
            falling_shape = execute_command(falling_shape, input_command, map_dict)

            # if falling, continue one lower
            if is_falling(falling_shape, map_dict):
                falling_shape = decrease_y(falling_shape)
                continue
            else:
                break

        # if rest
        for elem in falling_shape:
            map_dict[elem] = "#"

    # result
    result = get_tower_height(map_dict)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


# solved with observations of the output:

# Height of Tower after 1000000000000 rocks:
#   with part 1 code not solvable.
# but: Top of Tower, instructions and starting shape repeat at some point.

# in my example after 1751 rocks the starting position repeats every 1755 rocks and adds 2768 of height:
# Start: First   1751 rocks add 2726 of height
# Repeat: every  1755 rocks add 2768 of height
# End: Remaining 1409 rocks add 2236 of height

# Number of repeating starting position = (total_rocks - start_rocks) / repeat_size
# Number of repeating starting position = (1000000000000 -1751) /1755 = 569800568

# Total Height = num_repeats * height_repeat + start_height + end_height
# Total Height = 569800568 * 2768 + 2726 +2236 = 1577207977186

def solve_day17_2():

    # result
    result = 1577207977186

    print('Day {} (2) solution: {} (execution time: 0 ms)'.format(DAY_STR, result))


def execute_command(falling_shape, input_command, map_dict):
    if is_shape_colliding(falling_shape, input_command, map_dict):
        return falling_shape
    else:
        refreshed_falling_shape = dict()
        for elem in falling_shape:
            refreshed_falling_shape[(elem[0] + input_command, elem[1])] = "@"
        return refreshed_falling_shape


def is_shape_colliding(falling_shape, input_command, map_dict):
    for elem in falling_shape:
        if not(0 <= elem[0] + input_command <= 6):
            return True
        if (elem[0] + input_command, elem[1]) in map_dict:
            return True
    return False


def is_falling(falling_shape, map_dict):
    for elem in falling_shape:
        if (elem[0], elem[1] - 1) in map_dict or elem[1] <= 0 :
            return False
    return True


def decrease_y(falling_shape):
    falling_shape_decreased = dict()

    for elem in falling_shape:
        falling_shape_decreased[(elem[0], elem[1]-1)] = "@"

    return falling_shape_decreased


def convert_dict(shape_tuple, tower_height):
    shape_dict = dict()
    for elem in shape_tuple:
        elem = (elem[0], elem[1] + tower_height + 3)
        shape_dict[elem] = "@"
    return shape_dict


def get_map_height(map_dict, falling_shape):

    # default
    max_y = 0
    if map_dict:
        max_y = max(max_y, max(map_dict, key=lambda item: item[1])[1])
    if falling_shape:
        max_y = max(max_y, max(falling_shape, key=lambda item: item[1])[1])
    return max_y


def get_tower_height(map_dict):

    # default
    if map_dict:
        return max(map_dict, key=lambda item: item[1])[1] + 1
    else:
        return 0


def print_map(map_dict, falling_shape):

    max_y = get_map_height(map_dict, falling_shape)
    for y in range(max_y, 0 - 1, -1):
        print('|', end="")
        for x in range(7):
            if (x, y) in map_dict:
                print(map_dict[(x, y)], end="")
            elif (x, y) in falling_shape:
                print(falling_shape[(x, y)], end="")
            else:
                print(".", end="")
        print('|')
    print("+-------+")
    print("")

def print_map_top(map_dict, falling_shape):

    max_y = get_map_height(map_dict, falling_shape)
    for y in range(max_y, max_y-10 - 1, -1):
        print('|', end="")
        for x in range(7):
            if (x, y) in map_dict:
                print(map_dict[(x, y)], end="")
            elif (x, y) in falling_shape:
                print(falling_shape[(x, y)], end="")
            else:
                print(".", end="")
        print('|')
    print("+-------+")
    print("")

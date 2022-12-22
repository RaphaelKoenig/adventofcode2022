import time
import re

DAY_STR = "22"


def solve_day22():

    solve_day22_1()
    # solve_day22_2()


DIRECTIONS = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}


def solve_day22_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.replace("\n", "") for x in lines]

    # define variables

    path_desc, map_dict = parse_input(lines)

    # starting position (row, column)
    pos = get_starting_position(map_dict)

    # starting direction, R = (1, 0), L = (-1, 0), D = (0, 1), U = (0, -1)
    dir_int = 0

    # solve
    for command in path_desc:
        pos, dir_int = execute_command(map_dict, command, pos, dir_int)

    # result
    result = 1000 * pos[1] + 4 * pos[0] + dir_int

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def parse_input(lines):

    path_desc = parse_input_path_desc(lines.pop())
    map_dict = parse_input_map_dict(lines[:-1])

    return path_desc, map_dict


def parse_input_path_desc(line):

    path_desc = []
    numbers = list(map(int, re.findall(r'\d+', line)))
    directions = [x for x in line if not x.isnumeric()]

    for i in range(len(directions)):
        path_desc.append(numbers[i])
        path_desc.append(directions[i])
    path_desc.append(numbers[-1])

    return path_desc


def parse_input_map_dict(lines):

    max_x = len(max(lines, key=lambda item: len(item)))
    max_y = len(lines)

    map_dict = dict()

    for y in range(max_y):
        for x in range(max_x):
            if x >= len(lines[y]):
                continue
            coordinates = (x+1, y+1)
            if lines[y][x] != " ":
                map_dict[coordinates] = lines[y][x]

    return map_dict


def get_map_size(map_dict):

    max_x = max(map_dict, key=lambda item: item[0])[0]
    max_y = max(map_dict, key=lambda item: item[1])[1]
    min_x = min(map_dict, key=lambda item: item[0])[0]
    min_y = min(map_dict, key=lambda item: item[1])[1]

    return (min_x, max_x), (min_y, max_y)


def get_starting_position(map_dict):

    map_size = get_map_size(map_dict)
    min_x, max_x = map_size[0]
    min_y, max_y = map_size[1]

    for x in range(min_x, max_x+1):
        if (x, min_y) in map_dict:
            if map_dict[(x, min_y)] == ".":
                return x, min_y


def print_map(map_dir, curr_pos):

    map_size = get_map_size(map_dir)
    min_x, max_x = map_size[0]
    min_y, max_y = map_size[1]

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            pos = (x,y)
            if curr_pos == pos:
                print("O", end="")
            elif pos in map_dir:
                print(map_dir[pos], end="")
            else:
                print(" ", end="")
        print("")
    print("")


def execute_command(map_dict, command, pos, dir_int):

    if isinstance(command, str):
        if command == "R":
            return pos, (dir_int + 1) % 4
        else:
            return pos, (dir_int - 1) % 4
    else:
        for i in range(command):
            pos, blocked = move_step(map_dict, pos, dir_int)
            if blocked:
                return pos, dir_int
        return pos, dir_int


# return new position and if path is blocked
def move_step(map_dict, pos, dir_int):

    dir = DIRECTIONS[dir_int]
    old_pos = pos
    new_pos = (pos[0] + dir[0], pos[1] + dir[1])
    if new_pos in map_dict:
        if map_dict[new_pos] == ".":
            return new_pos, False
        elif map_dict[new_pos] == "#":
            return old_pos, True
    else:
        return wrap_around(map_dict, pos, dir_int)


def wrap_around(map_dict, pos, dir_int):

    contrary_dir = DIRECTIONS[(dir_int + 2) % 4]
    old_pos = pos
    while (pos[0] + contrary_dir[0], pos[1] + contrary_dir[1]) in map_dict:
        pos = (pos[0] + contrary_dir[0], pos[1] + contrary_dir[1])
    if map_dict[pos] == "#":
        return old_pos, True
    else:
        return pos, False

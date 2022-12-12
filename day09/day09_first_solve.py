import time
import copy

DAY_STR = "09"


def solve_day09():

    solve_day09_1()
    solve_day09_2()


def solve_day09_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # define variables
    length_of_tail = 1

    motions_of_head = get_motions_from_lines(lines)

    # calculate map size and starting position
    map_size, position_starting = calculate_map_size(motions_of_head)

    # fill map with (rows, columns)
    rope_map = fill_map(map_size)

    # calculate path and mark visited positions
    calculate_path(rope_map, motions_of_head, position_starting, length_of_tail)

    # count visited positions
    visited_positions = count_visited_positions(rope_map)

    # result
    result = visited_positions

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day09_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # define variables
    length_of_tail = 9

    motions_of_head = get_motions_from_lines(lines)

    # calculate map size and starting position
    map_size, position_starting = calculate_map_size(motions_of_head)

    # fill map with (rows, columns)
    rope_map = fill_map(map_size)

    # calculate path and mark visited positions
    calculate_path(rope_map, motions_of_head, position_starting, length_of_tail)

    # count visited positions
    visited_positions = count_visited_positions(rope_map)

    # result
    result = visited_positions

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def get_motions_from_lines(lines):

    motions_of_head = [x.strip().split(" ") for x in lines]
    motions_of_head = [[x[0], int(x[1])] for x in motions_of_head]
    return motions_of_head


def fill_map(map_size):

    row_int, column_int = map_size
    rope_map = [[False for x in range(column_int)] for y in range(row_int)]
    return rope_map


def calculate_map_size(motions_of_head):

    row_column_max = [0, 0]
    row_column_min = [0, 0]
    position = [0, 0]
    for motion in motions_of_head:
        direction = motion[0]
        step_size = motion[1]
        if direction == 'R':
            position[1] += step_size
            if position[1] > row_column_max[1]:
                row_column_max[1] = position[1]
        elif direction == 'L':
            position[1] -= step_size
            if position[1] < row_column_min[1]:
                row_column_min[1] = position[1]
        elif direction == 'D':
            position[0] += step_size
            if position[0] > row_column_max[0]:
                row_column_max[0] = position[0]
        elif direction == 'U':
            position[0] -= step_size
            if position[0] < row_column_min[0]:
                row_column_min[0] = position[0]
        else:
            raise RuntimeError('Direction is not R,L,D,U')

    map_size = list(map(lambda x, y: x-y+1, row_column_max, row_column_min))
    position_starting = list(map(abs, row_column_min))

    return map_size, position_starting


def calculate_path(rope_map, motions_of_head, position_starting, length_of_tail):
    positions = []

    for i in range(length_of_tail+1):
        positions.append(copy.deepcopy(position_starting))

    # mark starting position as "visited"
    mark_visited_position(rope_map, position_starting)

    for motion in motions_of_head:
        positions = calculate_motion(rope_map, motion, position_starting, positions)


def calculate_motion(rope_map, motion, position_starting, positions):

    direction = motion[0]
    step_size = motion[1]

    for step in range(step_size):
        positions = calculate_step(direction, positions)
        mark_visited_position(rope_map, positions[-1])
    return positions


def calculate_step(direction, positions):

    positions_new = list()
    for index, position in enumerate(positions):
        if index == 0:
            positions_new.append(calculate_step_head(direction, position))
        else:
            positions_new.append(calculate_step_tail(positions_new[-1], position))

    return positions_new


def calculate_step_head(direction, position_head):

    if direction == 'R':
        position_head[1] += 1
    elif direction == 'L':
        position_head[1] -= 1
    elif direction == 'D':
        position_head[0] += 1
    elif direction == 'U':
        position_head[0] -= 1
    else:
        raise RuntimeError('Direction is not R,L,D,U')
    return position_head


def calculate_step_tail(position_head, position_tail):

    # adjacent or same position
    if is_adjacent(position_head, position_tail):
        return position_tail
    else:
        # same row/column
        if position_head[0] == position_tail[0]:
            # right
            if position_head[1] > position_tail[1]:
                position_tail[1] += 1
            # left
            elif position_head[1] < position_tail[1]:
                position_tail[1] -= 1

        elif position_head[1] == position_tail[1]:
            # down
            if position_head[0] > position_tail[0]:
                position_tail[0] += 1
            # up
            elif position_head[0] < position_tail[0]:
                position_tail[0] -= 1
        # diagonal
        elif position_head[0] > position_tail[0]:
            # down right
            if position_head[1] > position_tail[1]:
                position_tail = [position_tail[0] + 1, position_tail[1] + 1]
            # down left
            else:
                position_tail = [position_tail[0] + 1, position_tail[1] - 1]

        elif position_head[0] < position_tail[0]:
            # up right
            if position_head[1] > position_tail[1]:
                position_tail = [position_tail[0] - 1, position_tail[1] + 1]
            # up left
            else:
                position_tail = [position_tail[0] - 1, position_tail[1] - 1]
        else:
            raise RuntimeError('Some case not covered (Tail movement)')
    return position_tail


def is_adjacent(position_head, position_tail):

    if position_tail[0] - 1 <= position_head[0] <= position_tail[0] + 1:
        if position_tail[1] - 1 <= position_head[1] <= position_tail[1] + 1:
            return True
        else:
            return False
    else:
        return False


def mark_visited_position(rope_map, position_tail):

    rope_map[position_tail[0]][position_tail[1]] = True


def count_visited_positions(rope_map):

    visited_positions = 0
    for index_row in range(len(rope_map)):
        for index_column in range(len(rope_map[0])):
            if rope_map[index_row][index_column]:
                visited_positions += 1
    return visited_positions


def print_map(rope_map, position_starting, positions):

    row_int, column_int = len(rope_map), len(rope_map[0])
    rope_map_print = [["." for x in range(column_int)] for y in range(row_int)]

    for index_row in range(len(rope_map)):
        for index_column in range(len(rope_map[0])):
            if rope_map[index_row][index_column]:
                rope_map_print[index_row][index_column] = "#"

    rope_map_print[position_starting[0]][position_starting[1]] = "s"

    for index, position in enumerate(positions):
        if rope_map_print[position[0]][position[1]] == "s" or rope_map_print[position[0]][position[1]] == "#"\
                or rope_map_print[position[0]][position[1]] == ".":
            rope_map_print[position[0]][position[1]] = str(index)

    if len(positions) > 0:
        rope_map_print[positions[0][0]][positions[0][1]] = "H"

    for row in rope_map_print:
        for column in row:
            print("\033[1m" + column + "\033[0m" + " ", end='')
        print("")
    print("")

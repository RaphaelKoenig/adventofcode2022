import time

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

    # calculate path and mark visited positions
    visited_positions = calculate_path(motions_of_head, length_of_tail)

    # result = visited_positions
    result = len(visited_positions)

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

    # calculate path and mark visited positions
    visited_positions = calculate_path(motions_of_head, length_of_tail)

    # result = visited_positions
    result = len(visited_positions)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def get_motions_from_lines(lines):

    motions_of_head = [x.strip().split(" ") for x in lines]
    motions_of_head = [[x[0], int(x[1])] for x in motions_of_head]
    return motions_of_head


def calculate_path(motions_of_head, length_of_tail):

    positions = []
    visited_positions = set()

    for i in range(length_of_tail+1):
        positions.append((0, 0))

    # mark starting position as "visited"
    # mark_visited_position(rope_map, position_starting)
    visited_positions.add((0, 0))

    for motion in motions_of_head:
        positions, visited_position = calculate_motion(motion, positions, visited_positions)
    return visited_positions


def calculate_motion(motion, positions, visited_positions):

    direction = motion[0]
    step_size = motion[1]

    for step in range(step_size):
        positions = calculate_step(direction, positions)
        visited_positions.add(positions[-1])

    return positions, visited_positions


def calculate_step(direction, positions):

    positions_new = list()
    for index, position in enumerate(positions):
        if index == 0:
            positions_new.append(calculate_step_head(direction, position))
        else:
            positions_new.append(calculate_step_tail_tuple(positions_new[-1], position))

    return positions_new


def calculate_step_head(direction, position_head):

    if direction == 'R':
        position_head = (position_head[0], position_head[1] + 1)
    elif direction == 'L':
        position_head = (position_head[0], position_head[1] - 1)
    elif direction == 'D':
        position_head = (position_head[0] + 1, position_head[1])
    elif direction == 'U':
        position_head = (position_head[0] - 1, position_head[1])
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


def calculate_step_tail_tuple(position_head, position_tail):

    # adjacent or same position
    if is_adjacent(position_head, position_tail):
        return position_tail
    else:
        # same row/column
        if position_head[0] == position_tail[0]:
            # right
            if position_head[1] > position_tail[1]:
                position_tail = (position_tail[0], position_tail[1] + 1)
                # position_tail[1] += 1
            # left
            elif position_head[1] < position_tail[1]:
                position_tail = (position_tail[0], position_tail[1] - 1)
                # position_tail[1] -= 1

        elif position_head[1] == position_tail[1]:
            # down
            if position_head[0] > position_tail[0]:
                position_tail = (position_tail[0] + 1, position_tail[1])
                # position_tail[0] += 1
            # up
            elif position_head[0] < position_tail[0]:
                position_tail = (position_tail[0] - 1, position_tail[1])
        # diagonal
        elif position_head[0] > position_tail[0]:
            # down right
            if position_head[1] > position_tail[1]:
                position_tail = (position_tail[0] + 1, position_tail[1] + 1)
                # position_tail = [position_tail[0] + 1, position_tail[1] + 1]
            # down left
            else:
                position_tail = (position_tail[0] + 1, position_tail[1] - 1)
                # position_tail = [position_tail[0] + 1, position_tail[1] - 1]

        elif position_head[0] < position_tail[0]:
            # up right
            if position_head[1] > position_tail[1]:
                position_tail = (position_tail[0] - 1, position_tail[1] + 1)
                # position_tail = [position_tail[0] - 1, position_tail[1] + 1]
            # up left
            else:
                position_tail = (position_tail[0] - 1, position_tail[1] - 1)
                # position_tail = [position_tail[0] - 1, position_tail[1] - 1]
        else:
            raise RuntimeError('Some case not covered (Tail movement)')
    return position_tail


def is_adjacent(position_head, position_tail):

    if position_tail[0] - 1 <= position_head[0] <= position_tail[0] + 1 and \
            position_tail[1] - 1 <= position_head[1] <= position_tail[1] + 1:
        return True
    else:
        return False

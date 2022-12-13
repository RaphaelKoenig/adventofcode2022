import time
import ast
import functools

DAY_STR = "13"


def solve_day13():

    solve_day13_1()
    solve_day13_2()


def solve_day13_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    pair = []
    right_order_indices = []

    # solve: check if pair is in right order, if so -> add to list right_order_indices
    for index, line in enumerate(lines):
        if line == "":
            smaller = check_pair(pair[0], pair[1])
            if not smaller == 1:
                right_order_indices.append(index // 3 + 1)
            pair = []
        else:
            pair.append(ast.literal_eval(line))

    # last element in lines
    decided = check_pair(pair[0], pair[1])
    if not decided == 1:
        right_order_indices.append(index // 3 + 1)

    # result
    result = sum(right_order_indices)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day13_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    result = 1
    lines_parsed = []

    # add divider packets
    lines.append("[[2]]")
    lines.append("[[6]]")

    for line in lines:
        if line != "":
            lines_parsed.append(ast.literal_eval(line))

    lines_sorted = sorted(lines_parsed, key=functools.cmp_to_key(check_pair))
    for index, line in enumerate(lines_sorted):
        # multiply divider packets indices
        if line == [[2]] or line == [[6]]:
            result = result * (index + 1)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


# 1 pair_1 bigger, 0 not clear, -1 pair_1 smaller
def check_pair(pair_1, pair_2):

    # if both are integer
    if isinstance(pair_1, int) and isinstance(pair_2, int):
        if pair_1 > pair_2:
            # pair_1 int > pair_2 int -> 1
            return 1
            # pair_1 int < pair_2 int -> 1
        elif pair_1 < pair_2:
            return -1
        else:
            return 0

    # if pair_1 is int, pair_2 is list -> put the int in a list and check again
    if isinstance(pair_1, int) and isinstance(pair_2, list):
        return check_pair([pair_1], pair_2)

    # if pair_1 is list, pair_2 is int -> put the int in a list and check again
    if isinstance(pair_1, list) and isinstance(pair_2, int):
        return check_pair(pair_1, [pair_2])

    # if both are lists, iterate over every element
    if isinstance(pair_1, list) and isinstance(pair_2, list):
        for index, elem in enumerate(pair_1):
            pair_1_1 = elem

            # len pair_2 empty and not decided yet -> 1
            if index > len(pair_2)-1:
                return 1

            # if still enough elements in both lists -> check first element of both
            pair_2_1 = pair_2[index]
            smaller = check_pair(pair_1_1, pair_2_1)

            # if "Check More" (smaller == 0) then continue, else -> 1 or -1
            if smaller == 1:
                return 1
            elif smaller == -1:
                return -1

    # reached end, if lists the same size 0, else list_2 > list_1 -> -1
    if len(pair_1) == len(pair_2):
        return 0
    else:
        return -1

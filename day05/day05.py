# template day
import time
from collections import deque
import re

day_str = "05"


def solve_day05():
    solve_day05_1()
    solve_day05_2()


def solve_day05_1():
    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and no(!) whitespaces
    lines = [x.replace("\n", "") for x in lines]

    # define variables

    # results of the items on top of each stack
    top_of_each_stack = ""

    # moves:  list of moves(Strings)
    # stacks: list of stacks
    stacks, moves = parse_input(lines)

    # do we move the items individually or in bulk? (part 1 = False) (part 2 = True)
    bulk = False

    # solve: move items between stacks
    for move in moves:
        move_stack(move, stacks, bulk)

    # get result (top item of each stack)
    for stack in stacks:
        top_of_each_stack += stack.pop()

    # result
    result = top_of_each_stack

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def solve_day05_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and no(!) whitespaces
    lines = [x.replace("\n", "") for x in lines]

    # define variables

    # results of the items on top of each stack
    top_of_each_stack = ""

    # moves:  list of moves(Strings)
    # stacks: list of stacks
    stacks, moves = parse_input(lines)

    # do we move the items individually or in bulk? (part 1 = False) (part 2 = True)
    bulk = True

    # solve: move items between stacks
    for move in moves:
        move_stack(move, stacks, bulk)

    # get result (top item of each stack)
    for stack in stacks:
        top_of_each_stack += stack.pop()

    # result
    result = top_of_each_stack

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def parse_input(lines):

    # stacks_unstructured:  used to import the stacks, list of stacks with number of stacks at the end
    # moves:                list of moves(Strings)
    # fill stacks_stacks_unstructured and moves
    stacks_unstructured, moves = split_input_data(lines)

    # fill stacks
    stacks = fill_stacks(stacks_unstructured)
    return stacks, moves


def split_input_data(lines):

    # boolean used to split the input
    already_moves = False
    stacks_unstructured = []
    moves_str = []
    for line in lines:
        if line == "":
            already_moves = True
            continue
        if not already_moves:
            stacks_unstructured.append(line)
        else:
            moves_str.append(line)
    return stacks_unstructured, moves_str


def fill_stacks(stacks_unstructured):

    # list of stacks
    stacks = []

    # define the number of stacks (last number in the last row of the stacks_str list)
    number_of_stacks = int(re.findall(r'\d+', stacks_unstructured[-1])[-1])

    # remove last row that includes the number of stacks
    stacks_str = stacks_unstructured[:-1]

    # add empty stacks to stacks
    for _ in (range(number_of_stacks)):
        stacks.append(deque())

    # fill stacks
    for line in stacks_str:
        for index, character in enumerate(line):
            if index % 4 == 1:
                if character.isalpha():
                    stacks[index // 4].appendleft(character)
    return stacks


def move_stack(move_str, stacks, bulk):

    count_int, from_int, to_int = get_ints_from_move(move_str)

    if bulk:
        right_order = deque()
        for i in range(0, count_int):
            right_order.append(stacks[from_int - 1].pop())
        for i in range(0, len(right_order)):
            stacks[to_int - 1].append(right_order.pop())
    else:
        for i in range(0, count_int):
            stacks[to_int-1].append(stacks[from_int-1].pop())


def get_ints_from_move(move_str):

    count_int, from_int, to_int = map(int, re.findall(r'\d+', move_str))
    # alternative
    # count_int, from_int, to_int = map(int, re.split('move|from|to', move_str)[1:])

    return count_int, from_int, to_int

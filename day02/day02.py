# template day

import time


def solve():
    solve_day02_1()
    solve_day02_2()


def solve_day02_1():
    # start execution time
    start_time = time.perf_counter()

    # read file Using readlines()
    input_file = open('day02/input.txt', 'r')
    lines = input_file.readlines()
    # print(lines)

    # remove \n and whitespaces
    lines = [x.replace("\n", "").strip() for x in lines]
    # print(lines)

    # define variables

    # solution
    solution = 0

    # stop execution time
    end_time = time.perf_counter()

    print('Day 0 (1) solution: {} (execution time: {} ms)'.format(solution, round((end_time - start_time) * 1000, 2)))


def solve_day02_2():

    # start execution time
    start_time = time.perf_counter()

    # read file Using readlines()
    input_file = open('day02/input.txt', 'r')
    lines = input_file.readlines()
    # print(lines)

    # remove \n and whitespaces
    lines = [x.replace("\n", "").strip() for x in lines]
    # print(lines)

    # define variables

    # result
    result = 0

    # stop execution time
    end_time = time.perf_counter()

    print('Day 0 (2) solution: {} (execution time: {} ms)'.format(result, round((end_time - start_time) * 1000, 2)))
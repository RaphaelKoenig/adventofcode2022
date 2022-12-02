# template day
import time

day_str = "03"

def solve_day03():
    solve_day03_1()
    solve_day03_2()


def solve_day03_1():
    # start execution time
    start_time = time.perf_counter()

    # read file using readlines()
    input_file = open('day' + day_str + '/input.txt', 'r')
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

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def solve_day03_2():

    # start execution time
    start_time = time.perf_counter()

    # read file Using readlines()
    input_file = open('day' + day_str + '/input.txt', 'r')
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

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))
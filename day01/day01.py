import time


def solve_day01():
    solve_day01_1()
    solve_day01_2()


def solve_day01_1():

    # start execution time
    start_time = time.perf_counter()

    # read file using readlines()
    input_file = open('day01/input.txt', 'r')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.replace("\n", "").strip() for x in lines]

    # define variables
    calories_by_elf = []
    sum_calories = 0

    # sum calories per elf
    for line in lines:
        if line == "":
            calories_by_elf.append(sum_calories)
            sum_calories = 0
        else:
            sum_calories += int(line)

    # result = calories of elf with highest calories
    result = (max(calories_by_elf))

    # stop execution time
    end_time = time.perf_counter()

    print('Day 1 (1) solution: {} (execution time: {} ms)'.format(result, round((end_time - start_time) * 1000, 2)))


def solve_day01_2():

    # start execution time
    start_time = time.perf_counter()

    # read file Using readlines()
    input_file = open('day01/input.txt', 'r')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.replace("\n", "").strip() for x in lines]

    # define variables
    calories_by_elf = []
    sum_calories = 0

    # sum calories per elf
    for line in lines:
        if line == "":
            calories_by_elf.append(sum_calories)
            sum_calories = 0
        else:
            sum_calories += int(line)

    # sort calories by elf descending
    calories_by_elf = sorted([x for x in calories_by_elf], reverse=True)

    # result = sum first 3 values
    result = (sum(calories_by_elf[:3]))

    # stop execution time
    end_time = time.perf_counter()

    print('Day 1 (2) solution: {} (execution time: {} ms)'.format(result, round((end_time - start_time) * 1000, 2)))
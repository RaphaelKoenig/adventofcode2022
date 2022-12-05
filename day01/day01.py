import time

day_str = "01"


def solve_day01():
    solve_day01_1()
    solve_day01_2()


def solve_day01_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

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

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def solve_day01_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

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
    calories_by_elf.sort(reverse=True)

    # result = sum first 3 values
    result = (sum(calories_by_elf[:3]))

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))

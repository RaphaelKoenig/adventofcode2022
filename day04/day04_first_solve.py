# first version
import time

DAY_STR = "04"


def solve_day04():

    solve_day04_1()
    solve_day04_2()


def solve_day04_1():

    # start execution time
    start_time = time.perf_counter()

    # read file using readlines()
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]
    print(lines)

    # define variables
    assignment_pairs = 0

    # solve
    for line in lines:
        a1, a2 = line.split(",")
        a11, a12 = a1.split("-")
        a21, a22 = a2.split("-")

        if(int(a11) <= int(a21) and int(a12) >= int(a22)) or (int(a21) <= int(a11) and int(a22) >= int(a12)):
            assignment_pairs += 1

    # result
    result = assignment_pairs

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day04_2():

    # start execution time
    start_time = time.perf_counter()

    # read file using readlines()
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()
    # print(lines)

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    assignment_overlaps = 0

    # solve
    for line in lines:
        a1, a2 = line.split(",")
        a11, a12 = a1.split("-")
        a21, a22 = a2.split("-")

        if (int(a11) >= int(a21) and int(a11) <= int(a21)) or (int(a21) >= int(a11) and int(a21) <= int(a12)) \
                or (int(a12) >= int(a22) and int(a12) <= int(a21)) or (int(a22) >= int(a11) and int(a22) <= int(a12)) \
                or (int(a11) <= int(a21) and int(a12) >= int(a22)) or (int(a21) <= int(a11) and int(a22) >= int(a12)):
            assignment_overlaps += 1

    # result
    result = assignment_overlaps

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))
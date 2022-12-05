# refactored version
import time

day_str = "04"


def solve_day04():
    solve_day04_1()
    solve_day04_2()


def solve_day04_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    assignment_pairs = 0

    # solve
    for line in lines:
        assignment_pair1, assignment_pair2 = line.split(",")
        if is_assignment_pair(assignment_pair1, assignment_pair2):
            assignment_pairs += 1

    # result
    result = assignment_pairs

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def solve_day04_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    assignment_overlaps = 0

    # solve
    for line in lines:
        assignment_pair1, assignment_pair2 = line.split(",")

        if (
                is_assignment_pair(assignment_pair1, assignment_pair2) or
                does_assignment_pair_overlap(assignment_pair1, assignment_pair2)
        ):
            assignment_overlaps += 1

    # result
    result = assignment_overlaps

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def assignments_to_int(a1, a2):
    a11, a12 = map(int, a1.split("-"))
    a21, a22 = map(int, a2.split("-"))
    return a11, a12, a21, a22


def is_assignment_pair(a1, a2):
    a11, a12, a21, a22 = assignments_to_int(a1, a2)
    if (
            int(a11) <= int(a21) and int(a12) >= int(a22) or
            int(a21) <= int(a11) and int(a22) >= int(a12)
    ):
        return True
    return False


def does_assignment_pair_overlap(a1, a2):
    a11, a12, a21, a22 = assignments_to_int(a1, a2)
    if(
            int(a11) >= int(a21) >= int(a11) or int(a11) <= int(a21) <= int(a12) or
            int(a22) <= int(a12) <= int(a21) or int(a11) <= int(a22) <= int(a12)
    ):
        return True
    return False

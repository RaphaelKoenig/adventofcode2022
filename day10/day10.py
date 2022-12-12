import time

DAY_STR = "10"


def solve_day10():
    solve_day10_1()
    solve_day10_2()


def solve_day10_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    cycle = 1
    x = 1
    signal_strength_sum = 0
    wait_time = 0
    command = ""

    # solve
    while lines or wait_time > 0:

        if wait_time == 0:
            if command != "":
                x = execute_command(x, command)
            if lines:
                command = lines.pop(0)
                wait_time = get_wait_time(command)

        if cycle % 40 == 20:
            signal_strength_sum += x * cycle

        cycle += 1
        wait_time -= 1

    # result
    result = signal_strength_sum

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day10_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    cycle = 1
    x = 1
    wait_time = 0
    command = ""
    screen = ""

    # solve

    while lines or wait_time > 0:

        if wait_time == 0:
            if command != "":
                x = execute_command(x, command)
            if lines:
                command = lines.pop(0)
                wait_time = get_wait_time(command)

        if x - 1 <= (cycle - 1) % 40 <= x + 1:
            screen += "#"
        else:
            screen += " "

        cycle += 1
        wait_time -= 1

    # result
    # print_screen(screen)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, "BZPAJELK", round((end_time - start_time) * 1000, 2)))


def execute_command(x, command):

    if command == "noop":
        return x
    else:
        return x + int(command.split(" ")[1])


def get_wait_time(command):

    if command == "noop":
        return 1
    else:
        return 2


def print_screen(screen):

    for index, character in enumerate(screen):
        print(character, end='')
        if index % 40 == 39:
            print("")
    print("")
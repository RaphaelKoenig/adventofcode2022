import time

day_str = "07"


def solve_day07():
    solve_day07_1()
    solve_day07_2()


def solve_day07_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    directories = {"/root": 0}
    total_size_10000 = 0

    # solve
    fill_directories_from_input(lines, directories)

    for Dir in directories:
        if directories[Dir] < 100000:
            total_size_10000 += directories[Dir]

    # result
    result = total_size_10000

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def solve_day07_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()
    # print(lines)

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]
    # print(lines)

    # define variables
    directories = {"/root": 0}

    # solve
    fill_directories_from_input(lines, directories)

    # print(directories)

    threshold = directories["/root"] - 40000000
    candidates = []
    for Dir in directories:
        if threshold <= directories[Dir]:
            candidates.append(directories[Dir])

    # result
    result = min(candidates)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def fill_directories_from_input(lines, directories):

    for line in lines:

        # executed commands
        if line[0] == "$":

            if line[2:4] == "cd":

                if line[5:6] == "/":
                    current = "/root"

                elif line[5:7] == "..":
                    current = current[0:current.rfind("/")]

                else:
                    current = current + "/" + (line[5:])
                    directories.update({current: 0})
                    # move in a level

            elif line[2:4] == "ls":
                pass

        # dir does not do anything
        elif line[0:3] == "dir":
            pass

        # size of files
        else:
            amount = int(line[:line.find(" ")])
            dict_loc = current

            for i in range(current.count("/")):
                directories[dict_loc] += amount
                dict_loc = dict_loc[:dict_loc.rfind("/")]
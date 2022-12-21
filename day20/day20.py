import time

DAY_STR = "20"


def solve_day20():

    solve_day20_1()
    solve_day20_2()


def solve_day20_1():

    def parse_input(lines):
        number_list = []
        result_list = []
        for index, line in enumerate(lines):
            number_list.append((int(line), index))
            result_list.append((int(line), index))
            if line == "0":
                zero_element = (int(line), index)
        return number_list, result_list, zero_element

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # parse input
    number_list, result_list, zero_element = parse_input(lines)

    # move
    for number in number_list:
        move_number(result_list, number)

    # calculate grove coordinates
    grove_coordinates = calculate_grove_coordinates(result_list, zero_element)

    result = sum(grove_coordinates)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day20_2():

    def parse_input(lines):
        number_list = list()
        result_list = list()
        for index, line in enumerate(lines):
            number = int(line) * 811589153
            number_list.append((number, index))
            result_list.append((number, index))
            if line == "0":
                zero_element = (number, index)
        return number_list, result_list, zero_element

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # parse input
    number_list, result_list, zero_element = parse_input(lines)

    # move
    for i in range(10):
        for number in number_list:
            move_number(result_list, number)

    # calculate grove coordinates
    grove_coordinates = calculate_grove_coordinates(result_list, zero_element)

    # result
    result = sum(grove_coordinates)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def move_number(result_list, number):

    # memorize old index
    old_index = result_list.index(number)

    # length of result_list:
    length = len(result_list)

    # remove old
    result_list.remove(number)

    # add new position
    new_index = (old_index + number[0]) % (length - 1)

    result_list.insert(new_index, number)


def calculate_grove_coordinates(result_list, zero_element):

    grove_coordinates = []
    index_0 = result_list.index(zero_element)

    for i in [1000, 2000, 3000]:
        grove_coordinates.append(result_list[(index_0 + i) % (len(result_list))][0])

    return grove_coordinates
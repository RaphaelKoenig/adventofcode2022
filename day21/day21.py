import time
import re

DAY_STR = "21"


def solve_day21():
    solve_day21_1()
    solve_day21_2()


def solve_day21_1():

    def parse_input(lines):
        solved_dict = dict()
        unsolved_dict = dict()
        for line in lines:
            key, value = line.split(": ")
            value_numbers = re.findall(r'\d+', value)
            if len(value_numbers) > 0:
                solved_dict[key] = int(value_numbers[0])
            else:
                value_literals = value.split(" ")
                unsolved_dict[key] = (value_literals[0], value_literals[1], value_literals[2])
        return solved_dict, unsolved_dict

    def resolve(key):
        if key in solved_dict:
            return solved_dict[key]
        else:
            value = unsolved_dict[key]
            operand_1, operand_2 = value[0], value[2]
            if value[1] == "+":
                return resolve(operand_1) + resolve(operand_2)
            elif value[1] == "-":
                return resolve(operand_1) - resolve(operand_2)
            elif value[1] == "*":
                return resolve(operand_1) * resolve(operand_2)
            elif value[1] == "/":
                return resolve(operand_1) // resolve(operand_2)
            else:
                raise RuntimeError("operator not known")

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # parse input
    solved_dict, unsolved_dict = parse_input(lines)

    # solve
    result = resolve("root")

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result,
                                                                   round((end_time - start_time) * 1000, 2)))


def solve_day21_2():

    def parse_input(lines):
        solved_dict = dict()
        unsolved_dict = dict()
        for line in lines:
            key, value = line.split(": ")
            value_numbers = re.findall(r'\d+', value)
            if len(value_numbers) > 0:
                solved_dict[key] = int(value_numbers[0])
            else:
                value_literals = value.split(" ")
                if key == "root":
                    unsolved_dict[key] = (value_literals[0], "-", value_literals[2])
                else:
                    unsolved_dict[key] = (value_literals[0], value_literals[1], value_literals[2])
        return solved_dict, unsolved_dict

    def resolve(key):
        if key in solved_dict:
            return solved_dict[key]
        else:
            value = unsolved_dict[key]
            operand_1, operand_2 = value[0], value[2]
            if value[1] == "+":
                return resolve(operand_1) + resolve(operand_2)
            elif value[1] == "-":
                return resolve(operand_1) - resolve(operand_2)
            elif value[1] == "*":
                return resolve(operand_1) * resolve(operand_2)
            elif value[1] == "/":
                return resolve(operand_1) // resolve(operand_2)
            else:
                raise RuntimeError("operator not known")

    def resolve_strict(key):
        if key in solved_dict:
            return solved_dict[key]
        else:
            value = unsolved_dict[key]
            operand_1, operand_2 = value[0], value[2]
            if value[1] == "+":
                return resolve_strict(operand_1) + resolve_strict(operand_2)
            elif value[1] == "-":
                return resolve_strict(operand_1) - resolve_strict(operand_2)
            elif value[1] == "*":
                return resolve_strict(operand_1) * resolve_strict(operand_2)
            elif value[1] == "/":
                if resolve_strict(operand_1) % resolve_strict(operand_2) == 0:
                    return resolve_strict(operand_1) // resolve_strict(operand_2)
                else: RuntimeError("not divisible without remainder")


            else:
                raise RuntimeError("operator not known")

    def binary_search(positive, lower_bound, upper_bound):
        next_try = lower_bound + ((upper_bound-lower_bound) // 2)
        solved_dict["humn"] = next_try
        difference = resolve("root")

        # check for duplicates
        if difference == 0:
            possible_results = list()
            for i in range (lower_bound, upper_bound + 1):
                solved_dict["humn"] = i
                if resolve("root") == 0:
                    possible_results.append(i)
            return possible_results

        # fixes bug with different sign_change
        if positive:
            if difference < 0:
                return binary_search(positive, lower_bound, next_try)
            else:
                return binary_search(positive, next_try, upper_bound)
        else:
            if difference > 0:
                return binary_search(positive, lower_bound, next_try)
            else:
                return binary_search(positive, next_try, upper_bound)

    # get lower and upper bound
    def get_bounds():
        positive = True
        sign_change = False
        solved_dict["humn"] = 0
        starting_difference = resolve("root")

        if starting_difference == 0:
            return positive, 0, 0
        else:
            positive = starting_difference > 0
        exponent = 0

        while not sign_change:
            counter = 2 ** exponent

            solved_dict["humn"] = counter
            difference = resolve("root")
            if difference > 0 and not positive or difference < 0 and positive:
                return positive, counter // 2, counter

            solved_dict["humn"] = - counter
            difference = resolve("root")
            if difference > 0 and not positive or difference < 0 and positive:
                return positive, counter, counter // 2
            exponent += 1

    def filter_possible_results(possible_results):
        for possible_result in possible_results:
            try:
                solved_dict["humn"] = possible_result
                resolve_strict("root")
                return possible_result
            except:
                continue

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # parse input
    solved_dict, unsolved_dict = parse_input(lines)

    # get lower and upper bound
    positive, lower_bound, upper_bound = get_bounds()
    # solve with binary search
    possible_results = binary_search(positive, lower_bound, upper_bound)

    # because of floor division there can be more than 1 result which should be checked again with strict division
    result = filter_possible_results(possible_results)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result,
                                                                   round((end_time - start_time) * 1000, 2)))

# template day
import time

day_str = "03"


def solve_day03():
    solve_day03_1()
    solve_day03_2()


# get priority from input letter: a = 1, b = 2 ... z = 26, A = 27, B = 28 ... Z = 52
def get_priority(character):
    priority = ord(character) - 38 if ord(character) < 97 else ord(character) - 97
    return priority


def solve_day03_1():

    # start execution time
    start_time = time.perf_counter()

    # read file using readlines()
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    priority_sum = 0

    # split every rucksack in 2 same size compartments and intersect them to find item(s)? that appears in both
    for rucksack in lines:
        split_int = int(len(rucksack)/2)

        compartment_1_set = set(rucksack[:split_int])
        compartment_2_set = set(rucksack[-split_int:])
        intersection = compartment_1_set.intersection(compartment_2_set)

        for character in intersection:
            priority_sum += get_priority(character)


    # result
    result = priority_sum

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def solve_day03_2():

    # start execution time
    start_time = time.perf_counter()

    # read file using readlines()
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    priority_sum = 0
    for index, rucksack in enumerate(lines):
        if index % 3 == 0:
            compartment_1_set = set(rucksack)
        elif index % 3 == 1:
            compartment_2_set = set(rucksack)
        else:
            compartment_3_set = set(rucksack)
            intersection = compartment_1_set.intersection(compartment_2_set).intersection(compartment_3_set)
            for character in intersection:
                priority_sum += get_priority(character)

    # result
    result = priority_sum

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(day_str, result,
                                                                   round((end_time - start_time) * 1000, 2)))


# r = rucksack
# p = get priority
# c = character

# get priority from character
def p(c):
    return ord(c) - 38 if ord(c) < 97 else ord(c) - 97


# split every rucksack in 2 same size compartments and intersect them to find item that appears in both
def solve_day03_1_short():
    print(sum(p(next(iter(set(r[:int(len(r)/2)]).intersection(set(r[-int(len(r)/2):]))))) for r in [x.strip() for x in open('day' + day_str + '/input.txt').readlines()]))


def solve_day03_2_short():

    result = 0
    for index, rucksack in enumerate([x.strip() for x in open('day' + day_str + '/input.txt').readlines()]):
        if index % 3 == 0:
            set_compartment_1 = set(rucksack)
        elif index % 3 == 1:
            set_compartment_2 = set(rucksack)
        else:
            set_compartment_3 = set(rucksack)
            intersection = set_compartment_1.intersection(set_compartment_2).intersection(set_compartment_3)

            result += p(next(iter(set(intersection))))
    print(result)


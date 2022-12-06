# template day
import time

day_str = "06"


def solve_day06():
    solve_day06_1()
    solve_day06_2()


def solve_day06_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    characters = lines[0]
    # start of paket marker = spm
    spm_length = 4

    # solve
    spm_index = calculate_spm_index(characters, spm_length)

    for i in range(0, len(characters)-3):
        if len(set(characters[i:i+4])) == 4:
            start_of_paket_marker_index = i + 4
            break

    # result
    result = spm_index

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def solve_day06_2():
    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    characters = lines[0]
    # start of paket marker = spm
    spm_length = 14

    # solve
    spm_index = calculate_spm_index_optimized(characters, spm_length)

    # result
    result = spm_index

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


# loop through characters and check if there is a sequence of characters with length = spm_length
def calculate_spm_index(characters, spm_length):

    for i in range(0, len(characters)-spm_length+1):
        distinct_characters_length = len(set(characters[i:i+spm_length]))
        if distinct_characters_length == spm_length:
            spm_index = i + spm_length
            return spm_index


# Use knowledge about the amount of distinct characters to skip loops
# Example: spm_length = 14, distinct characters 10: Skip 3 loops
# because there cannot be sequence of 14 distinct characters in the next 8 loops because it needs at least these 8 loops
# to remove the duplicates

# (1) 1.31 ms -> 1.35 ms ( 101 loops skipped) 1575 -> 1474 ( 6% reduction of loops) but slower/same because of offset calculation
# (2) 1.56 ms -> 0.43 ms (1782 loops skipped) 2165 ->  383 (82% reduction of loops)
def calculate_spm_index_optimized(characters, spm_length):

    offset = 0
    for i in range(0, len(characters) - spm_length + 1):
        i += offset
        distinct_characters_length = len(set(characters[i:i + spm_length]))
        if distinct_characters_length == spm_length:
            spm_index = i + spm_length
            return spm_index
        offset += spm_length - distinct_characters_length - 1




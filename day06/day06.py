import time

DAY_STR = "06"


def solve_day06():

    solve_day06_1()
    solve_day06_2()


def solve_day06_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    characters = lines[0]
    # start of paket marker = spm
    spm_length = 4

    # solve
    spm_index = calculate_spm_index(characters, spm_length)

    # result
    result = spm_index

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day06_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
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

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


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
# Time complexity: O(len(characters)*spm_length)
def calculate_spm_index_optimized(characters, spm_length):

    offset = 0
    for i in range(0, len(characters) - spm_length + 1):
        i += offset
        distinct_characters_length = len(set(characters[i:i + spm_length]))
        if distinct_characters_length == spm_length:
            spm_index = i + spm_length
            return spm_index
        offset += spm_length - distinct_characters_length - 1


# Use knowledge about limited alphabet
# Time complexity: O(len(characters))
def calculate_spm_index_optimized_time_complexity(characters, spm_length):

    # define alphabet dict
    unique_characters = set(characters)
    dict_alphabet = {}
    for character in unique_characters:
        dict_alphabet.update({str(character): 0})

    # define counter of duplicates
    duplicates = 0

    # add the first spm_length characters to the dict and update duplicates
    for character in characters[:spm_length]:
        dict_alphabet[character] += 1
        if dict_alphabet[character] >= 2:
            duplicates += 1

    # now always add new character and delete oldest one till duplicates == 0
    for index, character in enumerate(characters[spm_length:]):

        # remove oldest character
        dict_alphabet[characters[index]] -= 1
        # update duplicates
        if dict_alphabet[characters[index]] >= 1:
            duplicates -= 1

        # add new character
        dict_alphabet[character] += 1
        # update duplicates
        if dict_alphabet[character] >= 2:
            duplicates += 1

        if duplicates == 0:
            return index + 1 + spm_length


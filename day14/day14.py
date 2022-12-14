import time

DAY_STR = "14"


def solve_day14():

    solve_day14_1()
    solve_day14_2()


def solve_day14_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    len_sand = -1
    start_sand = (500, 0)
    sand_set = set()
    sand_set.add(start_sand)

    # convert to list of Rock
    rock_set = parse_rocks(lines)

    max_y = max(rock_set, key=lambda item: item[1])[1]

    # simulate grains of sand falling
    while len_sand < len(sand_set):
        len_sand = len(sand_set)
        falling_grain_of_sand = (500, 0)
        # while sand falling
        while True:
            # if sand falls into abyss
            if falling_grain_of_sand[1] + 1 > max_y:
                break
            # if path blocked below
            if (falling_grain_of_sand[0], falling_grain_of_sand[1] + 1) in rock_set or (falling_grain_of_sand[0], falling_grain_of_sand[1] + 1) in sand_set:
                # if path blocked below left
                if (falling_grain_of_sand[0] - 1, falling_grain_of_sand[1] + 1) in rock_set or (falling_grain_of_sand[0] - 1, falling_grain_of_sand[1] + 1) in sand_set:
                    # if path blocked below right
                    if (falling_grain_of_sand[0] + 1, falling_grain_of_sand[1] + 1) in rock_set or (falling_grain_of_sand[0] + 1, falling_grain_of_sand[1] + 1) in sand_set:
                        # sand fully blocked -> rest
                        sand_set.add(falling_grain_of_sand)
                        break
                    # fall further down right
                    else:
                        falling_grain_of_sand = falling_grain_of_sand[0] + 1, falling_grain_of_sand[1] + 1

                # fall further down left
                else:
                    falling_grain_of_sand = falling_grain_of_sand[0] - 1, falling_grain_of_sand[1] + 1
            # fall further down
            else:
                falling_grain_of_sand = falling_grain_of_sand[0], falling_grain_of_sand[1]+1

    # result
    # - 1 because starting_point also included in sand_set -> we do not reach because falling into abyss -> #todo restructure
    result = len(sand_set) - 1

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day14_2():
    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()
    # print(lines)

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    len_sand = -1
    start_sand = (500, 0)
    sand_set = set()
    sand_set.add(start_sand)

    # convert to list of Rock
    rock_set = parse_rocks(lines)

    max_y = max(rock_set, key=lambda item: item[1])[1] + 2

    # simulate grains of sand falling
    while len_sand < len(sand_set):
        len_sand = len(sand_set)
        falling_grain_of_sand = (500, 0)
        # while sand falling
        while True:
            # if bottom reached -> rest
            if falling_grain_of_sand[1]+1 == max_y:
                sand_set.add(falling_grain_of_sand)
                break
            # if path blocked below
            if (falling_grain_of_sand[0], falling_grain_of_sand[1] + 1) in rock_set or (falling_grain_of_sand[0], falling_grain_of_sand[1] + 1) in sand_set:
                # if path blocked below left
                if (falling_grain_of_sand[0] - 1, falling_grain_of_sand[1] + 1) in rock_set or (falling_grain_of_sand[0] - 1, falling_grain_of_sand[1] + 1) in sand_set:
                    # if path blocked below right
                    if (falling_grain_of_sand[0] + 1, falling_grain_of_sand[1] + 1) in rock_set or (falling_grain_of_sand[0] + 1, falling_grain_of_sand[1] + 1) in sand_set:
                        # sand fully blocked -> rest
                        sand_set.add(falling_grain_of_sand)
                        break
                    # fall further down right
                    else:
                        falling_grain_of_sand = falling_grain_of_sand[0] + 1, falling_grain_of_sand[1] + 1
                # fall further down left
                else:
                    falling_grain_of_sand = falling_grain_of_sand[0] - 1, falling_grain_of_sand[1] + 1
            # fall further down
            else:
                falling_grain_of_sand = falling_grain_of_sand[0], falling_grain_of_sand[1] + 1

    # result
    result = len(sand_set)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def parse_rocks(lines):

    rock_set = set()

    for rock_chain_str in lines:
        rock_chain_list = [tuple(map(int, x.split(","))) for x in rock_chain_str.split(" -> ")]
        for index in range(len(rock_chain_list)-1):
            rock_set.update(get_single_rocks_from_chain(rock_chain_list[index], rock_chain_list[index + 1]))
    return rock_set


def get_single_rocks_from_chain(rock_chain_start, rock_chain_end):

    single_rocks = []

    if rock_chain_start[0] == rock_chain_end[0]:
        if rock_chain_start[1] < rock_chain_end[1]:
            for i in range(rock_chain_start[1], rock_chain_end[1] + 1):
                single_rocks.append((rock_chain_start[0], i))
        else:
            for i in range(rock_chain_end[1], rock_chain_start[1] + 1):
                single_rocks.append((rock_chain_start[0], i))

    else:
        if rock_chain_start[0] < rock_chain_end[0]:
            for i in range(rock_chain_start[0], rock_chain_end[0] + 1):
                single_rocks.append((i, rock_chain_start[1]))
        else:
            for i in range(rock_chain_end[0], rock_chain_start[0] + 1):
                single_rocks.append((i, rock_chain_start[1]))

    return single_rocks


# everything below just for visualizing

def print_map(rock_set, sand_set):

    map_size = get_map_size(rock_set, sand_set)

    for y in range(map_size[1][0], map_size[1][1] + 1):
        for x in range(map_size[0][0], map_size[0][1] + 1):
            if (x, y) in rock_set:
                print("#", end="")
            elif (x, y) == (500, 0):
                print("+", end="")
            elif (x, y) in sand_set:
                print("o", end="")
            else:
                print(".", end="")
        print("")
    print(map_size)


def get_map_size(rock_set, sand_set):

    if sand_set:
        max_x = max(max(rock_set, key=lambda item: item[0])[0], max(sand_set, key=lambda item: item[0])[0])
        max_y = max(max(rock_set, key=lambda item: item[1])[1], max(sand_set, key=lambda item: item[1])[1])
        min_x = min(min(rock_set, key=lambda item: item[0])[0], min(sand_set, key=lambda item: item[0])[0])
        min_y = min(min(rock_set, key=lambda item: item[1])[1], min(sand_set, key=lambda item: item[1])[1])
    else:
        max_x = max(rock_set, key=lambda item: item[0])[0]
        max_y = max(rock_set, key=lambda item: item[1])[1]
        min_x = min(rock_set, key=lambda item: item[0])[0]
        min_y = min(rock_set, key=lambda item: item[1])[1]

    return [(min_x, max_x), (min_y, max_y)]

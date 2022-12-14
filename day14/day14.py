import time

DAY_STR = "14"


def solve_day14():
    solve_day14_1()
    solve_day14_2()


# further optimization possible: memorize path of sand and then start not from the top
def solve_day14_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    map_dict = {}
    len_dict = -1

    # fill map_dict with rocks from input
    parse_rocks(lines, map_dict)

    max_y = max(map_dict, key=lambda item: item[1])[1]

    # simulate grains of sand falling
    while len_dict < len(map_dict):

        len_dict = len(map_dict)

        # falling grain of sand
        sand_grain = (500, 0)

        # while sand falling
        while True:
            # if sand falls into abyss
            if sand_grain[1] + 1 > max_y:
                break

            # if path blocked below
            if (sand_grain[0], sand_grain[1] + 1) in map_dict:

                # if path blocked below left
                if (sand_grain[0] - 1, sand_grain[1] + 1) in map_dict:

                    # if path blocked below right
                    if (sand_grain[0] + 1, sand_grain[1] + 1) in map_dict:

                        # sand fully blocked -> rest
                        map_dict[sand_grain] = "o"
                        break

                    # fall further down right
                    else:
                        sand_grain = sand_grain[0] + 1, sand_grain[1] + 1

                # fall further down left
                else:
                    sand_grain = sand_grain[0] - 1, sand_grain[1] + 1

            # fall further down
            else:
                sand_grain = sand_grain[0], sand_grain[1] + 1

    # result
    result = sum(1 for v in map_dict.values() if v == "o")

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day14_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    map_dict = {}

    # fill map_dict with rocks from input
    parse_rocks(lines, map_dict)

    max_y = max(map_dict, key=lambda item: item[1])[1]

    drop_from(500, 0, map_dict, max_y)

    # result
    result = sum(1 for v in map_dict.values() if v == "o")

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def drop_from(x, y, map_dict, max_y):

    if (x, y) in map_dict or y >= max_y + 2:
        return
    for dx in [0, -1, 1]:
        drop_from(x + dx, y + 1, map_dict, max_y)
    map_dict[(x, y)] = "o"


def parse_rocks(lines, map_dict):

    for rock_chain_str in lines:
        rock_chain_list = [tuple(map(int, x.split(","))) for x in rock_chain_str.split(" -> ")]
        for index in range(len(rock_chain_list)-1):
            put_rocks_into_dict(rock_chain_list[index], rock_chain_list[index + 1], map_dict)


def put_rocks_into_dict(rock_chain_start, rock_chain_end, map_dict):

    if rock_chain_start[0] == rock_chain_end[0]:
        if rock_chain_start[1] < rock_chain_end[1]:
            for i in range(rock_chain_start[1], rock_chain_end[1] + 1):
                if (rock_chain_start[0], i) not in map_dict:
                    map_dict[(rock_chain_start[0], i)] = "#"
        else:
            for i in range(rock_chain_end[1], rock_chain_start[1] + 1):
                if (rock_chain_start[0], i) not in map_dict:
                    map_dict[(rock_chain_start[0], i)] = "#"

    else:
        if rock_chain_start[0] < rock_chain_end[0]:
            for i in range(rock_chain_start[0], rock_chain_end[0] + 1):
                if (i, rock_chain_start[1]) not in map_dict:
                    map_dict[(i, rock_chain_start[1])] = "#"
        else:
            for i in range(rock_chain_end[0], rock_chain_start[0] + 1):
                if (i, rock_chain_start[1]) not in map_dict:
                    map_dict[(i, rock_chain_start[1])] = "#"


# everything below just for visualizing

def print_map(map_dict):

    map_size = get_map_size(map_dict)
    for y in range(map_size[1][0], map_size[1][1] + 1):
        for x in range(map_size[0][0], map_size[0][1] + 1):
            if (x, y) in map_dict:
                print(map_dict[(x, y)], end="")
            else:
                print(".", end="")
        print("")


def get_map_size(map_dict):

    max_x = max(map_dict, key=lambda item: item[0])[0]
    max_y = max(map_dict, key=lambda item: item[1])[1]
    min_x = min(map_dict, key=lambda item: item[0])[0]
    min_y = min(map_dict, key=lambda item: item[1])[1]

    return [(min_x, max_x), (min_y, max_y)]

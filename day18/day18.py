import time
import re

DAY_STR = "18"


def solve_day18():
    solve_day18_1()
    solve_day18_2()


NEIGHBORS = lambda x, y, z: {(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)}


def solve_day18_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    lava_dict = parse_input(lines)

    # solve
    result = get_surface_area(lava_dict)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day18_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    lava_dict = parse_input(lines)

    # solve
    result = get_surface_area_water(lava_dict)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def parse_input(lines):

    lava_dict = dict()

    for line in lines:
        lava_dict[tuple(map(int, re.findall(r'\d+|-\d+', line)))] = "#"

    return lava_dict


def get_surface_area(lava_dict):

    surface_area = 0

    for e in lava_dict:
        surface_area += get_surface_area_pixel(lava_dict, e[0], e[1], e[2])

    return surface_area


def get_surface_area_pixel(lava_dict, x, y, z):

    surface_area = 0

    for neighbor in NEIGHBORS(x, y, z):
        if neighbor not in lava_dict:
            surface_area += 1

    return surface_area


def get_surface_area_water(lava_dict):

    def fill_water_dict(location):
        x, y, z = location
        water_dict[location] = "@"
        for neighbor in NEIGHBORS(x, y, z):
            if neighbor not in water_dict and neighbor not in lava_dict and not out_of_bounds(neighbor):
                queue.add(neighbor)

    def out_of_bounds(location):
        x, y, z = location
        if x < min_x or x > max_x or y < min_y or y > max_y or z < min_z or z > max_z:
            return True
        else:
            return False

    min_x, min_y, min_z, max_x, max_y, max_z = get_lava_dict_size(lava_dict)

    # map size but every min/max coordinate - 1/ + 1 to let water flow around
    water_dict_size = (min_x - 1, min_y - 1, min_z - 1, max_x + 1, max_y + 1, max_z + 1)

    min_x, min_y, min_z, max_x, max_y, max_z = water_dict_size

    # starting point to fill water:
    starting_point = (max_x, max_y, max_z)
    queue = set()
    queue.add(starting_point)

    water_dict = dict()
    while queue:
        fill_water_dict(queue.pop())

    surface_area = 0
    for elem in lava_dict:
        surface_area += get_surface_area_pixel_part2(lava_dict, water_dict, elem)

    return surface_area


# don't count area that touches water
def get_surface_area_pixel_part2(lava_dict, water_dict, location):

    x, y, z = location

    surface_area = 0
    for neighbor in NEIGHBORS(x, y, z):
        if neighbor not in lava_dict and neighbor in water_dict:
            surface_area += 1

    return surface_area


def get_lava_dict_size(lava_dict):

    min_x = min(lava_dict, key=lambda item: item[0])[0]
    min_y = min(lava_dict, key=lambda item: item[1])[1]
    min_z = min(lava_dict, key=lambda item: item[2])[2]

    max_x = max(lava_dict, key=lambda item: item[0])[0]
    max_y = max(lava_dict, key=lambda item: item[1])[1]
    max_z = max(lava_dict, key=lambda item: item[2])[2]

    return min_x, min_y, min_z, max_x, max_y, max_z

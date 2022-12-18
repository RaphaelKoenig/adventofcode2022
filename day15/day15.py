import sys
import time
import re
from tqdm import tqdm

DAY_STR = "15"


def solve_day15():

    solve_day15_1()
    solve_day15_2()


def solve_day15_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    sensors = []
    beacons = []
    distances = []
    # input:
    y = 2000000
    # test input:
    # y = 10

    # parses input
    for line in lines:
        sensor, beacon, distance = parse_input(line)
        sensors.append(sensor)
        beacons.append(beacon)
        distances.append(distance)

    result = solve_part_01(sensors, distances, beacons, y)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day15_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()
    # print(lines)

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    sensors = []
    beacons = []
    distances = []
    # input:
    location = [0, 4000000]

    # parses input
    for line in lines:
        sensor, beacon, distance = parse_input(line)
        sensors.append(sensor)
        beacons.append(beacon)
        distances.append(distance)

    # solve
    result = solve_part_02(location, distances, sensors)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_part_01(sensors, distances, beacons, y):

    result = 0
    x_skip_total = 0
    max_size = get_map_size(sensors, distances)
    for x in tqdm(range(max_size[0][0], max_size[0][1] + 1), desc='Day 15 (1) Progress Bar'):
        x += x_skip_total
        if x > max_size[0][1]:
            break

        result_increased = False
        x_skip = 0
        for index, sensor in enumerate(sensors):
            if get_distance(sensor, (x, y)) <= distances[index]:
                if not result_increased:
                    result += 1
                    result_increased = True
                if x_skip < distances[index] - get_distance(sensor, (x, y)):
                    x_skip = distances[index] - get_distance(sensor, (x, y))
        x_skip_total += x_skip

    # filter beacons out of result
    for beacon in set(beacons):
        if beacon[1] == 2000000:
            result -= 1

    # filter sensors out of result
    for sensor in set(sensors):
        if sensor[1] == 2000000:
            result -= 1

    # add all the skipped locations
    result += x_skip_total
    return result


def solve_part_02(location, distances, sensors):

    # iterate through every row
    for x in tqdm(range(location[0], location[1]+1), desc='Day 15 (2) Progress Bar'):

        y_skip_total = 0

        # iterate through every column

        for y in range(location[0], location[1]+1):

            # skip columns where beacon cannot be
            y += y_skip_total

            # if y outside of range
            if y > location[1]:
                break

            y_skip = 0
            finish = True

            # check for every sensor if (x,y)  location is in range
            for index, sensor in enumerate(sensors):

                # if (x,y) is in range, get sensor with distance to beacon which is much longer than distance to current (x,y) (longest skip distance)
                # Example:  Only one sensor at 0,0 with distance to closest beacon = 10
                #           current (x,y) = (1,1)
                #           distance (x,y) -> sensor = 2 ((0,0) to (1,1))
                #           10 - 2 = 8 -> next y is not 2 but 2+8 = 11.
                #           skipped y = 2,3,4,5,6,7,8,9,10 and continues at (1,11)

                if get_distance(sensor, (x, y)) <= distances[index]:
                    finish = False

                    # get maximum of all skip distances
                    if y_skip < distances[index] - get_distance(sensor, (x, y)):
                        y_skip = distances[index] - get_distance(sensor, (x, y))

            # (x,y) not in range, solution found
            if finish:
                return x*4000000+y
            y_skip_total += y_skip


def parse_input(line):

    sensor = tuple(map(int, re.findall(r'\d+|-\d+', line)[:2]))
    beacon = tuple(map(int, re.findall(r'\d+|-\d+', line)[2:4]))
    distance = get_distance(sensor, beacon)

    return sensor, beacon, distance


def get_distance(point_1, point_2):

    return abs(point_1[0]-point_2[0]) + abs(point_1[1]-point_2[1])


def get_map_size(sensors, distances):

    max_x = max_y = -sys.maxsize
    min_x = min_y = sys.maxsize

    for index, sensor in enumerate(sensors):
        if max_x < sensor[0] + distances[index]:
            max_x = sensor[0] + distances[index]
        if max_y < sensor[1] + distances[index]:
            max_y = sensor[1] + distances[index]
        if min_x > sensor[0] - distances[index]:
            min_x = sensor[0] - distances[index]
        if min_y > sensor[1] - distances[index]:
            min_y = sensor[1] - distances[index]

    return [(min_x, max_x), (min_y, max_y)]


# everything below just for visualizing


def print_map(sensors, beacons, distances, map_size):

    for y in range(map_size[1][0], map_size[1][1] + 1):
        for x in range(map_size[0][0], map_size[0][1] + 1):
            cannot_contain = False
            for index, sensor in enumerate(sensors):
                if get_distance(sensor, (x, y)) <= distances[index]:
                    cannot_contain = True
                    break

            if (x, y) in sensors:
                print("S", end="")
            elif (x, y) in beacons:
                print("B", end="")
            elif cannot_contain:
                print("#", end="")
            else:
                print(".", end="")
        print("")




import copy
import functools
import time
import re
from functools import reduce

DAY_STR = "19"


def solve_day19():

    # solve_day19_1()
    solve_day19_2()


def solve_day19_1():

    @functools.lru_cache(maxsize=None)
    def max_geode(blueprint, robots, resources, minute):

        max_geode.counter += 1

        if minute > 9:
            build_0 = False
        else:
            build_0 = resources[0] >= blueprint[0]

        if minute > 18:
            build_1 = False
        else:
            build_1 = resources[0] >= blueprint[1]

        if minute > 21:
            build_2 = False
        else:
            build_2 = resources[0] >= blueprint[2][0] and resources[1] >= blueprint[2][1]

        build_3 = resources[0] >= blueprint[3][0] and resources[2] >= blueprint[3][1]

        if minute == 24:
            resources = calculate_produced_resources(robots, resources)
            return resources[3]
        else:

            resources = calculate_produced_resources(robots, resources)

            if build_0:
                robots_0 = (robots[0] + 1, robots[1], robots[2], robots[3])
                resources_0 = (resources[0] - blueprint[0], resources[1], resources[2], resources[3])
            if build_1:
                robots_1 = (robots[0], robots[1] + 1, robots[2], robots[3])
                resources_1 = (resources[0] - blueprint[1], resources[1], resources[2], resources[3])
            if build_2:
                robots_2 = (robots[0], robots[1], robots[2] + 1, robots[3])
                resources_2 = (resources[0] - blueprint[2][0], resources[1] - blueprint[2][1], resources[2], resources[3])
            if build_3:
                robots_3 = (robots[0], robots[1], robots[2], robots[3] + 1)
                resources_3 = (resources[0] - blueprint[3][0], resources[1], resources[2] - blueprint[3][1], resources[3])

            if build_0 and build_1 and build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))
            if build_0 and build_1 and build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1))
            if build_0 and build_1 and not build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))
            if build_0 and not build_1 and build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))
            if not build_0 and build_1 and build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))

            if build_0 and build_1 and not build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1))
            if build_0 and not build_1 and build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1))
            if build_0 and not build_1 and not build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))
            if not build_0 and build_1 and build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1))
            if not build_0 and build_1 and not build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))
            if not build_0 and not build_1 and build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))

            if build_0 and not build_1 and not build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1))
            if not build_0 and build_1 and not build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1))
            if not build_0 and not build_1 and build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1))
            if not build_0 and not build_1 and not build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))

            if not build_0 and not build_1 and not build_2 and not build_3:
                return max_geode(blueprint, robots, resources, minute + 1)
            else:
                raise RuntimeError('something is very wrong')

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # define variables
    blueprints = parse_input(lines)
    robots = (1, 0, 0, 0)
    resources = (0, 0, 0, 0)

    max_geode_list = list()
    for index, blueprint in enumerate(blueprints):
        max_geode.counter = 0
        geodes_found = max_geode(blueprint, robots, resources, 1)
        max_geode_list.append(geodes_found*(index+1))

    # result
    result = sum(max_geode_list)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day19_2():

    @functools.lru_cache(maxsize=None)
    def max_geode(blueprint, robots, resources, minute):

        if minute > 11:
            build_0 = False
        else:
            build_0 = resources[0] >= blueprint[0]

        if minute > 20:
            build_1 = False
        else:
            build_1 = resources[0] >= blueprint[1]

        if minute > 25:
            build_2 = False
        else:
            build_2 = resources[0] >= blueprint[2][0] and resources[1] >= blueprint[2][1]

        build_3 = resources[0] >= blueprint[3][0] and resources[2] >= blueprint[3][1]

        if minute == 32:
            resources = calculate_produced_resources(robots, resources)
            return resources[3]
        else:
            resources = calculate_produced_resources(robots, resources)

            if build_0:
                robots_0 = (robots[0] + 1, robots[1], robots[2], robots[3])
                resources_0 = (resources[0] - blueprint[0], resources[1], resources[2], resources[3])
            if build_1:
                robots_1 = (robots[0], robots[1] + 1, robots[2], robots[3])
                resources_1 = (resources[0] - blueprint[1], resources[1], resources[2], resources[3])
            if build_2:
                robots_2 = (robots[0], robots[1], robots[2] + 1, robots[3])
                resources_2 = (
                resources[0] - blueprint[2][0], resources[1] - blueprint[2][1], resources[2], resources[3])
            if build_3:
                robots_3 = (robots[0], robots[1], robots[2], robots[3] + 1)
                resources_3 = (
                resources[0] - blueprint[3][0], resources[1], resources[2] - blueprint[3][1], resources[3])
            if build_0 and build_1 and build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))
            if build_0 and build_1 and build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1))
            if build_0 and build_1 and not build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))
            if build_0 and not build_1 and build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))
            if not build_0 and build_1 and build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))

            if build_0 and build_1 and not build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1))
            if build_0 and not build_1 and build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1))
            if build_0 and not build_1 and not build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))
            if not build_0 and build_1 and build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1))
            if not build_0 and build_1 and not build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))
            if not build_0 and not build_1 and build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))

            if build_0 and not build_1 and not build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_0, resources_0, minute + 1))
            if not build_0 and build_1 and not build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_1, resources_1, minute + 1))
            if not build_0 and not build_1 and build_2 and not build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_2, resources_2, minute + 1))
            if not build_0 and not build_1 and not build_2 and build_3:
                return max(
                    max_geode(blueprint, robots, resources, minute + 1),
                    max_geode(blueprint, robots_3, resources_3, minute + 1))

            if not build_0 and not build_1 and not build_2 and not build_3:
                return max_geode(blueprint, robots, resources, minute + 1)
            else:
                raise RuntimeError('something is very wrong')

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # define variables
    blueprints = parse_input(lines)[:3]
    robots = (1, 0, 0, 0)
    resources = (0, 0, 0, 0)

    max_geode_list = list()
    for index, blueprint in enumerate(blueprints):
        geodes_found = max_geode(blueprint, robots, resources, 1)
        max_geode_list.append(geodes_found)

    # result
    result = reduce((lambda x, y: x * y), max_geode_list)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def parse_input(lines):
    blueprints = []
    for blueprint_str in lines:
        blueprint_int = list(map(int, re.findall(r'\d+', blueprint_str)))
        blueprint = (
                        blueprint_int[1],
                        blueprint_int[2],
                        (blueprint_int[3], blueprint_int[4]),
                        (blueprint_int[5], blueprint_int[6])
                    )
        blueprints.append(blueprint)
    return blueprints


def calculate_produced_resources(robots, resources):

    return tuple(x + y for x, y in zip(robots, resources))

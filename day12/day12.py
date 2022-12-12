import time

import networkx as nx

day_str = "12"


def solve_day12():

    solve_day12_1()
    solve_day12_2()


def solve_day12_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    start_node = -1
    end_node = -1

    directed_graph = nx.DiGraph()

    # solve
    for index_row, row in enumerate(lines):
        for index_column, column in enumerate(row):

            # get start and end node
            if column == "S":
                start_node = index_row * len(row) + index_column
            if column == "E":
                end_node = index_row * len(row) + index_column

            # add nodes and edges
            suited_neighbors = get_suited_adjacent_neighbors(lines, index_row, index_column)
            if suited_neighbors:
                for neighbor in suited_neighbors:
                    directed_graph.add_edge(index_row * len(row) + index_column, neighbor)

    # result
    result = (nx.shortest_path_length(directed_graph, start_node, end_node))

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def solve_day12_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    result = 0
    start_node = -1
    a_nodes = []
    end_node = - 1

    directed_graph = nx.DiGraph()

    # solve
    for index_row, row in enumerate(lines):
        for index_column, column in enumerate(row):

            # get "a" nodes and end node
            if column == "a":
                a_nodes.append(index_row * len(row) + index_column)
            if column == "E":
                end_node = index_row * len(row) + index_column

            # add edges
            suited_neighbors = get_suited_adjacent_neighbors(lines, index_row, index_column)
            if suited_neighbors:
                for neighbor in suited_neighbors:
                    directed_graph.add_edge(index_row * len(row) + index_column, neighbor)

    # optimization:
    #   do not calculate the shortest path for all individual a's to the end node E
    # instead:
    #   add edges  from new starting Node S (-1) -> a's and search just one shortest path from S to E - 1
    for a in a_nodes:
        directed_graph.add_edge(start_node, a)

    # result
    result = (nx.shortest_path_length(directed_graph, start_node, end_node) - 1)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def get_suited_adjacent_neighbors(lines, index_row, index_column):

    neighbors = []
    column = lines[index_row][index_column]
    row = lines[index_row]
    # right
    if index_column < len(row) - 1:
        if HEIGHTS[lines[index_row][index_column + 1]] <= HEIGHTS[column] + 1:
            neighbors.append(index_row * len(row) + index_column + 1)
    # left
    if index_column > 0:
        if HEIGHTS[lines[index_row][index_column - 1]] <= HEIGHTS[column] + 1:
            neighbors.append(index_row * len(row) + index_column - 1)
    # down
    if index_row < len(lines) - 1:
        if HEIGHTS[lines[index_row + 1][index_column]] <= HEIGHTS[column] + 1:
            neighbors.append((index_row + 1) * len(row) + index_column)
    # up
    if index_row > 0:
        if HEIGHTS[lines[index_row - 1][index_column]] <= HEIGHTS[column] + 1:
            neighbors.append((index_row - 1) * len(row) + index_column)

        return neighbors


HEIGHTS = {
    "S": 0,
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
    "E": 25,
}

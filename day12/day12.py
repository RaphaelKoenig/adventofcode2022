import time

DAY_STR = "12"


def solve_day12():
    solve_day12_1()
    solve_day12_2()


def solve_day12_1():
    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    graph = {}
    start_node = -1
    end_node = -1

    # solve
    for index_row, row in enumerate(lines):
        for index_column, column in enumerate(row):

            node_id = calculate_id(index_row, index_column, lines)

            # get start and end node
            if column == "S":
                start_node = index_row * len(row) + index_column
            if column == "E":
                end_node = index_row * len(row) + index_column

            # add nodes and edges
            suited_neighbors = suited_adjacent_neighbors(lines, index_row, index_column)

            for neighbor in suited_neighbors:
                if node_id in graph:
                    graph[node_id].add(neighbor)
                else:
                    graph[node_id] = {neighbor}

    # result
    result = length_shortest_path(graph, start_node, end_node)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result,
                                                                   round((end_time - start_time) * 1000, 2)))


def solve_day12_2():
    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    graph = {}
    start_node = -1
    end_node = - 1
    a_nodes = []

    # solve
    for index_row, row in enumerate(lines):
        for index_column, column in enumerate(row):

            node_id = calculate_id(index_row, index_column, lines)

            # get "a" nodes and end node
            if column == "a":
                a_nodes.append(node_id)
            if column == "E":
                end_node = node_id

            # add edges
            suited_neighbors = suited_adjacent_neighbors(lines, index_row, index_column)

            for neighbor in suited_neighbors:
                if node_id in graph:
                    graph[node_id].add(neighbor)
                else:
                    graph[node_id] = {neighbor}

    # optimization:
    #   do not calculate the shortest path for all individual a's to the end node E
    # instead:
    #   add edges  from new starting Node S (-1) -> a's and search just one shortest path from S to E - 1
    for a in a_nodes:
        if start_node in graph:
            graph[start_node].add(a)
        else:
            graph[start_node] = {a}

    # result
    result = length_shortest_path(graph, start_node, end_node) - 1

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result,
                                                                   round((end_time - start_time) * 1000, 2)))


def suited_adjacent_neighbors(lines, index_row, index_column):
    # current column
    column = lines[index_row][index_column]

    neighbors = adjacent_neighbors(lines, index_row, index_column)
    if neighbors:
        neighbors_suited = filter_suited_neighbors(neighbors, column)
        return neighbors_suited
    else:
        return []


def adjacent_neighbors(lines, index_row, index_column):
    neighbors = []
    # current row
    row = lines[index_row]

    # right
    if index_column < len(row) - 1:
        neighbors.append((index_row * len(row) + index_column + 1, lines[index_row][index_column + 1]))
    # left
    if index_column > 0:
        neighbors.append((index_row * len(row) + index_column - 1, lines[index_row][index_column - 1]))
    # down
    if index_row < len(lines) - 1:
        neighbors.append((((index_row + 1) * len(row) + index_column), lines[index_row + 1][index_column]))
    # up
    if index_row > 0:
        neighbors.append((((index_row - 1) * len(row) + index_column), lines[index_row - 1][index_column]))

    return neighbors


def filter_suited_neighbors(neighbors, column):
    suited_neighbors = [x[0] for x in neighbors if HEIGHTS[x[1]] <= HEIGHTS[column] + 1]
    return suited_neighbors


def calculate_id(index_row, index_column, lines):
    return index_row * len(lines[index_row]) + index_column


def length_shortest_path(graph, start_node, end_node):

    path_list = [[start_node]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {start_node}
    if start_node == end_node:
        return 1

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if end_node in next_nodes:
            return len(current_path)
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return -1


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

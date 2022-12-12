import time

DAY_STR = "08"


def solve_day08():

    solve_day08_1()
    solve_day08_2()


def solve_day08_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # solve
    tree_map = fill_map_visibility(lines)

    mark_visible_trees(tree_map)

    # result
    result = get_number_visible_trees(tree_map)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day08_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # solve
    tree_map = fill_map_scenic_scores(lines)

    calculate_scenic_scores(tree_map)

    # result
    result = get_max_scenic_score(tree_map)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def fill_map_visibility(lines):

    row_int, column_int = len(lines), len(lines[0])
    tree_map = [[(0, False) for x in range(column_int)] for y in range(row_int)]
    for index_row, row_str in enumerate(lines):
        for index_column, tree in enumerate(row_str):
            tree_map[index_row][index_column] = (int(tree), False)
    return tree_map


def fill_map_scenic_scores(lines):

    row_int, column_int = len(lines), len(lines[0])
    tree_map = [[(0, False) for x in range(column_int)] for y in range(row_int)]
    for index_row, row_str in enumerate(lines):
        for index_column, tree in enumerate(row_str):
            tree_map[index_row][index_column] = (int(tree), 0)
    return tree_map


def mark_visible_trees(tree_map):

    # mark rows
    for index_row in range(len(tree_map)):

        # front to back
        highest_tree = -1
        for index_column in range(len(tree_map[0])):
            if tree_map[index_row][index_column][0] > highest_tree:
                tree_map[index_row][index_column] = (tree_map[index_row][index_column][0], True)
                highest_tree = tree_map[index_row][index_column][0]

        # back to front
        highest_tree = -1
        for index_column in range(len(tree_map[0])-1, -1, -1):
            if tree_map[index_row][index_column][0] > highest_tree:
                tree_map[index_row][index_column] = (tree_map[index_row][index_column][0], True)
                highest_tree = tree_map[index_row][index_column][0]

    # mark columns
    for index_column in range(len(tree_map[0])):

        # up to down
        highest_tree = -1
        for index_row in range(len(tree_map)):
            if tree_map[index_row][index_column][0] > highest_tree:
                tree_map[index_row][index_column] = (tree_map[index_row][index_column][0], True)
                highest_tree = tree_map[index_row][index_column][0]

        # down to up
        highest_tree = -1
        for index_row in range(len(tree_map)-1, -1, -1):
            if tree_map[index_row][index_column][0] > highest_tree:
                tree_map[index_row][index_column] = (tree_map[index_row][index_column][0], True)
                highest_tree = tree_map[index_row][index_column][0]


def get_number_visible_trees(tree_map):

    result = 0
    for index_row in range(len(tree_map)):
        for index_column in range(len(tree_map[0])):
            if tree_map[index_row][index_column][1]:
                result += 1

    return result


def calculate_scenic_scores(tree_map):

    for index_row in range(len(tree_map)):
        for index_column in range(len(tree_map[0])):
            calculate_scenic_score(index_row, index_column, tree_map)


def calculate_scenic_score(tree_row, tree_column, tree_map):

    tree_height = tree_map[tree_row][tree_column][0]

    # calculate scenic score

    # scenic score right:
    scenic_score_right = 0
    for index_column in range(tree_column+1, len(tree_map[0])):
        scenic_score_right += 1
        if tree_map[tree_row][index_column][0] >= tree_height:
            break

    # scenic score left
    scenic_score_left = 0
    for index_column in range(tree_column-1, -1, -1):
        scenic_score_left += 1
        if tree_map[tree_row][index_column][0] >= tree_height:
            break

    # scenic score down
    scenic_score_down = 0
    for index_row in range(tree_row+1, len(tree_map)):
        scenic_score_down += 1
        if tree_map[index_row][tree_column][0] >= tree_height:
            break

    # scenic score up
    scenic_score_up = 0
    for index_row in range(tree_row-1, -1, -1):
        scenic_score_up += 1
        if tree_map[index_row][tree_column][0] >= tree_height:
            break

    scenic_score = scenic_score_right*scenic_score_left*scenic_score_down*scenic_score_up

    tree_map[tree_row][tree_column] = (tree_map[tree_row][tree_column][0], scenic_score)


def get_max_scenic_score(tree_map):

    result = 0
    for index_row in range(len(tree_map)):
        for index_column in range(len(tree_map[0])):
            if tree_map[index_row][index_column][1] > result:
                result = tree_map[index_row][index_column][1]

    return result


def print_map_trees(tree_map):

    for index_row in range(len(tree_map)):
        for index_column in range(len(tree_map[0])):
            # bold if tree is visible
            if tree_map[index_row][index_column][1]:
                print("\033[1m" + str(tree_map[index_row][index_column][0]) + "\033[0m" + " ", end='')
            else:
                print(str(tree_map[index_row][index_column][0]) + " ", end='')
        print("")


def print_map_tuples(tree_map):

    for index_row in range(len(tree_map)):
        for index_column in range(len(tree_map[0])):
            # bold if tree is visible
            print(str(tree_map[index_row][index_column]), end='')
        print("")
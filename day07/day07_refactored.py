import time

DAY_STR = "07"


def solve_day07():

    solve_day07_1()
    solve_day07_2()


class Tree(object):
    def __init__(self, name, parent, size):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = size

    def __repr__(self):
        return self.name + " " + str(self.size)

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


def solve_day07_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # define variables
    root_tree = Tree("root", [], 0)

    directories = {"/root": 0}
    total_size_10000 = 0

    # solve
    fill_directories_from_input(lines, directories)
    fill_directory_tree_from_input(lines, root_tree)

    update_sizes(root_tree)

    print(root_tree.children)

    for Dir in directories:
        if directories[Dir] < 100000:
            total_size_10000 += directories[Dir]

    # result
    result = total_size_10000

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day07_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()
    # print(lines)

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]
    # print(lines)

    # define variables
    directories = {"/root": 0}

    # solve
    fill_directories_from_input(lines, directories)

    # print(directories)

    threshold = directories["/root"] - 40000000
    candidates = []
    for Dir in directories:
        if threshold <= directories[Dir]:
            candidates.append(directories[Dir])

    # result
    result = min(candidates)

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def fill_directories_from_input(lines, directories):

    for line in lines:

        # executed commands
        if line[0] == "$":

            if line[2:4] == "cd":

                if line[5:6] == "/":
                    current = "/root"

                elif line[5:7] == "..":
                    current = current[0:current.rfind("/")]

                else:
                    current = current + "/" + (line[5:])
                    directories.update({current: 0})
                    # move in a level

            elif line[2:4] == "ls":
                pass

        # dir does not do anything
        elif line[0:3] == "dir":
            pass

        # size of files
        else:
            amount = int(line[:line.find(" ")])
            dict_loc = current

            for i in range(current.count("/")):
                directories[dict_loc] += amount
                dict_loc = dict_loc[:dict_loc.rfind("/")]


def fill_directory_tree_from_input(lines, root_tree):

    for line in lines:

        # executed commands
        if line[0] == "$":

            if line[2:4] == "cd":

                if line[5:6] == "/":
                    current_tree = root_tree

                elif line[5:7] == "..":
                    current_tree = current_tree.parent
                else:
                    child_tree = Tree((line[5:]), current_tree, 0)
                    current_tree.add_child(child_tree)
                    current_tree = child_tree
                    # move in a level

            elif line[2:4] == "ls":
                pass

        # dir does not do anything
        elif line[0:3] == "dir":
            pass

        # size of files
        else:
            current_tree.size += int(line[:line.find(" ")])


def update_sizes(tree):
    if len(tree.children) > 0:
        for child in tree.children:
            update_sizes(child)
    else:
        tree.parent.size += tree.size
        print(tree)

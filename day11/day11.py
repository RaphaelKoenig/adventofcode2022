import copy
import time
import numpy

day_str = "11"


class Monkey(object):

    def __init__(self, id):
        self.id = id
        self.items = []
        self.operation = lambda x: x
        self.test = 0
        self.true = 0
        self.false = 0
        self.inspected_items = 0

    def __repr__(self):
        return "Monkey " + str(self.id) + "\n" \
               + "  Items: " + str(self.items) + "\n" + "  Operation: " + str(self.operation(2)) + "\n" \
               + "  Test: divisible by " + str(self.test) + "\n" + "    If  true: throw to Monkey " + str(self.true) \
               + "\n" + "    If false: throw to Monkey " + str(self.false) + "\n" + "  Inspected items: " \
               + str(self.inspected_items)

    def get_id(self):
        return self.id

    def add_item(self, item):
        self.items.append(item)

    def update_item(self, item, index):
        self.items[index] = item

    def get_items(self):
        return self.items

    def empty_items(self):
        self.items = []

    def set_operation(self, operation):
        self.operation = operation

    def get_operation(self):
        return self.operation

    def get_test(self):
        return self.test

    def set_test(self, test):
        self.test = test

    def get_true(self):
        return self.true

    def set_true(self, true):
        self.true = true

    def get_false(self):
        return self.false

    def set_false(self, false):
        self.false = false

    def increase_inspected_items(self):
        self.inspected_items += 1

    def get_inspected_items(self):
        return self.inspected_items


def solve_day11():

    solve_day11_1()
    solve_day11_2()


def solve_day11_1():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # solve
    monkeys = parse_input(lines)

    for round_ in range(1, 21):
        # print("Round: " + str(round_))

        for monkey in monkeys:
            for index_item, item in enumerate(monkey.get_items()):
                # print("  Monkey " + str(monkey.get_id()) + " inspects an item with worry level of " + str(item))
                monkey.increase_inspected_items()
                execute_operation(index_item, monkey)
                throw_item(index_item, monkey, monkeys)
            monkey.empty_items()

    # result
    inspected_items = []
    for monkey in monkeys:
        inspected_items.append(monkey.get_inspected_items())

    result = (sorted(inspected_items, reverse=True))[0] * (sorted(inspected_items, reverse=True))[1]

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(day_str, result,
                                                                   round((end_time - start_time) * 1000, 2)))


def solve_day11_2():

    # start execution time
    start_time = time.perf_counter()

    # read input file
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    lines = [x.strip() for x in lines]

    # solve
    monkeys = parse_input(lines)
    lcm = get_lcm(monkeys)

    for round_ in range(1, 10001):
        # print("Round: " + str(round_))

        for monkey in monkeys:

            for index_item, _ in enumerate(monkey.get_items()):
                # print("  Monkey " + str(monkey.get_id()) + " inspects an item with worry level of " + str(item))
                monkey.increase_inspected_items()
                execute_operation_part2(index_item, monkey, lcm)
                throw_item(index_item, monkey, monkeys)
            monkey.empty_items()

    # result
    inspected_items = sorted([monkey.get_inspected_items() for monkey in monkeys], reverse=True)
    result = inspected_items[0] * inspected_items[1]

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(day_str, result,
                                                                   round((end_time - start_time) * 1000, 2)))


def parse_input(lines):

    monkeys = list()
    for line in lines:
        if "Monkey" in line:
            monkey = Monkey(int(line[:-1].split(" ")[1]))
        elif "Starting items: " in line:
            starting_items = list(map(int, line[line.find(":") + 1:].split(",")))
            for item in starting_items:
                monkey.add_item(item)
        elif "Operation: " in line:
            operation = line[line.find("old") + 4:]
            if operation[2:] == "old":
                operation = lambda x: x * x
            elif operation[0] == "*":
                value = int(operation[2:])
                operation = lambda x, y = value: x * y
            elif operation[0] == "+":
                value = int(operation[2:])
                operation = lambda x, y = value: x + y
            else:
                raise RuntimeError('Unexpected symbol while parsing operation')
            monkey.set_operation(operation)
        elif "Test: " in line:
            test = int(line[line.find("by") + 3:])
            monkey.set_test(test)
        elif "true" in line:
            true = int(line[line.find("monkey") + 7:])
            monkey.set_true(true)
        elif "false" in line:
            false = int(line[line.find("monkey") + 7:])
            monkey.set_false(false)
        elif line == "":
            monkeys.append(monkey)
        else:
            raise RuntimeError('Unexpected line while parsing')
    monkeys.append(monkey)
    return monkeys


def execute_operation(index_item, monkey):

    worry_level = monkey.get_items()[index_item]
    worry_level_old = worry_level
    worry_level = monkey.get_operation()(worry_level)
    # print("    Worry level changes from " + str(worry_level_old) + " to " + str(worry_level)
    #       + " (Operation: " + "str(monkey.get_operation())" + ")")

    worry_level = worry_level // 3
    monkey.update_item(worry_level, index_item)
    # print("    Monkey gets bored with item. Worry level is divided by 3 to  " + str(worry_level))


def execute_operation_part2(index_item, monkey, lcm):

    worry_level = monkey.get_operation()(monkey.get_items()[index_item])
    worry_level = worry_level % lcm
    monkey.update_item(worry_level, index_item)


def throw_item(index_item, monkey, monkeys):

    if monkey.get_items()[index_item] % monkey.get_test() == 0:
        # print("    Current worry level is divisible by " + str(monkey.get_test()) + ".")
        monkeys[monkey.get_true()].add_item(monkey.get_items()[index_item])
        # print("    Item with worry level " + str(monkey.get_items()[index_item]) + " is thrown to monkey " + str(monkey.get_true()))
    else:
        # print("    Current worry level is not divisible by " + str(monkey.get_test()) + ".")
        monkeys[monkey.get_false()].add_item(monkey.get_items()[index_item])
        # print("    Item with worry level " + str(monkey.get_items()[index_item]) + " is thrown to monkey " + str(monkey.get_false()))


def get_lcm(monkeys):

    dividers = []
    for monkey in monkeys:
        dividers.append(monkey.get_test())
    lcm = numpy.lcm.reduce(dividers)
    return int(lcm)

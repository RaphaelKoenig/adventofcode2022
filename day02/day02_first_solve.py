#first_solved
import time

day_str = "02"

def solve_day02():
    solve_day02_1()
    solve_day02_2()


def solve_day02_1():

    def calculate_points_of_game(me, opponent):
        points_me = 0
        if me == "X":
            points_me+=1
        elif me == "Y":
            points_me+=2
        elif me == "Z":
            points_me+=3
        else:
            raise RuntimeError('Fehler')
        points_opponent = 0

        if opponent == "A":
            points_opponent += 1
        elif opponent == "B":
            points_opponent += 2
        elif opponent == "C":
            points_opponent += 3
        else:
            raise RuntimeError('Fehler1')

        if opponent == "A" and me == "X" or opponent == "B" and me == "Y" or opponent == "C" and me == "Z":
            points_me += 3
            points_opponent += 3
        elif opponent == "A" and me == "Z" or opponent == "B" and me == "X" or opponent == "C" and me == "Y":
            points_me += 0
            points_opponent += 6
        elif opponent == "A" and me == "Y" or opponent == "B" and me == "Z" or opponent == "C" and me == "X":
            points_me += 6
            points_opponent += 0
        else:
            raise RuntimeError('Fehler2')

        return points_me, points_opponent

    # start execution time
    start_time = time.perf_counter()

    # read file Using readlines()
    input_file = open('day' + day_str + '/input.txt', 'r')
    lines = input_file.readlines()
    # print(lines)

    # remove \n and whitespaces
    lines = [x.replace("\n", "").strip() for x in lines]
    # print(lines)

    # define variables
    points_me_all_games = 0

    for line in lines:
        opponent, me = line.split(" ")
        points_me, point_opponent = calculate_points_of_game(me, opponent)
        points_me_all_games += points_me
        # print(points_me, point_opponent)

    # result
    result = points_me_all_games

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def solve_day02_2():

    def calculate_points_of_game(me, opponent):
        points_me = 0
        if me == "X":
            points_me += 0
        elif me == "Y":
            points_me += 3
        elif me == "Z":
            points_me += 6
        else:
            raise RuntimeError('Fehler2')
        points_opponent = 0

        if (opponent == "A" and me == "Y") or (opponent == "B" and me == "X") or (opponent == "C" and me == "Z"):
            points_me += 1
        elif (opponent == "A" and me == "Z") or (opponent == "B" and me == "Y") or (opponent == "C" and me == "X"):
            points_me += 2
        elif (opponent == "A" and me == "X") or (opponent == "B" and me == "Z") or (opponent == "C" and me == "Y"):
            points_me += 3
        else:
            raise RuntimeError('Fehler3')

        return points_me, points_opponent

    # start execution time
    start_time = time.perf_counter()

    # read file Using readlines()
    input_file = open('day' + day_str + '/input.txt', 'r')
    lines = input_file.readlines()
    # print(lines)

    # remove \n and whitespaces
    lines = [x.replace("\n", "").strip() for x in lines]
    # print(lines)

    # define variables
    points_me_all_games = 0

    for line in lines:
        opponent, me = line.split(" ")
        points_me, point_opponent = calculate_points_of_game(me, opponent)
        points_me_all_games += points_me
        # print(points_me, point_opponent)

    # result
    result = points_me_all_games

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))
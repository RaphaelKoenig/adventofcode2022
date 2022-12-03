# refactored version
import time

day_str = "02"


def solve_day02():
    solve_day02_1()
    solve_day02_2()
    # solve_day02_short()
    # solve_day02_shortest()


# day02_1

# A, X = Rock
# B, Y = Paper
# C, Z = Scissors

# Games in form: 'A Y' which translates to 'player1 chooses Rock and player2 choose Paper'
# Rock > Scissors, Paper > Rock, Scissors > Paper
# Score: 0 for Loss, 3 for Draw, 6 for Win + 1 for Rock, 2 for Paper, 3 for Scissors
# result: sum scores of all games for player2 (me)


# day02_2

# X/Y/Z means that player2 haha to lose/draw/win
# A/B/C still Rock/Paper/Scissors
# Games in form: 'A Y' which translates to 'player1 chooses Rock and player2 has to Draw, so player2 has to choose Rock as well'
# Score: same as in day02_1'
# result: sum scores of all games for player2 (me)

def solve_day02_1():

    # start execution time
    start_time = time.perf_counter()

    # read file using readlines()
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    games = [x.strip() for x in lines]

    # define variables
    game_scores = {"A X": 1 + 3, "A Y": 2 + 6, "A Z": 3 + 0,
                   "B X": 1 + 0, "B Y": 2 + 3, "B Z": 3 + 6,
                   "C X": 1 + 6, "C Y": 2 + 0, "C Z": 3 + 3}
    total_score = 0

    for game in games:
        total_score += game_scores[game]

    # result = sum scores of all games for player2 (me)
    result = total_score

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def solve_day02_2():

    # start execution time
    start_time = time.perf_counter()

    # read file using readlines()
    input_file = open('day' + day_str + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    games = [x.strip() for x in lines]

    # define variables
    game_scores = {"A X": 3 + 0, "A Y": 1 + 3, "A Z": 2 + 6,
                   "B X": 1 + 0, "B Y": 2 + 3, "B Z": 3 + 6,
                   "C X": 2 + 0, "C Y": 3 + 3, "C Z": 1 + 6}
    total_score = 0

    # sum scores for every game (player2/me)
    for game in games:
        total_score += game_scores[game]

    # result = sum scores of all games for player2 (me)
    result = total_score

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(day_str, result, round((end_time - start_time) * 1000, 2)))


def solve_day02_short():

    games = [x.replace("\n", "") for x in open('day02/input.txt').readlines()]
    game_scores_1 = {"A X": 1 + 3, "A Y": 2 + 6, "A Z": 3 + 0, "B X": 1 + 0, "B Y": 2 + 3, "B Z": 3 + 6, "C X": 1 + 6, "C Y": 2 + 0, "C Z": 3 + 3}
    game_scores_2 = {"A X": 3 + 0, "A Y": 1 + 3, "A Z": 2 + 6, "B X": 1 + 0, "B Y": 2 + 3, "B Z": 3 + 6, "C X": 2 + 0, "C Y": 3 + 3, "C Z": 1 + 6}
    result_1 = sum([game_scores_1[x] for x in games])
    result_2 = sum([game_scores_2[x] for x in games])

    print(result_1, result_2)


def solve_day02_shortest():

    game_scores_1 = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
    game_scores_2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
    print(sum([game_scores_1[x] for x in [x.replace("\n", "") for x in open('day02/input.txt').readlines()]]))
    print(sum([game_scores_2[x] for x in [x.replace("\n", "") for x in open('day02/input.txt').readlines()]]))


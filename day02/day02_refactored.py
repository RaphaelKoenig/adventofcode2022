# refactored version
import time

DAY_STR = "02"


def solve_day02():

    solve_day02_1()
    solve_day02_2()


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

    # calculate score of game for player2 (me)
    def calculate_score_of_game(player1_shape, player2_shape):

        score_player2 = 0

        # calculate score of Rock = 1, Paper = 2, Scissors = 3
        if player2_shape == "X":
            score_player2 += 1
        elif player2_shape == "Y":
            score_player2 += 2
        elif player2_shape == "Z":
            score_player2 += 3
        else:
            raise RuntimeError('Score calculation Rock/Paper/Scissors failed')

        # calculate score of Loss = 0, Draw = 3, Win = 6
        if player1_shape == "A" and player2_shape == "Z" or player1_shape == "B" and player2_shape == "X" or player1_shape == "C" and player2_shape == "Y":
            score_player2 += 0
        elif player1_shape == "A" and player2_shape == "X" or player1_shape == "B" and player2_shape == "Y" or player1_shape == "C" and player2_shape == "Z":
            score_player2 += 3
        elif player1_shape == "A" and player2_shape == "Y" or player1_shape == "B" and player2_shape == "Z" or player1_shape == "C" and player2_shape == "X":
            score_player2 += 6
        else:
            raise RuntimeError('Score calculation Loss/Draw/Win failed')

        return score_player2

    # start execution time
    start_time = time.perf_counter()

    # read file using readlines()
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    games = [x.strip() for x in lines]

    # define variables
    score_player2_all_games = 0

    for game in games:
        player1_shape, player2_shape = game.split(" ")
        score_player2 = calculate_score_of_game(player1_shape, player2_shape)
        score_player2_all_games += score_player2

    # result = sum scores of all games for player2 (me)
    result = score_player2_all_games

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (1) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))


def solve_day02_2():

    # calculate score of game for player2 (me)
    def calculate_score_of_game(player1_shape, outcome):

        score_player2 = 0
        if outcome == "X":
            score_player2 += 0
        elif outcome == "Y":
            score_player2 += 3
        elif outcome == "Z":
            score_player2 += 6
        else:
            raise RuntimeError('Score calculation Loss/Draw/Win failed')

        if (player1_shape == "A" and outcome == "Y") or (player1_shape == "B" and outcome == "X") or (player1_shape == "C" and outcome == "Z"):
            score_player2 += 1
        elif (player1_shape == "A" and outcome == "Z") or (player1_shape == "B" and outcome == "Y") or (player1_shape == "C" and outcome == "X"):
            score_player2 += 2
        elif (player1_shape == "A" and outcome == "X") or (player1_shape == "B" and outcome == "Z") or (player1_shape == "C" and outcome == "Y"):
            score_player2 += 3
        else:
            raise RuntimeError('Score calculation Rock/Paper/Scissors failed')

        return score_player2

    # start execution time
    start_time = time.perf_counter()

    # read file using readlines()
    input_file = open('day' + DAY_STR + '/input.txt')
    lines = input_file.readlines()

    # remove \n and whitespaces
    games = [x.strip() for x in lines]

    # define variables
    score_player2_all_games = 0

    # sum scores for every game (player2/me)
    for game in games:
        player1_shape, outcome = game.split(" ")
        score_player2 = calculate_score_of_game(player1_shape, outcome)
        score_player2_all_games += score_player2

    # result = sum scores of all games for player2 (me)
    result = score_player2_all_games

    # stop execution time
    end_time = time.perf_counter()

    print('Day {} (2) solution: {} (execution time: {} ms)'.format(DAY_STR, result, round((end_time - start_time) * 1000, 2)))
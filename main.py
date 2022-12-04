from day01.day01 import solve_day01
from day02.day02 import solve_day02
from day03.day03 import solve_day03
from day04.day04 import solve_day04


def solve_all():
    solve_day01()  # solution (1): 66186 (1.06 ms) | (2): 196804 (0.99 ms)
    solve_day02()  # solution (1): 14264 (1.73 ms) | (2):  12382 (1.66 ms) #optimized to 0.85 ms
    solve_day03()  # solution (1):  8394 (0.92 ms) | (2):   2413 (0.72 ms)
    solve_day04()  # solution (1):  567  (2.01 ms) | (2):    907 (2.62 ms)


if __name__ == '__main__':
    solve_all()

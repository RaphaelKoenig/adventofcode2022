from day01.day01 import solve_day01
from day02.day02 import solve_day02
from day03.day03 import solve_day03
from day04.day04 import solve_day04
from day05.day05 import solve_day05
from day06.day06 import solve_day06


def solve_all():
    solve_day01()  # solution (1):      66186 (1.06 ms) | (2):    196804 (0.99 ms)
    solve_day02()  # solution (1):      14264 (0.85 ms) | (2):     12382 (0.85 ms) #      optimized from 1.75 ms
    solve_day03()  # solution (1):       8394 (0.92 ms) | (2):      2413 (0.72 ms)
    solve_day04()  # solution (1):        567 (2.01 ms) | (2):       907 (2.62 ms)
    solve_day05()  # solution (1):  FCVRLMVQP (2.04 ms) | (2): RWLWGJGFD (2.08 ms) # both optimized to    1.5 ms
    solve_day06()  # solution (1):       1578 (1.31 ms) | (2):      2178 (0.43 ms) # (2)  optimized from 1.56 ms


if __name__ == '__main__':
    solve_all()

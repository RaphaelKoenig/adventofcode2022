from day01.day01 import solve_day01
from day02.day02 import solve_day02
from day03.day03 import solve_day03
from day04.day04 import solve_day04
from day05.day05 import solve_day05
from day06.day06 import solve_day06
from day07.day07 import solve_day07
from day08.day08 import solve_day08
from day09.day09 import solve_day09
from day10.day10 import solve_day10
from day11.day11 import solve_day11
from day12.day12 import solve_day12
from day13.day13 import solve_day13
from day14.day14 import solve_day14


def solve_all():
    solve_day01()  # solution (1):     66186 ( 1.06 ms) | (2):      196804 (   0.99 ms)
    solve_day02()  # solution (1):     14264 ( 0.85 ms) | (2):       12382 (   0.85 ms) # both optimized from 1.75 ms
    solve_day03()  # solution (1):      8394 ( 0.92 ms) | (2):        2413 (   0.72 ms)
    solve_day04()  # solution (1):       567 ( 2.01 ms) | (2):         907 (   2.62 ms)
    solve_day05()  # solution (1): FCVRLMVQP ( 2.04 ms) | (2):   RWLWGJGFD (   2.08 ms) # both optimized to    1.5 ms
    solve_day06()  # solution (1):      1578 ( 1.31 ms) | (2):        2178 (   0.43 ms) # (2)  optimized from 1.56 ms
    solve_day07()  # solution (1):     95437 ( 0.15 ms) | (2):    24933642 (   0.11 ms)
    solve_day08()  # solution (1):      1854 ( 6.58 ms) | (2):      527340 (  25.62 ms)
    solve_day09()  # solution (1):      6339 (20.04 ms) | (2):        2541 (  63.89 ms) # optimized from 70ms | 321ms
    solve_day10()  # solution (1):     11220 ( 0.23 ms) | (2):    BZPAJELK (   0.72 ms)
    solve_day11()  # solution (1):    113232 ( 2.32 ms) | (2): 29703395016 (1124.62 ms) # (2) optimized from 1.4s
    solve_day12()  # solution (1):       370 (11.83 ms) | (2):         363 (  11.11 ms) # (2) optimized from 786 ms
    solve_day13()  # solution (1):      5557 (18.57 ms) | (2):       22425 (  22.71 ms)
    solve_day14()  # solution (1):       913 (61.24 ms) | (2):       30762 (2398.28 ms)


if __name__ == '__main__':
    solve_all()


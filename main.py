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
from day15.day15 import solve_day15
from day16.day16 import solve_day16
from day17.day17 import solve_day17
from day18.day18 import solve_day18
from day19.day19 import solve_day19
from day20.day20 import solve_day20
from day21.day21 import solve_day21
from day22.day22 import solve_day22


def solve_all():
    solve_day01()  # solution (1):           66186 (  1.06 ms) | (2):         196804 (   0.99 ms)
    solve_day02()  # solution (1):           14264 (  0.85 ms) | (2):          12382 (   0.85 ms) # both optimized from 1.75 ms
    solve_day03()  # solution (1):            8394 (  0.92 ms) | (2):           2413 (   0.72 ms)
    solve_day04()  # solution (1):             567 (  2.01 ms) | (2):            907 (   2.62 ms)
    solve_day05()  # solution (1):       FCVRLMVQP (  2.04 ms) | (2):      RWLWGJGFD (   2.08 ms) # both optimized to    1.5 ms
    solve_day06()  # solution (1):            1578 (  1.31 ms) | (2):           2178 (   0.43 ms) # (2)  optimized from 1.56 ms
    solve_day07()  # solution (1):           95437 (  0.15 ms) | (2):       24933642 (   0.11 ms)
    solve_day08()  # solution (1):            1854 (  6.58 ms) | (2):         527340 (  25.62 ms)
    solve_day09()  # solution (1):            6339 ( 20.04 ms) | (2):           2541 (  63.89 ms) # optimized from 70ms | 321ms
    solve_day10()  # solution (1):           11220 (  0.23 ms) | (2):       BZPAJELK (   0.72 ms)
    solve_day11()  # solution (1):          113232 (  2.32 ms) | (2):    29703395016 ( 118.62 ms) # (2) optimized from 1400 ms (pypy)
    solve_day12()  # solution (1):             370 ( 11.83 ms) | (2):            363 (  11.11 ms) # (2) optimized from 786 ms
    solve_day13()  # solution (1):            5557 ( 18.57 ms) | (2):          22425 (  22.71 ms)
    solve_day14()  # solution (1):             913 ( 41.96 ms) | (2):          30762 (  30.58 ms) # optimized from 61 ms | 2400 ms
    solve_day15()  # solution (1):         5299855 (565.17 ms) | (2): 13615843289729 (    11.5 s) # (pypy)
    solve_day16()  # solution (1):            1327 (537.58 ms) | (2):           2520 (          ) # (cached)
    solve_day17()  # solution (1):            3166 (  1     s) | (2):  1577207977186 (          )
    solve_day18()  # solution (1):            3496 (  6.25 ms) | (2):           2064 (  28.28 ms)
    solve_day19()  # solution (1):            817  (  10.5  s) | (2):           4216 ( 335     s) # (pypy) (cached)
    solve_day20()  # solution (1):            2203 ( 39.48 ms) | (2):  6641234038999 ( 408.38 ms) # (pypy)
    solve_day21()  # solution (1): 286698846151845 (  4.65 ms) | (2):  3759566892641 (   1.1   s) # (pypy)
    solve_day22()  # solution (1):          106094 ( 56.26 ms) |

if __name__ == '__main__':
    # solve_all()
    solve_day22()
import time


from chess import *
from solve import *


def solve_knights_bishops(m, n):
    start = time.time()
    board = Board(m, n)
    best_solution = solve(board, start, place_knight=True, place_bishop=True, debug=True)
    return best_solution
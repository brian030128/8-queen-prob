import time


from chess import *
from solve import *


def max_knights(m, n):
    start = time.time()
    board = Board(m, n)
    best_solution = solve(board, start, place_knight=True, debug=True)
    return best_solution
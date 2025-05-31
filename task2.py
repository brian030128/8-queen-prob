import time


from chess import *
from solve import *

def max_bishops(m, n):
    start = time.time()
    board = Board(m, n)
    best_solution = solve(board, start, place_bishop=True, debug=True)
    return best_solution
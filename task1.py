import time

from chess import *
from solve import *

def max_queens(m, n):
    start = time.time()
    board = Board(m, n)
    best_solution = solve(board, start, place_queen=True, debug=True)
    return best_solution


if __name__ == "__main__":
    result = max_queens(8, 8)
    print(result.board.print_board())
    result, msg = validate_chess_placement(result.board)
    print("✅" if result else "❌", msg)

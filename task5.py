import copy
import sys 
import time

from chess import *


class Solution:
    def __init__(self, board: Board, score: int):
        self.board = copy.deepcopy(board)
        self.score = score
        self.diverse_score = board.diverse_score()


def solve(board: Board, start = None, place_queen=False, place_knight=False, place_bishop=False, best_solution: Solution = None, score=0):
    if start is None:
        start = time.time()
    if best_solution is None:
        best_solution = Solution(board, score)
    for r in range(board.m):
        for c in range(board.n):
            if place_queen and board.can_place(r, c, 'Q'):
                board.place_piece(r, c, 'Q')
                best_solution = solve(board, start, True, False, False, best_solution, score + 1)
                board.remove_piece(r, c)
            if place_knight and board.can_place(r, c, 'N'):
                board.place_piece(r, c, 'N')
                best_solution = solve(board, start, False, True, False, best_solution, score + 1)
                board.remove_piece(r, c)
            if place_bishop and board.can_place(r, c, 'B'):
                board.place_piece(r, c, 'B')
                best_solution = solve(board, start, False, False, True, best_solution, score + 1)
                board.remove_piece(r, c)
            
            if score > best_solution.score or (score == best_solution.score and board.diverse_score() > best_solution.diverse_score):
                best_solution = Solution(board, score)
                print(f"Found better solution: {score} {board.diverse_score()} in {time.time() - start} seconds")
                best_solution.board.print_board()
    
    return best_solution


def solve_knights_bishops_with_queens(m, n, queen_positions):
    board = Board(m, n, queen_positions)

    best_solution = solve(board, place_knight=True, place_bishop=True)
    best_solution.board.print_board()




if __name__ == "__main__":
    # increase max recursion limit
    sys.setrecursionlimit(10000)
    result = solve_knights_bishops_with_queens(8, 8, [(0, 0), (2, 3)])
    print("Total:", result["total"])
    print("bishops:", result["bishops"])
    print("knights:", result["knights"])

    board = Board(8, 8, [(0, 0), (2, 3)], result["bishops"], result["knights"])
    board.print_board() 
    valid, message = validate_chess_placement(board)
    print("✅" if valid else "❌", message)
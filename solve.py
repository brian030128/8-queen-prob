import sys 
import time
import copy

from chess import *


class Solution:
    def __init__(self, board: Board, score: int):
        # copy is necessary because the board is a reference, and will be modified in the solve function
        self.board = copy.deepcopy(board)
        self.score = score
        self.diverse_score = board.diverse_score()

class Result:
    def __init__(self, solution: Solution):
        self.queen_positions = []
        self.knight_positions = []
        self.bishop_positions = []
        self.total = solution.score
        board = solution.board

        for r in range(board.m):
            for c in range(board.n):
                if board.board[r][c] == 'Q':
                    self.queen_positions.append((r, c))
                elif board.board[r][c] == 'N':
                    self.knight_positions.append((r, c))
                elif board.board[r][c] == 'B':
                    self.bishop_positions.append((r, c))
        self.total = solution.score
        

def solve(board: Board, start=None, r=0, c=0, place_queen=False, place_knight=False, place_bishop=False, best_solution: Solution = None, score=0, debug=True):
    if start is None:
        start = time.time()

    if best_solution is None:
        best_solution = Solution(board, score)
    # Recursive terminate condition
    if r == board.m:
        if score > best_solution.score or (score == best_solution.score and board.diverse_score() > best_solution.diverse_score):
            best_solution = Solution(board, score)
            if debug:
                print(f"Found better solution: {score} {board.diverse_score()} in {time.time() - start} seconds")
                best_solution.board.print_board()
        return best_solution

    # Early termination - if we can't possibly beat the current best
    remaining_cells = (board.m - r) * board.n - c
    if score + remaining_cells < best_solution.score:
        return best_solution



    next_r, next_c = (r, c + 1) if c + 1 < board.n else (r + 1, 0)

    # Try pieces in order of potential value (queens typically most valuable)
    pieces_to_try = []
    if place_queen and board.can_place(r, c, 'Q'):
        pieces_to_try.append('Q')
    if place_knight and board.can_place(r, c, 'N'):
        pieces_to_try.append('N')
    if place_bishop and board.can_place(r, c, 'B'):
        pieces_to_try.append('B')
    
    # Try placing pieces
    for piece in pieces_to_try:
        board.place_piece(r, c, piece)
        best_solution = solve(board, start, r=next_r, c=next_c, score=score + 1, 
                            best_solution=best_solution, place_queen=place_queen, 
                            place_knight=place_knight, place_bishop=place_bishop, debug=debug)
        board.remove_piece(r, c)

    
    # Try placing nothing
    best_solution = solve(board, start, r=next_r, c=next_c, score=score, 
                        best_solution=best_solution, place_queen=place_queen, 
                        place_knight=place_knight, place_bishop=place_bishop, debug=debug)
    
    return best_solution

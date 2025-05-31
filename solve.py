import copy
import sys 
import time

from chess import *


class Solution:
    def __init__(self, board: Board, score: int):
        self.board = copy.deepcopy(board)
        self.score = score
        self.diverse_score = board.diverse_score()

class Result:
    def __init__(self, solution: Solution):
        self.queen_positions = []
        self.knight_positions = []
        self.bishop_positions = []
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


def solve(board: Board, start, r=0, c=0, place_queen=False, place_knight=False, place_bishop=False, best_solution: Solution = None, score=0, debug=True):
    if best_solution is None:
        best_solution = Solution(board, score)

    if r == board.m:
        if score > best_solution.score or (score == best_solution.score and board.diverse_score() > best_solution.diverse_score):
            best_solution = Solution(board, score)
            if debug:
                print(f"Found better solution: {score} {board.diverse_score()} in {time.time() - start} seconds")
                best_solution.board.print_board()
        return best_solution

    next_r, next_c = (r, c + 1) if c + 1 < board.n else (r + 1, 0)

    # Try placing nothing
    best_solution = solve(board, start, r=next_r, c=next_c, score=score, best_solution=best_solution, place_queen=place_queen, place_knight=place_knight, place_bishop=place_bishop)
    # Try placing a queen
    if place_queen and board.can_place(r, c, 'Q'):
        board.place_piece(r, c, 'Q')
        best_solution = solve(board, start, r=next_r, c=next_c, score=score + 1, best_solution=best_solution, place_queen=place_queen, place_knight=place_knight, place_bishop=place_bishop)
        board.remove_piece(r, c)
    if place_knight and board.can_place(r, c, 'N'):
        board.place_piece(r, c, 'N')
        best_solution = solve(board, start, r=next_r, c=next_c, score=score + 1, best_solution=best_solution, place_queen=place_queen, place_knight=place_knight, place_bishop=place_bishop)
        board.remove_piece(r, c)
    if place_bishop and board.can_place(r, c, 'B'):
        board.place_piece(r, c, 'B')
        best_solution = solve(board, start, r=next_r, c=next_c, score=score + 1, best_solution=best_solution, place_queen=place_queen, place_knight=place_knight, place_bishop=place_bishop)
        board.remove_piece(r, c)
    
    return best_solution

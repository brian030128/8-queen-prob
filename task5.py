from chess import *
from solve import *

def solve_knights_bishops_with_queens(m, n, queen_positions):
    board = Board(m, n, queen_positions)

    best_solution = solve(board, time.time(), place_queen=False, place_knight=True, place_bishop=True)

    return best_solution


if __name__ == "__main__":
    solution = solve_knights_bishops_with_queens(8, 8, [(0, 0), (2, 3)])
    result = Result(solution)
    print("Total:", result.total)
    print("bishops:", result.bishop_positions)
    print("knights:", result.knight_positions)

    board = solution.board  
    board.print_board() 
    valid, message = validate_chess_placement(board)
    print("✅" if valid else "❌", message)
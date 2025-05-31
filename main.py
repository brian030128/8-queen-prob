import sys
import ast

from chess import *
from solve import *
from task1 import max_queens
from task2 import max_bishops
from task3 import max_knights
from task4 import solve_knights_bishops
from task5 import solve_knights_bishops_with_queens

def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <task_id> <m> <n> [<queen_positions>]")
        return

    task_id = int(sys.argv[1])
    m = int(sys.argv[2])
    n = int(sys.argv[3])

    if task_id == 1:
        res = Result(max_queens(m, n))
        print(f"合計置入棋子數量： {res.total}")
        print(f"皇后位置： {res.queen_positions}")
    elif task_id == 2:
        res = Result(max_bishops(m, n))
        print(f"合計置入棋子數量： {res.total}")
        print(f"主教位置： {res.bishop_positions}")
    elif task_id == 3:
        res = Result(max_knights(m, n))
        print(f"合計置入棋子數量： {res.total}")
        print(f"騎士位置： {res.knight_positions}")
    elif task_id == 4:
        bishops, knights = solve_knights_bishops(m, n)
        print(f"Total: {len(bishops) + len(knights)}")
        print("Bishops:", bishops)
        print("Knights:", knights)
    elif task_id == 5:
        if len(sys.argv) < 5:
            print("Task 5 requires a list of queen positions")
            return
        queens = ast.literal_eval(sys.argv[4])
        bishops, knights = solve_knights_bishops_with_queens(m, n, queens)
        print(f"Total: {len(bishops) + len(knights)}")
        print("Bishops:", bishops)
        print("Knights:", knights)
    else:
        print("Invalid task_id (must be 1–5)")

if __name__ == "__main__":
    main()

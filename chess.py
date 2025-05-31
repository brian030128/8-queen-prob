queen_dirs = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
# Knight moves
knight_dirs = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]
# Bishop moves
bishop_dirs = [(-1,-1), (-1,1), (1,-1), (1,1)]



class Board:
    def __init__(self, m, n, queen_positions = [], bishop_positions = [], knight_positions = []):
        self.m = m
        self.n = n
        # check the positions do not overlap in the same list
        if len(set(queen_positions)) != len(queen_positions):
            raise ValueError("Queen positions overlap")
        if len(set(bishop_positions)) != len(bishop_positions):
            raise ValueError("Bishop positions overlap")
        if len(set(knight_positions)) != len(knight_positions):
            raise ValueError("Knight positions overlap")
        # check the positions do not overlap between the three lists
        if len(set(queen_positions) & set(bishop_positions)) > 0:
            raise ValueError("Queen and Bishop positions overlap")
        if len(set(queen_positions) & set(knight_positions)) > 0:
            raise ValueError("Queen and Knight positions overlap")
        if len(set(bishop_positions) & set(knight_positions)) > 0:
            raise ValueError("Bishop and Knight positions overlap")
        
        self.board = [['.' for _ in range(n)] for _ in range(m)]
        self.attack_board = [[False for _ in range(n)] for _ in range(m)]
        self.queen_positions = queen_positions
        self.bishop_positions = bishop_positions
        self.knight_positions = knight_positions
        for r, c in queen_positions:
            self.board[r][c] = 'Q'
            self.mark_attacks(r, c, 'Q')
        for r, c in bishop_positions:
            self.board[r][c] = 'B'
            self.mark_attacks(r, c, 'B')
        for r, c in knight_positions:
            self.board[r][c] = 'N'
            self.mark_attacks(r, c, 'N')
    
    def mark_attacks(self, r, c, piece):
        if piece == 'Q':
            for dr, dc in queen_dirs:
                rr, cc = r + dr, c + dc
                while 0 <= rr < self.m and 0 <= cc < self.n:
                    self.attack_board[rr][cc] = True
                    rr += dr
                    cc += dc
        elif piece == 'B':
            for dr, dc in bishop_dirs:
                rr, cc = r + dr, c + dc
                while 0 <= rr < self.m and 0 <= cc < self.n:
                    self.attack_board[rr][cc] = True
                    rr += dr
                    cc += dc
        elif piece == 'N':
            for dr, dc in knight_dirs:
                rr, cc = r + dr, c + dc
                if 0 <= rr < self.m and 0 <= cc < self.n:
                    self.attack_board[rr][cc] = True

    def place_piece(self, r, c, piece):
        self.board[r][c] = piece
        self.mark_attacks(r, c, piece)

    def print_board(self):
        for row in self.board:
            print(' '.join(row))


def can_place(board: Board, r, c, piece):
    if piece == 'Q':
        for dr, dc in queen_dirs:
            rr, cc = r + dr, c + dc
            while 0 <= rr < board.m and 0 <= cc < board.n:
                if board.board[rr][cc] != '.':
                    return False
                rr += dr
                cc += dc
    elif piece == 'B':
        for dr, dc in bishop_dirs:
            rr, cc = r + dr, c + dc
            while 0 <= rr < board.m and 0 <= cc < board.n:
                if board.board[rr][cc] != '.':
                    return False
                rr += dr
                cc += dc
    elif piece == 'N':
        for dr, dc in knight_dirs:
            rr, cc = r + dr, c + dc
            if 0 <= rr < board.m and 0 <= cc < board.n:
                if board.board[rr][cc] != '.':
                    return False
    return True


def validate_chess_placement(board: Board):
    for r in range(board.m):
        for c in range(board.n):
            if board.attack_board[r][c] and board.board[r][c] != '.':
                return False, f"Attack position ({r}, {c}) overlaps with {board.board[r][c]}"
    return True, "Valid placement"


if __name__ == "__main__":
    board1 = Board(8, 8, [(0, 0), (2, 3)], [(7, 6)], [(3, 6), (4, 6), (5, 1), (6, 1), (7, 1), (7, 4), (7, 5)])
    board1.print_board()
    result, msg = validate_chess_placement(board1)
    assert result == True, msg
    board2 = Board(5, 4, [(0, 0), (0, 1)], [], [])
    board2.print_board()
    result, msg = validate_chess_placement(board2)
    assert result == False, msg

    board3 = Board(5, 4, [(0, 0)], [], [])
    assert can_place(board3, 0, 1, 'Q') == False
    assert can_place(board3, 1, 2, 'N') == False
    assert can_place(board3, 1, 1, 'B') == False
    assert can_place(board3, 1, 2, 'Q') == True


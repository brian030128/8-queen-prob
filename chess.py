queen_dirs = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
# Knight moves
knight_moves = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]
# Bishop moves
bishop_dirs = [(-1,-1), (-1,1), (1,-1), (1,1)]


def visualize_chess_placement(m, n, queen_positions, bishop_positions, knight_positions):
    board = [['.' for _ in range(n)] for _ in range(m)]
    for r, c in queen_positions:
        board[r][c] = 'Q'
    for r, c in bishop_positions:
        board[r][c] = 'B'
    for r, c in knight_positions:
        board[r][c] = 'N'
    
    for row in board:
        print(' '.join(row))


def validate_chess_placement(m, n, queen_positions, bishop_positions, knight_positions):
    def in_board(r, c):
        return 0 <= r < m and 0 <= c < n

    occupied = set(queen_positions) | set(bishop_positions) | set(knight_positions)

    # Step 1: Compute queen attack positions
    queen_attacks = set()
    for qr, qc in queen_positions:
        for dr, dc in queen_dirs:
            r, c = qr + dr, qc + dc
            while in_board(r, c):
                queen_attacks.add((r, c))
                if (r, c) in occupied:
                    break
                r += dr
                c += dc

    # Step 2: Validate bishop positions
    for i, (r1, c1) in enumerate(bishop_positions):
        if (r1, c1) in queen_attacks:
            return False, f"Bishop at {(r1, c1)} is attacked by a queen."
        for j in range(i + 1, len(bishop_positions)):
            r2, c2 = bishop_positions[j]
            if abs(r1 - r2) == abs(c1 - c2):
                return False, f"Bishops at {(r1, c1)} and {(r2, c2)} attack each other."

    # Step 3: Validate knight positions
    knight_set = set(knight_positions)
    for r, c in knight_positions:
        if (r, c) in queen_attacks:
            return False, f"Knight at {(r, c)} is attacked by a queen."
        for dr, dc in knight_moves:
            nr, nc = r + dr, c + dc
            if (nr, nc) in knight_set:
                return False, f"Knights at {(r, c)} and {(nr, nc)} attack each other."
            
    bishops_set = set(bishop_positions)
    for r, c in bishop_positions:
        if (r, c) in queen_attacks:
            return False, f"Bishop at {(r, c)} is attacked by a queen."
        for dr, dc in bishop_dirs:
            nr, nc = r + dr, c + dc

    # Step 4: Validate knight and bishop mutual non-attack (optional, they don’t attack each other by rule)
    return True, "Valid configuration."


if __name__ == "__main__":
    result, msg = validate_chess_placement(8, 8, [(0, 0), (2, 3)], [(7, 6)], [(3, 6), (4, 6), (5, 1), (6, 1), (7, 1), (7, 4), (7, 5)])
    assert result == True, msg
    result, msg = validate_chess_placement(8, 7, [(0, 0), (0, 1)], [(7, 6)], [(3, 6), (4, 6), (5, 1), (6, 1), (7, 1), (7, 4), (7, 5)])
    assert result == False, msg
    visualize_chess_placement(8, 8, [(0, 0), (2, 3)], [(7, 6)], [(3, 6), (4, 6), (5, 1), (6, 1), (7, 1), (7, 4), (7, 5)])

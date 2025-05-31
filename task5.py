from chess import *

def solve_knights_bishops(m, n, queen_positions):
    # Directions for queen (rook + bishop)


    board = [['.' for _ in range(n)] for _ in range(m)]
    attacked = [[False for _ in range(n)] for _ in range(m)]

    # Mark queens and their attack
    for qr, qc in queen_positions:
        board[qr][qc] = 'Q'
        attacked[qr][qc] = True
        for dr, dc in queen_dirs:
            r, c = qr + dr, qc + dc
            while 0 <= r < m and 0 <= c < n:
                attacked[r][c] = True
                if board[r][c] == 'Q':
                    break
                r += dr
                c += dc

    # Helper to check knight attack
    def knight_attacks(r, c, placed_knights):
        for dr, dc in knight_moves:
            nr, nc = r + dr, c + dc
            if (nr, nc) in placed_knights:
                return True
        return False

    # Helper to check bishop attack
    def bishop_attacks(r, c, placed_bishops):
        for dr, dc in bishop_dirs:
            nr, nc = r + dr, c + dc
            while 0 <= nr < m and 0 <= nc < n:
                if (nr, nc) in placed_bishops:
                    return True
                if board[nr][nc] == 'Q':
                    break
                nr += dr
                nc += dc
        return False

    # Try placing knights first then bishops (greedy)
    knights = []
    bishops = []
    occupied = set(queen_positions)

    for r in range(m):
        for c in range(n):
            if attacked[r][c] or (r, c) in occupied:
                continue
            # Try knight first
            if not knight_attacks(r, c, knights):
                knights.append((r, c))
                occupied.add((r, c))

    for r in range(m):
        for c in range(n):
            if attacked[r][c] or (r, c) in occupied:
                continue
            if not bishop_attacks(r, c, bishops):
                bishops.append((r, c))
                occupied.add((r, c))

    return {
        "total": len(knights) + len(bishops),
        "bishops": bishops,
        "knights": knights
    }




if __name__ == "__main__":
    result = solve_knights_bishops(8, 8, [(0, 0), (2, 3)])
    print("Total:", result["total"])
    print("bishops:", result["bishops"])
    print("knights:", result["knights"])

    
    valid, message = validate_chess_placement(8, 8, [(0, 0), (2, 3)], result["bishops"], result["knights"])
    print("✅" if valid else "❌", message)
def solve_knights_bishops(m, n):
    best = {'bishops': [], 'knights': []}
    occupied, bishops, knights = set(), [], []
    b_diag1, b_diag2 = set(), set()
    k_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
               (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def is_safe_bishop(x, y):
        return (x - y) not in b_diag1 and (x + y) not in b_diag2 and (x, y) not in occupied

    def is_safe_knight(x, y):
        return all((x + dx, y + dy) not in occupied for dx, dy in k_moves) and (x, y) not in occupied

    def backtrack(pos):
        if pos == m * n:
            total = len(bishops) + len(knights)
            best_total = len(best['bishops']) + len(best['knights'])
            if total > best_total:
                best['bishops'] = bishops[:]
                best['knights'] = knights[:]
            return
        x, y = divmod(pos, n)
        if is_safe_bishop(x, y):
            b_diag1.add(x - y)
            b_diag2.add(x + y)
            bishops.append((x, y))
            occupied.add((x, y))
            backtrack(pos + 1)
            b_diag1.remove(x - y)
            b_diag2.remove(x + y)
            bishops.pop()
            occupied.remove((x, y))
        if is_safe_knight(x, y):
            knights.append((x, y))
            occupied.add((x, y))
            backtrack(pos + 1)
            knights.pop()
            occupied.remove((x, y))
        backtrack(pos + 1)

    backtrack(0)
    return best['bishops'], best['knights']
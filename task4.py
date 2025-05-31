def solve_knights_bishops(m, n):
    best = {'bishops': [], 'knights': []}
    occupied = set()
    bishops, knights = [], []
    b_diag1, b_diag2 = set(), set()
    k_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
               (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def is_safe_bishop(x, y):
        if (x - y) in b_diag1 or (x + y) in b_diag2:
            return False
        if (x, y) in occupied:
            return False
        # bishop can't attack existing knights
        for kx, ky in knights:
            if abs(kx - x) == abs(ky - y):
                return False
        # bishop can't be attacked by existing knights
        for kx, ky in knights:
            if (abs(kx - x), abs(ky - y)) in [(2, 1), (1, 2)]:
                return False
        return True

    def is_safe_knight(x, y):
        if (x, y) in occupied:
            return False
        # knight can't attack existing knights
        for dx, dy in k_moves:
            if (x + dx, y + dy) in occupied:
                return False
        # knight can't attack existing bishops
        for bx, by in bishops:
            if (abs(bx - x), abs(by - y)) in [(2, 1), (1, 2)]:
                return False
        # knight can't be attacked by existing bishops
        for bx, by in bishops:
            if abs(bx - x) == abs(by - y):
                return False
        return True

    def backtrack(pos):
        if pos == m * n:
            total = len(bishops) + len(knights)
            best_total = len(best['bishops']) + len(best['knights'])
            # Update if we have more pieces OR if we have same number of pieces but both types exist
            if (total > best_total) or (total == best_total and len(bishops) > 0 and len(knights) > 0):
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

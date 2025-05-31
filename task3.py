def max_knights(m, n):
    best_solution = []
    current_solution = []
    occupied = set()

    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]

    def is_valid(x, y):
        for dx, dy in moves:
            if (x + dx, y + dy) in occupied:
                return False
        return True

    def backtrack(x, y):
        nonlocal best_solution
        if x >= m:
            if len(current_solution) > len(best_solution):
                best_solution = current_solution[:]
            return

        next_x, next_y = (x, y + 1) if y + 1 < n else (x + 1, 0)

        if is_valid(x, y):
            occupied.add((x, y))
            current_solution.append((x, y))
            backtrack(next_x, next_y)
            occupied.remove((x, y))
            current_solution.pop()

        backtrack(next_x, next_y)

    backtrack(0, 0)
    return best_solution
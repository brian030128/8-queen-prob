def max_bishops(m, n):
    best_solution = []
    current_solution = []
    diag1 = set()
    diag2 = set()

    def backtrack(x, y):
        nonlocal best_solution
        if x >= m:
            if len(current_solution) > len(best_solution):
                best_solution = current_solution[:]
            return

        next_x, next_y = (x, y + 1) if y + 1 < n else (x + 1, 0)

        if (x - y) not in diag1 and (x + y) not in diag2:
            diag1.add(x - y)
            diag2.add(x + y)
            current_solution.append((x, y))
            backtrack(next_x, next_y)
            diag1.remove(x - y)
            diag2.remove(x + y)
            current_solution.pop()

        backtrack(next_x, next_y)

    backtrack(0, 0)
    return best_solution
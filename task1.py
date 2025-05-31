def max_queens(m, n):
    result = []
    max_solution = []

    def backtrack(row, cols, diag1, diag2, current):
        nonlocal max_solution
        if row == m:
            if len(current) > len(max_solution):
                max_solution = current[:]
            return
        
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            current.append((row, col))

            backtrack(row + 1, cols, diag1, diag2, current)

            current.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        # 也可以考慮這一列不放皇后
        backtrack(row + 1, cols, diag1, diag2, current)

    backtrack(0, set(), set(), set(), result)
    return max_solution
#print(max_queens(8, 8))
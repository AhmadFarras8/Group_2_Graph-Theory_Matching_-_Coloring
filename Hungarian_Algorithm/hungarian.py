import sys


def read_matrix(lines):
    """Parse the input into an n x n matrix."""
    tokens = []
    for line in lines:
        tokens += line.split("#")[0].split()
    if not tokens:
        raise ValueError("Input is empty")
    n = int(tokens[0])
    values = [float(t) for t in tokens[1:]]
    if n <= 0:
        raise ValueError("Matrix size must be positive")
    if len(values) != n * n:
        raise ValueError(f"Expected {n * n} values for a {n}x{n} matrix, got {len(values)}")
    return [values[i * n:(i + 1) * n] for i in range(n)]


def reduce_rows_and_columns(m):
    """Steps 2 and 3: subtract the row minimums, then the column minimums."""
    n = len(m)
    for i in range(n):
        low = min(m[i])
        m[i] = [x - low for x in m[i]]
    for j in range(n):
        low = min(m[i][j] for i in range(n))
        for i in range(n):
            m[i][j] -= low


def max_zero_matching(m):
    """Largest set of zeros with no two in the same row or column (Kuhn's augmenting paths)."""
    n = len(m)
    match_col = [-1] * n            # match_col[j] = row matched to column j

    def try_row(i, seen):
        for j in range(n):
            if m[i][j] == 0 and not seen[j]:
                seen[j] = True
                if match_col[j] == -1 or try_row(match_col[j], seen):
                    match_col[j] = i
                    return True
        return False

    for i in range(n):
        try_row(i, [False] * n)
    return match_col


def min_cover(m, match_col):
    """Step 4: minimum lines covering all zeros (Konig's theorem).

    Returns (covered_rows, covered_cols).
    """
    n = len(m)
    match_row = [-1] * n
    for j, i in enumerate(match_col):
        if i != -1:
            match_row[i] = j

    # Mark rows reachable from unmatched rows by alternating zero / matched edges
    marked_rows = {i for i in range(n) if match_row[i] == -1}
    marked_cols = set()
    stack = list(marked_rows)
    while stack:
        i = stack.pop()
        for j in range(n):
            if m[i][j] == 0 and j not in marked_cols:
                marked_cols.add(j)
                r = match_col[j]
                if r != -1 and r not in marked_rows:
                    marked_rows.add(r)
                    stack.append(r)

    covered_rows = {i for i in range(n) if i not in marked_rows}
    covered_cols = marked_cols
    return covered_rows, covered_cols


def adjust(m, covered_rows, covered_cols):
    """Step 5: subtract the smallest uncovered value from uncovered elements,
    add it to elements covered by both a row line and a column line."""
    n = len(m)
    smallest = min(m[i][j] for i in range(n) for j in range(n)
                   if i not in covered_rows and j not in covered_cols)
    for i in range(n):
        for j in range(n):
            if i not in covered_rows and j not in covered_cols:
                m[i][j] -= smallest
            elif i in covered_rows and j in covered_cols:
                m[i][j] += smallest


def hungarian(cost, verbose=False):
    """Return (assignment, total_cost). assignment[i] = column given to row i."""
    n = len(cost)
    m = [row[:] for row in cost]        # work on a copy, keep the original costs

    reduce_rows_and_columns(m)
    if verbose:
        print("After row and column reduction:")
        show(m)

    rounds = 0
    while True:
        match_col = max_zero_matching(m)
        covered_rows, covered_cols = min_cover(m, match_col)
        lines = len(covered_rows) + len(covered_cols)
        if verbose:
            print(f"Cover zeros: {lines} line(s), matrix size {n}")
        if lines == n:
            break                        # step 6
        adjust(m, covered_rows, covered_cols)
        rounds += 1
        if verbose:
            print(f"Adjustment #{rounds}:")
            show(m)

    assignment = [-1] * n
    for j, i in enumerate(match_col):
        assignment[i] = j
    total = sum(cost[i][assignment[i]] for i in range(n))
    return assignment, total


def show(m):
    for row in m:
        print("  " + " ".join(f"{x:g}".rjust(6) for x in row))
    print()


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            lines = f.readlines()
    else:
        print("Enter matrix size n, then the n x n cost matrix:")
        lines = sys.stdin.readlines()

    try:
        cost = read_matrix(lines)
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    n = len(cost)
    print(f"Cost matrix ({n}x{n}):")
    show(cost)

    assignment, total = hungarian(cost, verbose=True)

    print("Optimal Assignment")
    print("------------------")
    for i, j in enumerate(assignment):
        print(f"Row {i + 1} -> Column {j + 1} (cost {cost[i][j]:g})")
    print(f"\nMinimum total cost: {total:g}")


if __name__ == "__main__":
    main()

# Part 1: Sudoku Solver Using Vertex Coloring & Backtracking
import numpy as np
import matplotlib.pyplot as plt
import os

def load_sudoku_from_file(filename):
    board = []
    with open(filename, 'r') as f:
        for line in f:
            row = [int(x) for x in line.split()]
            if row:
                board.append(row)
    return board

def is_safe(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def visualize_sudoku(solved_board):
    fig, ax = plt.subplots(figsize=(6, 6))
    color_grid = np.zeros((9, 9))
    for r in range(9):
        for c in range(9):
            if (r // 3 + c // 3) % 2 == 0:
                color_grid[r, c] = 1
                
    ax.imshow(color_grid, cmap='Blues', alpha=0.3, extent=[0, 9, 9, 0])
    for i in range(10):
        linewidth = 2.5 if i % 3 == 0 else 1
        ax.axhline(i, color='black', linewidth=linewidth)
        ax.axvline(i, color='black', linewidth=linewidth)
        
    for r in range(9):
        for c in range(9):
            val = solved_board[r][c]
            ax.text(c + 0.5, r + 0.5, str(val), fontsize=16, fontweight='bold', 
                    ha='center', va='center')
            
    ax.set_xlim(0, 9)
    ax.set_ylim(9, 0)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Sudoku Solution (Vertex Coloring Grid)", fontsize=14, fontweight='bold', pad=10)
    plt.tight_layout()
    plt.savefig('sudoku_coloring.png')
    print("Sudoku visualization saved as 'sudoku_coloring.png'")
    plt.show()

if __name__ == "__main__":
    sudoku_file = 'input_sudoku.txt'
    if os.path.exists(sudoku_file):
        board = load_sudoku_from_file(sudoku_file)
        print(f"Loaded Sudoku board from {sudoku_file}")
    else:
        print("Input file not found. Using default board.")
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

    print("Initial Sudoku Board:")
    for r in board:
        print(r)

    if solve_sudoku(board):
        print("\nSolved Sudoku Board:")
        for r in board:
            print(r)
        visualize_sudoku(board)
    else:
        print("No solution exists.")
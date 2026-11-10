# Group_2_Graph-Theory_Matching_and_Coloring

## Group Members

| No. | Name | NRP |
|-----|------|-----|
| 1 | Ahmad Farras Favian Al Efasi | 5025251005 |
| 2 | Daniel Pedrosaputra | 5025251171 |

## Algorithm Introduction

### Hungarian Algorithm (Kuhn-Munkres)

The Hungarian algorithm (Kuhn-Munkres algorithm) is a combinatorial optimization method for the assignment problem, which is a minimum-cost matching in a weighted bipartite graph. Given n workers and n jobs with a cost for every worker-job pair, it finds the one-to-one assignment with the lowest total cost. Instead of testing every possible assignment (n! of them), it repeatedly transforms the cost matrix so that zeros appear in the positions of an optimal assignment, without changing which assignment is optimal.

The algorithm relies on the following ideas:

- **Matching:** A subgraph in which no two edges share a vertex, so every matched vertex has degree one.
- **Perfect (complete) matching:** A matching that matches all vertices of the graph. Hall's Marriage Theorem states that a complete matching between V1 and V2 exists if and only if the deficiency δ(G) ≤ 0.
- **Cost matrix:** An n × n matrix where entry (i, j) is the cost of assigning row i to column j.
- **Row and column reduction:** Subtracting the minimum of each row, then the minimum of each column, creates zeros without changing the optimal assignment.
- **Covering lines:** The minimum number of horizontal and vertical lines needed to cover all zeros. If this number equals n, an optimal assignment exists among the zeros.

### Sudoku Solver using Graph Coloring (Backtracking)

Graph coloring is the problem of assigning colors to the vertices of a graph so that no two adjacent vertices have the same color. The minimum number of colors needed is called the chromatic number χ(G). A Sudoku puzzle is a natural application of vertex coloring, because the rules of Sudoku are exactly the constraints of a proper coloring.

The puzzle is modeled as a graph as follows:

- **Vertex:** Each of the 81 cells.
- **Edge:** Two cells are connected if they share a row, a column, or a 3×3 box. Every vertex therefore has 20 neighbors.
- **Colors:** The 9 colors are the digits 1 to 9.
- **Pre-colored vertices:** The given clues of the puzzle.
- **Solution:** A proper 9-coloring of the graph that extends the pre-colored vertices.

The solver uses backtracking m-coloring. It colors one vertex at a time, tries every legal color, and undoes (backtracks) a choice when a later vertex is left with no legal color.

## Steps

### Hungarian Algorithm

1. Construct the cost matrix (n × n).
2. Subtract the minimum value of each row from every element of that row.
3. Subtract the minimum value of each column from every element of that column.
4. Cover all zeros in the matrix using the minimum number of horizontal and vertical lines.
   - If the number of lines is not equal to n, go to step 5.
   - Otherwise, go to step 6.
5. Find the smallest element that is not covered. Subtract it from all uncovered elements and add it to elements covered by both a horizontal and a vertical line, then return to step 4.
6. Determine the optimal assignment by selecting one zero in every row and column. The sum of the original costs at those positions is the minimum total cost.

The textbook version of the algorithm runs in O(n⁴), and efficient implementations that maintain row and column potentials run in O(n³). The main drawback is that it only handles one-to-one assignment between sets of the same size, so a rectangular matrix must first be padded with dummy rows or columns, and the covering-lines step is tedious to implement directly.

### Sudoku Solver using Graph Coloring

1. Build the graph of 81 vertices, connecting every pair of cells that share a row, column, or 3×3 box.
2. Read the puzzle and pre-color the vertices that have a clue (0 or `.` means empty).
3. Check that the clues are valid, meaning no two adjacent vertices share the same color. If they do, stop because the puzzle is invalid.
4. Choose the uncolored vertex with the fewest legal colors. A color is legal if none of the vertex's neighbors already uses it.
5. If that vertex has no legal color, the current path is a dead end, so backtrack.
6. Otherwise, try each legal color in turn. Assign the color and repeat from step 4.
7. If a color leads to a dead end, reset the vertex to uncolored (backtrack) and try the next color.
8. When every vertex is colored, the coloring is a valid solution. If all colors fail for the first vertex, the puzzle has no solution.

Choosing the most constrained vertex first greatly reduces the number of backtracks compared with filling the cells in fixed order. In the worst case backtracking is still exponential, which is the main drawback, although 9×9 Sudoku is small enough that it solves in a fraction of a second.

## Implementations

### Hungarian Algorithm

The Hungarian Algorithm program is implemented in Python using a two-dimensional list as the cost matrix. The size of the matrix is not fixed: the program reads n from the input, so it works for any square matrix size and any set of costs.

<!-- TODO: replace the function names below with the ones in your own code. -->
The implementation begins by reading the cost matrix and validating that it is square. It then performs the row reduction and column reduction steps, which create the first zeros in the matrix. The program then determines the minimum set of lines covering all zeros. If the number of lines is smaller than n, the smallest uncovered value is subtracted from all uncovered elements and added to the elements covered twice, and the covering step is repeated. When the number of lines equals n, the program selects one zero in every row and column to form the optimal assignment. Finally, it maps the selected positions back to the original cost matrix, prints each assignment, and prints the minimum total cost.

The implementation is tested against the bulldozer example from the lecture, which has a minimum total distance of 275 km, and against additional cases with different matrix sizes and values.

### Sudoku Solver using Graph Coloring

The Sudoku Solver is implemented in Python using an adjacency-list representation of the graph. Each of the 81 cells is a vertex with an id from 0 to 80 (`row * 9 + column`), and its neighbors are stored in a set. The current coloring is stored in a list of 81 integers, where 0 means the vertex has no color yet.

The implementation begins with the `build_graph()` function, which creates the adjacency list by connecting every pair of cells that share a row, a column, or a 3×3 box. The `read_puzzle()` function then reads the input file, ignoring spaces and comments, and converts the 9 lines of 9 cells into the list of pre-colored vertices. It raises an error if the input is not exactly 9 × 9.

Before solving, the `clues_are_valid()` function checks that no two adjacent vertices have the same pre-assigned color. This lets the program report an invalid puzzle immediately instead of searching forever. The `available_colors()` function returns the colors that a vertex can legally take, which are the digits not already used by any of its neighbors.

The main solving procedure is the `color_graph()` function, which implements backtracking m-coloring. At each step it picks the uncolored vertex with the fewest available colors, assigns each available color in turn, and recursively colors the rest of the graph. If a recursive call fails, the vertex is reset to 0 (backtrack) and the next color is tried. The function returns true once all vertices are colored, and the number of backtracks is counted so that the effort of each puzzle can be compared.

The overall process is coordinated by the `main()` function, which reads the puzzle, checks the clues, runs `color_graph()`, and prints the result using `print_grid()`. If a valid coloring is found, the program prints the solved grid, otherwise it reports that the puzzle has no solution.

Overall, the implementation follows the main idea of vertex coloring by treating Sudoku rules as adjacency constraints and searching for a proper 9-coloring. Each function handles a specific stage of the process, making the implementation easier to understand, organize, and maintain.

## How to Run & Prerequisites

### Hungarian Algorithm

Before running the Hungarian Algorithm program, make sure the following requirements are met:

- **Python 3:** Installed on your computer.
- **Code Editor (Optional):** Visual Studio Code, PyCharm, or another editor for viewing and modifying the source code.
- **Project Files:** The repository cloned or extracted, with all files kept in the same directory.
- **Third-Party Libraries:** None required, as the program uses standard Python libraries. <!-- TODO: edit if you use numpy or scipy -->

### Sudoku Solver using Graph Coloring

Before running the Sudoku Solver, make sure the following requirements are met:

- **Python 3 (3.8 or newer):** Installed on your computer.
- **Code Editor (Optional):** Visual Studio Code, PyCharm, or another editor for viewing and modifying the source code.
- **Project Files:** The repository cloned or extracted, with `sudoku_coloring.py` and the sample input files kept in the same directory.
- **Third-Party Libraries:** None required, as the program uses standard Python libraries.

## Running the Program

### Hungarian Algorithm

1. **Get the project files.** Clone the repository or extract the project files into a directory on your computer.

2. **Open the project directory.** Open the folder using a terminal or command prompt.

3. **Run the program.** Execute the following command:

   ```
   python hungarian.py
   ```

   If the command above does not work, try:

   ```
   python3 hungarian.py
   ```

   <!-- TODO: replace hungarian.py with your actual file name, and fix the input steps below if you read from a file. -->

4. **Enter the matrix information.** Follow the instructions displayed in the terminal to enter the matrix size n and the n × n cost matrix.

5. **View the result.** The program processes the matrix using the Hungarian Algorithm and displays the optimal assignment and the minimum total cost.

### Sudoku Solver using Graph Coloring

1. **Get the project files.** Clone the repository or extract the project files into a directory on your computer.

2. **Open the project directory.** Open the folder using a terminal or command prompt.

3. **Run the program.** Execute the following command to solve the default sample puzzle:

   ```
   python sudoku_coloring.py
   ```

   If the command above does not work, try:

   ```
   python3 sudoku_coloring.py
   ```

4. **Choose a puzzle (optional).** Pass the path of an input file as an argument:

   ```
   python sudoku_coloring.py sample_input_2.txt
   ```

5. **View the result.** The program prints the puzzle, then either the solved grid together with the number of backtracks, or a message that the puzzle is invalid or has no solution.

## Example Input

### Hungarian Algorithm

The following example is the bulldozer problem from the lecture, with 4 bulldozers and 4 construction sites. Each value is the distance in km:

```
Matrix size: 4
Cost matrix:
90 75 75 80
35 85 55 65
125 95 90 105
45 110 95 115
```

<!-- TODO: adjust this block to match your program's real input format. -->

### Sudoku Solver using Graph Coloring

The input is 9 lines of 9 cells. Use `0` or `.` for an empty cell. Spaces are optional, and text after `#` is ignored.

```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

## Running the Tests

### Hungarian Algorithm

To test the program, run it with several cost matrices of different sizes and compare the minimum total cost with the expected result.

<!-- TODO: if you wrote a unittest file or compared with scipy.optimize.linear_sum_assignment, describe it here, for example: python -m unittest -v test_hungarian.py -->

### Sudoku Solver using Graph Coloring

To test the program, run `sudoku_coloring.py` on each of the provided sample files and check the results:

```
python sudoku_coloring.py sample_input.txt
python sudoku_coloring.py sample_input_2.txt
python sudoku_coloring.py sample_input_invalid.txt
```

| File | Description | Expected result |
|------|-------------|-----------------|
| `sample_input.txt` | Puzzle from the lecture slides | Solved |
| `sample_input_2.txt` | A different, easier puzzle | Solved |
| `sample_input_invalid.txt` | Two clues of 5 in the same row | Reported as invalid |

## Sample Run Result

### Hungarian Algorithm

The following example demonstrates how the Hungarian Algorithm program processes the bulldozer problem and displays the result.

**Example 1: Bulldozer Assignment (4 × 4)**

Input:

```
Matrix size: 4
Cost matrix:
90 75 75 80
35 85 55 65
125 95 90 105
45 110 95 115
```

Output:

```
Optimal Assignment
------------------
Bulldozer 1 -> Construction site 4 (80 km)
Bulldozer 2 -> Construction site 3 (55 km)
Bulldozer 3 -> Construction site 2 (95 km)
Bulldozer 4 -> Construction site 1 (45 km)

Minimum total distance: 275 km
```

<!-- TODO: replace the output above with your program's actual output, and add a second example with a different matrix size. -->

### Sudoku Solver using Graph Coloring

The following examples demonstrate how the Sudoku Solver processes puzzles and displays the results.

**Example 1: Easy Puzzle (`sample_input_2.txt`)**

Output:

```
Solved (0 backtracks):
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

**Example 2: Puzzle from the Lecture Slides (`sample_input.txt`)**

Output:

```
Solved (1538 backtracks):
7 4 9 | 2 3 8 | 6 1 5
1 5 2 | 6 9 7 | 8 3 4
8 3 6 | 4 5 1 | 2 7 9
------+-------+------
2 1 8 | 9 7 6 | 5 4 3
9 7 5 | 3 2 4 | 1 8 6
4 6 3 | 8 1 5 | 7 9 2
------+-------+------
3 2 1 | 5 8 9 | 4 6 7
5 8 4 | 7 6 3 | 9 2 1
6 9 7 | 1 4 2 | 3 5 8
```

This puzzle has more than one valid solution, so the grid may differ from the one printed on the slide. Every adjacent pair of cells still has different digits, so it is a valid coloring.

**Example 3: Invalid Puzzle (`sample_input_invalid.txt`)**

Output:

```
Invalid puzzle: two adjacent cells share the same clue.
```

These examples illustrate how the implementation turns Sudoku into a graph coloring problem. A solvable puzzle produces a proper 9-coloring, while conflicting clues are detected before any search starts.

## Prompt History

### Hungarian Algorithm



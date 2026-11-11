# Group_2_Graph-Theory_Matching_and_Coloring

## Group Members

| No. | Name | NRP |
|-----|------|-----|
| 1 | Ahmad Farras Favian Al Efasi | 5025251005 |
| 2 | Daniel Pedrosaputra | 5025251171 |

## Algorithm Introduction

### Hungarian Algorithm (Kuhn-Munkres)

This homework covers the Matching topic of the lecture. The task is to recreate the lecture sample (the bulldozer assignment problem) with different cases and a dynamic matrix size, using the Hungarian algorithm.

The Hungarian algorithm (Kuhn-Munkres algorithm) is a combinatorial optimization method for the assignment problem, which is a minimum-cost matching in a weighted bipartite graph. Given n workers and n jobs with a cost for every worker-job pair, it finds the one-to-one assignment with the lowest total cost. Instead of testing every possible assignment (n! of them), it repeatedly transforms the cost matrix so that zeros appear in the positions of an optimal assignment, without changing which assignment is optimal.

The algorithm relies on the following ideas:

- **Matching:** A subgraph in which no two edges share a vertex, so every matched vertex has degree one.
- **Perfect (complete) matching:** A matching that matches all vertices of the graph. Hall's Marriage Theorem states that a complete matching between V1 and V2 exists if and only if the deficiency δ(G) ≤ 0.
- **Cost matrix:** An n × n matrix where entry (i, j) is the cost of assigning row i to column j.
- **Row and column reduction:** Subtracting the minimum of each row, then the minimum of each column, creates zeros without changing the optimal assignment.
- **Covering lines:** The minimum number of horizontal and vertical lines needed to cover all zeros. If this number equals n, an optimal assignment exists among the zeros.

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

The textbook version of the algorithm runs in O(n⁴), and efficient implementations that maintain row and column potentials run in O(n³). Our implementation follows the lecture steps directly and favors clarity over speed. The main drawback of the algorithm is that it only handles one-to-one assignment between sets of the same size, so a rectangular matrix must first be padded with dummy rows or columns, and the covering-lines step is tedious to implement directly.

## Implementations

### Hungarian Algorithm

The Hungarian Algorithm program is implemented in Python using a two-dimensional list as the cost matrix. The size of the matrix is not fixed: the program reads n from the input, so it works for any square matrix size and any set of costs.

The implementation begins with the `read_matrix()` function, which reads the matrix size n and the n × n values from the input, ignoring comments. It raises an error if the number of values does not match n × n. The `hungarian()` function then works on a copy of the matrix, so the original costs are kept for calculating the final total.

The `reduce_rows_and_columns()` function performs the row reduction and column reduction steps, which create the first zeros in the matrix. Next, the program must cover all zeros with the minimum number of lines. This is done by the `max_zero_matching()` function, which finds the largest set of zeros with no two in the same row or column using augmenting paths, and the `min_cover()` function, which converts that matching into the minimum set of covered rows and columns using König's theorem. The number of lines equals the size of the matching.

If the number of lines is smaller than n, the `adjust()` function finds the smallest uncovered value, subtracts it from all uncovered elements, and adds it to the elements covered by both a row line and a column line. The covering step is then repeated. When the number of lines equals n, the zeros contain a complete assignment. The program reads it from the matching, maps the selected positions back to the original cost matrix, and calculates the minimum total cost.

The overall process is coordinated by the `main()` function, which reads the input from a file or from the terminal, prints every intermediate matrix with the `show()` function, and displays the optimal assignment and the minimum total cost. The implementation is verified in `test_hungarian.py` against the bulldozer example from the lecture, which has a minimum total distance of 275 km, and against brute force on random matrices of different sizes.

Overall, the implementation follows the main idea of the Hungarian algorithm by gradually transforming the cost matrix until the zeros contain a complete assignment. Each function handles a specific stage of the process, making the implementation easier to understand, organize, and maintain.

## How to Run & Prerequisites

### Hungarian Algorithm

Before running the Hungarian Algorithm program, make sure the following requirements are met:

- **Python 3:** Installed on your computer.
- **Code Editor (Optional):** Visual Studio Code, PyCharm, or another editor for viewing and modifying the source code.
- **Project Files:** The repository cloned or extracted, with all files kept in the same directory:

  ```
  
  ├── hungarian.py
  ├── test_hungarian.py
  ├── sample_input.txt
  ├── sample_input_2.txt
  └── sample_input_3.txt
  ```

- **Third-Party Libraries:** None required, as the program uses standard Python libraries.

## Running the Program

### Hungarian Algorithm

1. **Get the project files.** Clone the repository or extract the project files into a directory on your computer.

2. **Open the project directory.** Open the project folder using a terminal or command prompt.

3. **Run the program.** Execute the following command to read the matrix from a file:

   ```
   python hungarian.py sample_input.txt
   ```

   If the command above does not work, try:

   ```
   python3 hungarian.py sample_input.txt
   ```

4. **Or type the matrix in the terminal.** Run the program without a file name, then enter the matrix size n followed by the n × n cost matrix. Finish the input with `Ctrl + D` (Linux/macOS) or `Ctrl + Z` then `Enter` (Windows):

   ```
   python hungarian.py
   ```

5. **View the result.** The program prints the cost matrix after each step, then displays the optimal assignment and the minimum total cost.

## Example Input

### Hungarian Algorithm

The input starts with the matrix size n, followed by the n × n cost matrix. Text after `#` is ignored. The following example is the bulldozer problem from the lecture, with 4 bulldozers and 4 construction sites. Each value is the distance in km:

```
4
90 75 75 80
35 85 55 65
125 95 90 105
45 110 95 115
```

## Running the Tests

### Hungarian Algorithm

The project includes `test_hungarian.py`, which contains test cases for the implementation. To execute the tests, run the following command from the project directory:

```
python -m unittest -v test_hungarian.py
```

The tests check the bulldozer example from the lecture (275 km), a 1 × 1 matrix, an identity-cost matrix, a matrix with all equal costs, that the assignment is a valid permutation, the input parsing, and 175 random matrices of size 1 to 7 whose results are compared with a brute force search over all assignments. All 8 tests pass.

## Sample Run Result

### Hungarian Algorithm

The following examples demonstrate how the Hungarian Algorithm program processes cost matrices of different sizes and displays the optimal assignment. Each input starts with the matrix size n, followed by the n × n cost matrix.

**Example 1: Bulldozer Assignment from the Lecture (4 × 4)**

Command:

```
python hungarian.py sample_input.txt
```

Input:

```
4
90 75 75 80
35 85 55 65
125 95 90 105
45 110 95 115
```

Output:

```
Cost matrix (4x4):
      90     75     75     80
      35     85     55     65
     125     95     90    105
      45    110     95    115

After row and column reduction:
      15      0      0      0
       0     50     20     25
      35      5      0     10
       0     65     50     65

Cover zeros: 3 line(s), matrix size 4
Adjustment #1:
      35      0      0      0
       0     30      0      5
      55      5      0     10
       0     45     30     45

Cover zeros: 3 line(s), matrix size 4
Adjustment #2:
      40      0      5      0
       0     25      0      0
      55      0      0      5
       0     40     30     40

Cover zeros: 4 line(s), matrix size 4
Optimal Assignment
------------------
Row 1 -> Column 4 (cost 80)
Row 2 -> Column 3 (cost 55)
Row 3 -> Column 2 (cost 95)
Row 4 -> Column 1 (cost 45)

Minimum total cost: 275
```

**Example 2: Workers and Tasks (5 × 5)**

Command:

```
python hungarian.py sample_input_2.txt
```

Input:

```
5
12 8 15 10 9
7 9 8 14 11
13 6 12 9 10
9 11 7 8 13
10 12 9 11 6
```

Output:

```
Cost matrix (5x5):
      12      8     15     10      9
       7      9      8     14     11
      13      6     12      9     10
       9     11      7      8     13
      10     12      9     11      6

After row and column reduction:
       4      0      7      1      1
       0      2      1      6      4
       7      0      6      2      4
       2      4      0      0      6
       4      6      3      4      0

Cover zeros: 4 line(s), matrix size 5
Adjustment #1:
       3      0      6      0      0
       0      3      1      6      4
       6      0      5      1      3
       2      5      0      0      6
       4      7      3      4      0

Cover zeros: 5 line(s), matrix size 5
Optimal Assignment
------------------
Row 1 -> Column 4 (cost 10)
Row 2 -> Column 1 (cost 7)
Row 3 -> Column 2 (cost 6)
Row 4 -> Column 3 (cost 7)
Row 5 -> Column 5 (cost 6)

Minimum total cost: 36
```

**Example 3: Small Case (3 × 3)**

Command:

```
python hungarian.py sample_input_3.txt
```

Input:

```
3
4 1 3
2 0 5
3 2 2
```

Output:

```
Cost matrix (3x3):
       4      1      3
       2      0      5
       3      2      2

After row and column reduction:
       2      0      2
       1      0      5
       0      0      0

Cover zeros: 2 line(s), matrix size 3
Adjustment #1:
       1      0      1
       0      0      4
       0      1      0

Cover zeros: 3 line(s), matrix size 3
Optimal Assignment
------------------
Row 1 -> Column 2 (cost 1)
Row 2 -> Column 1 (cost 2)
Row 3 -> Column 3 (cost 2)

Minimum total cost: 5
```

These examples illustrate how the implementation follows the lecture steps: row and column reduction, covering all zeros with lines, adjusting the matrix, and repeating until the number of lines equals the matrix size n. The first example reproduces the bulldozer problem from the slides (275 km), while the other two show that the program works for different matrix sizes and costs.


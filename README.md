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


## Implementations

### Hungarian Algorithm

The Hungarian Algorithm program is implemented in Python using a two-dimensional list as the cost matrix. The size of the matrix is not fixed: the program reads n from the input, so it works for any square matrix size and any set of costs.

<!-- TODO: replace the function names below with the ones in your own code. -->
The implementation begins by reading the cost matrix and validating that it is square. It then performs the row reduction and column reduction steps, which create the first zeros in the matrix. The program then determines the minimum set of lines covering all zeros. If the number of lines is smaller than n, the smallest uncovered value is subtracted from all uncovered elements and added to the elements covered twice, and the covering step is repeated. When the number of lines equals n, the program selects one zero in every row and column to form the optimal assignment. Finally, it maps the selected positions back to the original cost matrix, prints each assignment, and prints the minimum total cost.

The implementation is tested against the bulldozer example from the lecture, which has a minimum total distance of 275 km, and against additional cases with different matrix sizes and values.


## How to Run & Prerequisites

### Hungarian Algorithm

Before running the Hungarian Algorithm program, make sure the following requirements are met:

- **Python 3:** Installed on your computer.
- **Code Editor (Optional):** Visual Studio Code, PyCharm, or another editor for viewing and modifying the source code.
- **Project Files:** The repository cloned or extracted, with all files kept in the same directory.
- **Third-Party Libraries:** None required, as the program uses standard Python libraries. <!-- TODO: edit if you use numpy or scipy -->

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


## Running the Tests

### Hungarian Algorithm

To test the program, run it with several cost matrices of different sizes and compare the minimum total cost with the expected result.

<!-- TODO: if you wrote a unittest file or compared with scipy.optimize.linear_sum_assignment, describe it here, for example: python -m unittest -v test_hungarian.py -->


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


## Prompt History

### Hungarian Algorithm



from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a `rows x cols` matrix `mat` where:
          - `0` represents a **zero cell**.
          - `1` represents a **one cell**.
        - The goal is to update every `1` in the matrix with the **distance to the nearest 0**.
        - The distance is measured in **four possible directions**: up, down, left, and right.

        Constraints:
        - `1 <= rows, cols <= 10^4` (Very large input! Need an efficient solution).
        - `mat[i][j]` is either `0` or `1`.

        Clarifications:
        - What if the matrix contains all `0`s? ➝ Return the same matrix.
        - What if the matrix contains all `1`s? ➝ Output will be filled with distances from the nearest `0`.
        - Can we modify `mat` in place? ➝ Yes.
        - Can diagonal movements be considered? ➝ No, only **4 directions**.

        Examples:
        Input: mat = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1]
        ]
        Output: [
            [0, 0, 0],
            [0, 1, 0],
            [1, 2, 1]
        ]

        Input: mat = [
            [0, 1, 1],
            [1, 1, 1],
            [1, 1, 0]
        ]
        Output: [
            [0, 1, 2],
            [1, 2, 1],
            [2, 1, 0]
        ]
        """

        # M - Match with Patterns
        """
        - This is a **Graph Traversal** problem.
        - It can be solved efficiently using **BFS (Breadth-First Search)** because:
          - We need the **shortest** distance from each `1` to the nearest `0`.
          - BFS is optimal for shortest path problems on an **unweighted grid**.
        - Instead of starting from every `1`, we can **start from all `0`s** and propagate outwards.
        """

        # P - Plan
        """
        1. Initialize a BFS queue (`q`) and mark all `0`s as starting points.
        2. Convert all `1`s into `-1` (unprocessed state).
        3. Perform BFS:
            - Dequeue a cell `(row, col, step)`.
            - Try all **4 directions** (up, down, left, right).
            - If a neighbor `(nr, nc)` is `-1`, update it with `step` and enqueue `(nr, nc, step+1)`.
        4. Return the modified matrix `mat` with distances updated.
        """

        rows, cols = len(mat), len(mat[0])
        q = deque()

        # Step 1: Initialize BFS queue with all 0s
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j, 1))  # Initialize BFS with `0` positions
                else:
                    mat[i][j] = -1  # Mark `1`s as unprocessed

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4 possible directions

        # Step 2: Process BFS
        while q:
            row, col, step = q.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = step  # Update distance
                    q.append((nr, nc, step + 1))  # Enqueue next cell

        return mat

        """
        I - Implement
        ✅ Uses **Breadth-First Search (BFS)**.
        ✅ Ensures shortest distance propagation.
        ✅ Modifies `mat` in-place, keeping **O(1) extra space**.

        R - Review
        ✅ Traverses each cell **only once**.
        ✅ Uses **O(N * M) time complexity**, where `N` and `M` are matrix dimensions.
        ✅ Uses **O(N * M) space complexity** for BFS queue.

        E - Evaluate
        Time Complexity: **O(N * M)**
        - Each cell is visited once and added to the queue once.
        - BFS runs in **linear time**.

        Space Complexity: **O(N * M)**
        - Worst-case scenario: Entire grid is filled with `1`s, requiring all cells in the queue.

        Optimizations:
        - Use **in-place modification** to reduce extra memory usage.
        """

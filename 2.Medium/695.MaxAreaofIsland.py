class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a 2D grid consisting of 1s (land) and 0s (water), find the maximum area of an island.
        - An island is formed by a group of connected 1s, connected horizontally or vertically.
        - Assume all edges of the grid are surrounded by water.

        Clarifications/Constraints:
        - The grid size is m x n (1 <= m, n <= 50).
        - The function should return 0 if there are no islands.

        Examples:
        Input: grid = [[0, 1], [1, 1]] -> Output: 3
        Input: grid = [[0, 0, 0], [0, 0, 0]] -> Output: 0
        Input: grid = [[1]] -> Output: 1

        Potential clarifying questions for an interview:
        1. Can islands touch diagonally? (No, only horizontal and vertical connections count.)
        2. Should the grid be modified? (Yes, mark visited cells by setting them to 0.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use Depth-First Search (DFS) to traverse each island.
        # - Mark cells as visited by modifying the grid (sink the island).
        # - For each land cell, calculate the connected area recursively.

        """
        P - Plan
        1. Define a helper function `calculateSum` that:
           - Returns 0 if the cell is out of bounds or is water.
           - Marks the cell as visited by setting it to 0.
           - Recursively explores its neighbors (up, down, left, right) and sums their areas.
        2. Traverse the grid:
           - If a cell is land (value 1), call `calculateSum` to calculate the area of the island.
           - Update the maximum area found so far.
        3. Return the maximum area as the result.
        """

        def calculateSum(i, j, row, col):
            # Base case: out of bounds or water
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return 0

            # Mark the cell as visited by setting it to 0 (sinking the island)
            grid[i][j] = 0

            # Recursively calculate the sum of the current cell and its neighbors
            up = calculateSum(i - 1, j, row, col)
            right = calculateSum(i, j + 1, row, col)
            down = calculateSum(i + 1, j, row, col)
            left = calculateSum(i, j - 1, row, col)

            # Include the current cell in the area count
            return 1 + up + right + down + left

        row, col = len(grid), len(grid[0])
        answer = 0

        # Traverse the grid to find the maximum area of islands
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:  # Start a DFS if a land cell is found
                    answer = max(answer, calculateSum(i, j, row, col))

        # Return the maximum island area found
        return answer

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: grid = [[0, 1], [1, 1]] -> Output: 3
2. Input: grid = [[0, 0, 0], [0, 0, 0]] -> Output: 0
3. Input: grid = [[1]] -> Output: 1

Edge Cases:
1. Grid with no land (all 0s) -> Output: 0.
2. Grid with only one land cell (1) -> Output: 1.
3. Large grid with multiple disconnected islands -> Correctly calculate maximum area.

Time Complexity:
- O(m * n): Each cell is visited at most once.

Space Complexity:
- O(m * n): Maximum recursion depth for DFS (stack usage).
"""

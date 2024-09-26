class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def calculateSum(i, j, row, col):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return 0

            # Mark the cell as visited by setting it to 0 (sinking the island)
            grid[i][j] = 0

            # Calculate the sum of the current cell and its neighbors
            up = calculateSum(i - 1, j, row, col)
            right = calculateSum(i, j + 1, row, col)
            down = calculateSum(i + 1, j, row, col)
            left = calculateSum(i, j - 1, row, col)

            # The current cell itself counts as 1, so add 1 to the sum of its neighbors
            return 1 + up + right + down + left

        row, col = len(grid), len(grid[0])
        answer = 0

        # Traverse the grid and find the maximum area of islands
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    # Update the answer with the maximum island area found
                    answer = max(answer, calculateSum(i, j, row, col))

        return answer
        
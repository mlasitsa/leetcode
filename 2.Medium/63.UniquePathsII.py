class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        U - Understand:
        - Given a grid with obstacles, find the number of unique paths from top-left to bottom-right.
        - A cell with 1 is an obstacle and cannot be traversed.
        - A cell with 0 is free to traverse.
        - Only downward and rightward moves are allowed.

        M - Match:
        - Dynamic programming: Tabulation for efficient path calculation.
        - Recursive backtracking (TLE).
        - Recursive backtracking with memoization for optimization.

        P - Plan:
        - Implement three approaches:
            1. Dynamic Programming (most efficient).
            2. Recursive approach without memoization (time-limit exceeded for large inputs).
            3. Recursive approach with memoization.
        """

        # Method 1: Dynamic Programming
        def dp_solution(obstacleGrid):
            if obstacleGrid[0][0] == 1:
                return 0

            dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
            dp[0][0] = 1

            for i in range(len(obstacleGrid)):
                for j in range(len(obstacleGrid[0])):
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        if i > 0:
                            dp[i][j] += dp[i - 1][j]
                        if j > 0:
                            dp[i][j] += dp[i][j - 1]

            return dp[-1][-1]

        # Method 2: Recursive Approach (TLE for large inputs)
        def recursive_solution(obstacleGrid):
            def helper(row, col):
                if row < 0 or col < 0 or row >= len(obstacleGrid) or col >= len(obstacleGrid[0]) or obstacleGrid[row][col] == 1:
                    return 0
                if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1:
                    return 1
                return helper(row + 1, col) + helper(row, col + 1)

            return helper(0, 0)

        # Method 3: Recursive Approach with Memoization
        def recursive_memo_solution(obstacleGrid):
            def helper(row, col, memo):
                if row < 0 or col < 0 or row >= len(obstacleGrid) or col >= len(obstacleGrid[0]) or obstacleGrid[row][col] == 1:
                    return 0
                if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1:
                    return 1
                if (row, col) in memo:
                    return memo[(row, col)]

                memo[(row, col)] = helper(row + 1, col, memo) + helper(row, col + 1, memo)
                return memo[(row, col)]

            return helper(0, 0, {})

        # Uncomment one of the methods to use:

        # return dp_solution(obstacleGrid)         # Method 1: Dynamic Programming (Most efficient)
        # return recursive_solution(obstacleGrid) # Method 2: Recursive (Inefficient, TLE)
        return recursive_memo_solution(obstacleGrid)  # Method 3: Recursive with Memoization

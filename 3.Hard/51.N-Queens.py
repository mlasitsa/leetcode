class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # U - Understand the Problem
        # Place `n` queens on an `n x n` chessboard such that:
        # - No two queens attack each other
        # - Return all valid configurations
        #
        # Queens can attack: same row, same column, or diagonals
        #
        # Input: n = 4
        # Output:
        # [
        #   [".Q..","...Q","Q...","..Q."],
        #   ["..Q.","Q...","...Q",".Q.."]
        # ]

        # M - Match with Patterns
        # - This is a classic **backtracking** problem
        # - We try placing a queen row by row
        # - At each row, we attempt to place a queen in every column and check if it's safe
        # - If safe, we place it and move to the next row (recursive call)
        # - If we reach row == n, we have a valid board configuration

        # P - Plan
        # 1. Create a board with "." initially
        # 2. Start backtracking from row 0
        # 3. In each row, try placing queen in each column if safe
        # 4. If placed, call backtrack for the next row
        # 5. If a valid configuration is found (row == n), copy and save the board
        # 6. Restore state (backtrack)

        res = []
        board = [["."] * n for i in range(n)]  # Initial empty board

        def backtrack(r):
            if r == n:
                # Found a valid board setup, convert to list of strings and save
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if self.isSafe(r, c, board):  # Check if we can place a queen here
                    board[r][c] = "Q"         # Place the queen
                    backtrack(r + 1)          # Move to the next row
                    board[r][c] = "."         # Backtrack: remove the queen

        backtrack(0)
        return res

    # isSafe checks if placing a queen at (r, c) is valid by verifying:
    # - no queens in the same column above
    # - no queens in the upper-left diagonal
    # - no queens in the upper-right diagonal
    def isSafe(self, r: int, c: int, board):
        # Check vertical column
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        # Check upper-left diagonal
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # Check upper-right diagonal
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1

        return True

        # R - Review
        # - Carefully backtracks and checks constraints
        # - Only places queens where they are safe

        # E - Evaluate
        # Time complexity: O(N!) — each row has N choices, but pruning reduces it significantly
        # Space complexity: O(N^2) for the board + O(N) recursion stack


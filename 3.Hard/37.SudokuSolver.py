# This solution leads to timeout for the last test case on LC, I will improve it once I have more time.
# Or feel free to try it yourself.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        U - Understand the Problem
        -------------------------------------
        Problem:
        - Given a partially filled 9x9 Sudoku board, fill in the blanks so that:
            1. Each row contains digits 1-9 with no repetition.
            2. Each column contains digits 1-9 with no repetition.
            3. Each of the 9 sub-boxes (3x3) contains digits 1-9 with no repetition.
        
        Constraints:
        - The input board is always solvable.
        - You must modify the input board in-place.
        
        M - Match with Patterns
        -------------------------------------
        Pattern: Backtracking + Constraint Validation
        - Try filling empty cells with numbers 1–9.
        - Recursively continue if valid.
        - Backtrack if a dead-end is reached.
        
        P - Plan
        -------------------------------------
        1. Loop through all cells on the board.
        2. If cell is ".", try digits 1–9.
        3. For each digit:
            a. Check if it's valid (row, column, sub-box).
            b. If valid, place it and recurse to the next cell.
            c. If recursion fails, backtrack (reset cell to ".").
        4. Return True if board is complete.

        Helper Functions:
        - `isValid(ch, row, col)`: Checks if placing `ch` at board[row][col] breaks Sudoku rules.
        """

        def isValid(ch, row, col):
            for i in range(9):
                if board[row][i] == ch or board[i][col] == ch:
                    return False
            start_row = 3 * (row // 3)
            start_col = 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == ch:
                        return False
            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for ch in "123456789":
                            if isValid(ch, i, j):
                                board[i][j] = ch
                                if solve():
                                    return True
                                board[i][j] = "."  # Backtrack
                        return False  # No valid number found
            return True  # Fully solved

        solve()

        """
        R - Review
        -------------------------------------
        - Uses recursive DFS to explore valid placements.
        - Backtracking helps undo invalid paths.
        - Checks constraints at every decision point.

        E - Evaluate
        -------------------------------------
        Time Complexity: O(9^(m)) where m = number of empty cells (worst case).
        Space Complexity: O(m) for recursion stack depth.

        Edge Cases:
        - Fully filled and valid board → no changes.
        - One empty cell → just one recursive call needed.
        - Empty board → many combinations; full backtracking.

        Optimization Tip:
        - Use row/col/box sets to memoize used values for faster constraint checking.
        """

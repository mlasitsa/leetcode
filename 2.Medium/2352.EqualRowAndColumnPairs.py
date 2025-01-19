from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given an `n x n` grid, find the number of row-column pairs (r, c) such that the row `r` is equal to column `c`.

        Clarifications/Constraints:
        - The grid is guaranteed to be square (`n x n`).
        - Rows and columns can be identical.
        - Multiple matching row-column pairs are possible, and each match should be counted.

        Examples:
        Input: [[3,2,1],[1,7,6],[2,7,7]] -> Output: 1
        Explanation: Only the first row matches the first column.

        Input: [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,5,2,2]] -> Output: 3
        Explanation: Multiple matches between rows and columns.

        Potential clarifying questions for an interview:
        1. Can the grid contain negative numbers or zeros? (Yes.)
        2. What should the function return if there are no matches? (Return 0.)
        3. How large can the grid size be? (Assume it fits in memory.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use hash maps to count occurrences of rows and columns as tuples.
        # - Compare the counts of matching row and column tuples to calculate the result.

        """
        P - Plan
        1. Traverse the grid row-wise and store each row as a tuple in a hash map (`row_map`).
           - Keep track of the count of each row tuple.
        2. Traverse the grid column-wise and store each column as a tuple in another hash map (`col_map`).
           - Keep track of the count of each column tuple.
        3. Compare the tuples in `row_map` and `col_map`:
           - For each matching tuple, multiply their counts and add to the result.
        """

        # Step 1: Create a hash map for rows
        row_map = {}  # Hashmap to store row tuples and their counts
        for r in range(len(grid)):
            row_tuple = tuple(grid[r])  # Convert row to tuple
            row_map[row_tuple] = row_map.get(row_tuple, 0) + 1

        # Step 2: Create a hash map for columns
        col_map = {}  # Hashmap to store column tuples and their counts
        for c in range(len(grid[0])):  # Loop over each column index
            col_tuple = tuple(grid[r][c] for r in range(len(grid)))  # Collect column as tuple
            col_map[col_tuple] = col_map.get(col_tuple, 0) + 1

        # Step 3: Count matching row-column pairs
        count = 0
        for row_tuple in row_map:
            if row_tuple in col_map:
                count += row_map[row_tuple] * col_map[row_tuple]

        return count

# Example Usage
sol = Solution()

"""
E - Evaluate
Test the solution with examples:
1. Input: [[3,2,1],[1,7,6],[2,7,7]] -> Output: 1
2. Input: [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,5,2,2]] -> Output: 3
3. Input: [[1,2],[2,1]] -> Output: 0

Edge Cases:
1. No matching row-column pairs -> Output: 0
2. Grid with all identical rows and columns -> Multiply all occurrences.
3. Single element grid -> Output: 1

Time Complexity:
- O(n^2): Iterating through the grid row-wise and column-wise.
- Hashmap operations (insert/get) are O(1) on average.

Space Complexity:
- O(n^2): Space required for `row_map` and `col_map`.

"""

res = sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]])

if res == 1:
    print("Good Job")
else:
    print("Try again...")

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        U - Understand:
        - Problem: Given an `m x n` matrix where:
          1. Integers in each row are sorted in ascending order from left to right.
          2. Integers in each column are sorted in ascending order from top to bottom.
        - Determine if a given `target` value exists in the matrix.
        - Examples:
          - Input: matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]], target = 5
            Output: True
          - Input: matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]], target = 10
            Output: False
        - Constraints:
          1. Matrix dimensions: `1 <= m, n <= 1000`.
          2. Values: `-10^9 <= matrix[i][j], target <= 10^9`.

        M - Match:
        - Use a **search algorithm** optimized for the matrix's properties:
          - Each row and column are sorted.
        - Start from the top-right corner:
          - If the current value is greater than the target, move left.
          - If the current value is less than the target, move down.

        P - Plan:
        1. Start at the top-right corner of the matrix (`row = 0`, `col = cols - 1`).
        2. While `row` is within bounds and `col` is non-negative:
           - If the current element equals `target`, return True.
           - If the current element is greater than `target`, move left (`col -= 1`).
           - If the current element is less than `target`, move down (`row += 1`).
        3. If the loop ends, return False (target not found).

        I - Implement:
        '''

        # Time Complexity: O(m + n)
        # Space Complexity: O(1)
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1  # Start at top-right corner

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1  # Move left
            else:
                row += 1  # Move down

        return False

    # Alternative Solution
    # Time Complexity: O(log(m * n))
    # Space Complexity: O(1)
    def searchMatrixBinarySearch(self, matrix: List[List[int]], target: int) -> bool:
        '''
        1. Perform a binary search on the matrix as if it were a 1D list.
        2. Calculate the row and column indices from the 1D index.
        3. Compare the element at the calculated indices with the target.
        4. If the element equals the target, return True.
        5. If the element is less than the target, move the left pointer to the right.
        6. If the element is greater than the target, move the right pointer to the left.
        7. If the loop ends, return False (target not found).
        '''

        # Time Complexity: O(log(m * n))
        # Space Complexity: O(1)
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_val = matrix[mid // cols][mid % cols]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
# Example Usage:
'''
E - Evaluate:
1. Input: matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]], target = 5
   Output: True
   Explanation:
   - Start at (0, 2): 7 > 5, move left to (0, 1).
   - At (0, 1): 4 < 5, move down to (1, 1).
   - At (1, 1): 5 == 5, return True.

2. Input: matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]], target = 10
   Output: False
   Explanation:
   - Start at (0, 2): 7 < 10, move down to (1, 2).
   - At (1, 2): 8 < 10, move down to (2, 2).
   - At (2, 2): 9 < 10, move down to out of bounds, return False.

3. Edge Case: matrix = [[1]], target = 1
   Output: True

Time Complexity:
- O(m + n): In the worst case, we traverse at most `m` rows and `n` columns.

Space Complexity:
- O(1): No additional space is used.
'''

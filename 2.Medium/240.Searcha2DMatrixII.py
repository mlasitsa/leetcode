class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Solution 1: Binary Search on Each Row
        U - Understand:
        - Problem: Given an `m x n` matrix, determine if a `target` exists in the matrix.
          The matrix has the following properties:
            1. Integers in each row are sorted in ascending order from left to right.
            2. Integers in each column are sorted in ascending order from top to bottom.
        - Approach: Perform binary search on each row to find the target.

        M - Match:
        - Use **binary search** to search for the target in each row.

        P - Plan:
        1. Define a helper function `binarySearch(nums)` to perform binary search on a row:
           - Initialize `left` and `right` pointers.
           - Calculate the mid-point, compare with `target`, and adjust pointers accordingly.
           - Return True if `target` is found, else return False.
        2. Iterate through each row in the matrix:
           - Call `binarySearch` on the current row.
           - If `binarySearch` returns True, return True.
        3. If no match is found after checking all rows, return False.

        I - Implement:
        '''
        def binarySearch(nums):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return True
            return False

        for i in range(len(matrix)):
            if binarySearch(matrix[i]):
                return True
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Solution 2: Two-Pointer Approach (Start from Top-Right)
        U - Understand:
        - Problem: Same as above.
        - Approach: Use a two-pointer approach starting at the top-right corner.

        M - Match:
        - Use a **greedy algorithm** to eliminate rows or columns based on the value at the current position.

        P - Plan:
        1. Initialize `row` to 0 and `col` to the last column (top-right corner).
        2. While `row` and `col` are within bounds:
           - Compare the current value `matrix[row][col]` with `target`.
           - If `matrix[row][col] == target`, return True.
           - If `matrix[row][col] > target`, move left (`col -= 1`).
           - If `matrix[row][col] < target`, move down (`row += 1`).
        3. If the loop ends without finding the target, return False.

        I - Implement:
        '''
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            val = matrix[row][col]

            if val == target:
                return True

            if val > target:
                col -= 1
            else:
                row += 1

        return False

# Example Usage:
'''
E - Evaluate:
Solution 1: Binary Search on Each Row
1. Input: matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]], target = 9
   Output: True
   Explanation:
   - Binary search row 0: No match.
   - Binary search row 1: Match found at column 1.
   - Return True.

2. Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], target = 10
   Output: False
   Explanation:
   - Binary search all rows: No match.
   - Return False.

Solution 2: Two-Pointer Approach
1. Input: matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]], target = 9
   Output: True
   Explanation:
   - Start at top-right: 5 < 9, move down to 9. Match found.
   - Return True.

2. Input: matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]], target = 10
   Output: False
   Explanation:
   - Traverse to bottom-left corner without finding the target.
   - Return False.

Time Complexity:
- Solution 1: O(m * log(n)) (binary search on each row).
- Solution 2: O(m + n) (at most `m + n` moves in the matrix).

Space Complexity:
- Both solutions: O(1).
'''

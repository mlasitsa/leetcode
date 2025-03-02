class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a sorted array `nums` and a `target` value, return the index of `target` if it exists in `nums`.
        - If `target` is not in `nums`, return -1
        
        Clarifications/Constraints:
        - The array `nums` is sorted in ascending order.
        - `nums` contains distinct integers.
        - The input size can be large, so an efficient approach is preferred.
        - What if `nums` is empty? (Return -1)
        - What if `target` is at the beginning or end of the array?
        - Are negative numbers allowed? (Yes, as long as the array is sorted)
        - Should the function modify the input array? (No, just search)

        Examples:
        Input: nums = [-1, 0, 3, 5, 9, 12], target = 9 -> Output: 4
        Input: nums = [-1, 0, 3, 5, 9, 12], target = 2 -> Output: -1
        Input: nums = [5], target = 5 -> Output: 0
        """

        """
        M - Match with Patterns
        Observations:
        - The array is **sorted**, which suggests **binary search**
        - Binary search is an efficient way to search in a sorted array (O(log N) time complexity).
        - The problem does not require modification of `nums`, so an iterative or recursive binary search will work.

        Approach:
        - Use **binary search**:
          - Set two pointers, `left` at the beginning and `right` at the end.
          - Calculate the `mid` index.
          - Compare `nums[mid]` with `target`:
            - If `nums[mid] == target`, return `mid`.
            - If `nums[mid] > target`, search in the left half.
            - If `nums[mid] < target`, search in the right half.
          - Repeat until `left` crosses `right`.
          - If no match is found, return -1.
        """

        """
        P - Plan
        1. Initialize `left` at 0 and `right` at len(nums) - 1.
        2. Use a `while` loop to continue searching while `left` <= `right`:
           - Compute `mid` as the middle index.
           - If `nums[mid] == target`, return `mid`.
           - If `nums[mid] > target`, move `right` to `mid - 1`.
           - If `nums[mid] < target`, move `left` to `mid + 1`.
        3. If no match is found, return -1.
        """

        # I - Implement
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

        """
        R - Review
        - Check edge cases:
          - nums is empty -> should return -1.
          - nums has only one element, which is `target` -> should return 0.
          - `target` is at the first or last position -> should return correct index.
          - `target` does not exist in `nums` -> should return -1.
        """

        """
        E - Evaluate
        Time Complexity:
        - O(log N): Binary search reduces the search space by half in each step.

        Space Complexity:
        - O(1): No extra space is used apart from a few integer variables.

        Edge Cases:
        1. nums = [], target = 3 -> Output: -1 (Empty list)
        2. nums = [5], target = 5 -> Output: 0 (Single element, match)
        3. nums = [5], target = 2 -> Output: -1 (Single element, no match)
        4. nums = [1, 2, 3, 4, 5, 6], target = 6 -> Output: 5 (Target at the end)
        5. nums = [1, 2, 3, 4, 5, 6], target = 0 -> Output: -1 (Target less than min)
        """

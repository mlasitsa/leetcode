class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        U - Understand:
        - Problem: You are given an array `nums` where each element represents the maximum jump length at that position.
          Determine if you can reach the last index starting from the first index.
        - Clarifications/Constraints:
          1. `nums` is non-empty, and contains at least one element.
          2. Each element is a non-negative integer.
          3. If the array contains one element, the answer is always True.

        Examples:
        - Input: nums = [2, 3, 1, 1, 4]
          Output: True
          Explanation: Jump 2 steps to index 1, then 3 steps to the last index.

        - Input: nums = [3, 2, 1, 0, 4]
          Output: False
          Explanation: Stuck at index 3, cannot reach index 4.

        M - Match:
        - This is a **greedy problem**, where we try to keep track of the furthest reachable index as we iterate through the array.
        - If at any index `i`, we can't reach it (i.e., `i > maxLen`), we return False.

        P - Plan:
        1. Initialize a variable `maxLen` to 0 to track the furthest index reachable.
        2. Iterate through the array:
           - If the current index `i` exceeds `maxLen`, return False.
           - Update `maxLen` as the maximum of its current value and `i + nums[i]`.
           - If `maxLen` is greater than or equal to the last index, return True.
        3. If the loop completes, return False (in case we can't reach the end).

        I - Implement:
        """
        maxLen = 0
        
        for i in range(len(nums)):
            # If we can't reach this index, we are stuck
            if i > maxLen:
                return False

            # Update the furthest reachable index
            maxLen = max(maxLen, i + nums[i])

            # If we've already reached or surpassed the last index, return True
            if maxLen >= len(nums) - 1:
                return True

        return False

# Example Usage:
"""
E - Evaluate:
1. Input: nums = [2, 3, 1, 1, 4]
   Output: True
   Explanation:
   - Start at index 0: maxLen = max(0, 0 + 2) = 2.
   - At index 1: maxLen = max(2, 1 + 3) = 4.
   - At index 2: maxLen = max(4, 2 + 1) = 4.
   - Since maxLen >= 4 (last index), return True.

2. Input: nums = [3, 2, 1, 0, 4]
   Output: False
   Explanation:
   - Start at index 0: maxLen = max(0, 0 + 3) = 3.
   - At index 1: maxLen = max(3, 1 + 2) = 3.
   - At index 2: maxLen = max(3, 2 + 1) = 3.
   - At index 3: maxLen = max(3, 3 + 0) = 3.
   - Cannot reach index 4; return False.

Time Complexity: O(n) (Single pass through the array)
Space Complexity: O(1) (Constant extra space)
"""

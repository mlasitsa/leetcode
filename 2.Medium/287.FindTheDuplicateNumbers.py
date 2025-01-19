class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """

       !!! IS NOT OPTIMAL, FOR MEDIUM SPACE SHOULD BE O(1) !!!

        U - Understand the Problem
        Problem Statement:
        - Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]`.
        - There is only one duplicate number in the array, but it can appear more than once.
        - Find and return the duplicate number.

        Clarifications/Constraints:
        - The input array contains at least one duplicate.
        - The array is read-only; modification of input is not allowed.
        - Must use O(1) extra space and constant additional memory.

        Examples:
        Input: nums = [1, 3, 4, 2, 2] -> Output: 2
        Input: nums = [3, 1, 3, 4, 2] -> Output: 3

        Potential clarifying questions for an interview:
        1. Are there any constraints on the size of the input array? (No specific constraints, but fits in memory.)
        2. What if there are multiple duplicates? (Guaranteed only one duplicate.)
        3. Should the result include all duplicates? (No, return only one duplicate.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a set to track numbers already seen:
        #   * Iterate through the array, adding numbers to the set.
        #   * If a number is already in the set, return it as the duplicate.

        """
        P - Plan
        1. Initialize an empty set `seen` to track numbers.
        2. Iterate through the array:
           - If the current number exists in `seen`, return it as the duplicate.
           - Otherwise, add the current number to `seen`.
        3. If the loop completes without finding a duplicate (shouldn't happen per constraints), return -1.
        """

        seen = set()  # Step 1: Initialize an empty set to track seen numbers
        for num in nums:  # Step 2: Iterate through the array
            if num in seen:  # If the number is already in the set, it's the duplicate
                return num
            seen.add(num)  # Add the number to the set if not already present

        # This line is not expected to be reached due to problem constraints
        return -1

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: nums = [1, 3, 4, 2, 2] -> Output: 2
2. Input: nums = [3, 1, 3, 4, 2] -> Output: 3
3. Input: nums = [1, 1] -> Output: 1

Edge Cases:
1. Minimum size array (e.g., [1, 1]) -> Output: Duplicate number.
2. Duplicate at the beginning or end of the array -> Ensure correct detection.
3. Large array with many duplicates -> Ensure efficiency.

Time Complexity:
- O(n): Each number is visited once.

Space Complexity:
- O(n): Space required to store the `seen` set.
"""

sol = Solution()
res = sol.findDuplicate([1, 3, 4, 2, 2])

if res == 2:
    print("Good Job")
else:
    print("Try Again...")

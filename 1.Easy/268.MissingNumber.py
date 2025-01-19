class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the missing number.
        - The array is guaranteed to have one missing number.

        Clarifications/Constraints:
        - The array has no duplicates.
        - It contains only integers in the range `[0, n]`.
        - Exactly one number is missing.

        Examples:
        Input: nums = [3, 0, 1]
        Output: 2

        Input: nums = [0, 1]
        Output: 2

        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8

        Potential clarifying questions for an interview:
        1. Can the input array be empty? (No, it's guaranteed to have `n` numbers with one missing.)
        2. Are there negative numbers or duplicates? (No, only integers in the range `[0, n]`.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use the sum formula for the first `n` natural numbers: `sum = n * (n + 1) / 2`.
        # - Subtract the sum of the array elements from this total sum to find the missing number.

        """
        P - Plan
        1. Handle edge case: If 0 is missing, return 0.
        2. Calculate the expected sum of numbers from 0 to `n` using the formula.
        3. Calculate the actual sum of the numbers in the input array.
        4. Compare the two sums:
           - If they are equal, the missing number is `n`.
           - Otherwise, return the difference between the expected sum and the actual sum.
        """

        def findMax(nums):
            """Helper function to find the maximum number in the array."""
            maxNum = float("-inf")
            for num in nums:
                maxNum = max(maxNum, num)
            return maxNum

        # Step 1: Find the maximum number in the array
        maxNum = findMax(nums)

        def calculateSum(maxNum):
            """Helper function to calculate the sum of numbers from 0 to maxNum."""
            summ = 0
            for i in range(0, maxNum + 1):
                summ += i
            return summ

        # Step 2: Calculate the expected sum
        summ = calculateSum(maxNum)

        # Step 3: Calculate the actual sum of the array
        summ2 = sum(nums)

        # Step 4: Determine the missing number
        if 0 not in nums:
            return 0  # Case where 0 is the missing number
        elif summ == summ2:
            return maxNum + 1  # Case where the missing number is beyond the current maximum
        else:
            return summ - summ2  # Case where the missing number is within the range

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: nums = [3, 0, 1] -> Output: 2
2. Input: nums = [0, 1] -> Output: 2
3. Input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1] -> Output: 8

Edge Cases:
1. Missing number is 0 -> Correctly return 0.
2. Missing number is `n` -> Correctly return `n`.
3. Single-element array -> Correctly identify missing number.

Time Complexity:
- O(n): Traverse the array twice (once for `findMax` and once for the actual sum).

Space Complexity:
- O(1): No extra data structures are used.
"""

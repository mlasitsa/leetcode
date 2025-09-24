class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given an integer array `nums`, find the contiguous subarray (containing at least one number) that has the **largest sum**.
        - Return the **maximum sum** found.

        Constraints:
        - `nums` may contain negative, positive, or zero values.
        - A subarray is **contiguous**, meaning we can't pick elements from random positions.
        - The array contains **at least one** element.

        Clarifications:
        - What if `nums` contains all negative numbers? ➝ Pick the **largest single negative number**.
        - What if `nums` has only one element? ➝ Return that single element.
        - What if `nums` contains only zeroes? ➝ Return `0`.

        Examples:
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: The subarray `[4, -1, 2, 1]` has the **largest sum** of `6`.

        Input: nums = [1]
        Output: 1

        Input: nums = [5,4,-1,7,8]
        Output: 23
        Explanation: The entire array is the largest subarray.

        Edge Cases:
        - `nums = [-1, -2, -3, -4]` → Output: `-1` (Pick the least negative number)
        - `nums = [0, 0, 0, 0]` → Output: `0`
        """

        # M - Match with Patterns
        """
        - **Dynamic Programming** approach:
          - Define `dp[i]` as the **maximum subarray sum ending at index `i`**.
          - Transition:
            - `dp[i] = max(dp[i-1] + nums[i], nums[i])`
            - We either extend the previous subarray or start a new one.
          - The answer is `max(dp)`.

        - **Kadane’s Algorithm (Optimized DP):**
          - Instead of maintaining a full `dp` array, we can use **two variables**:
            - `currentSum`: Tracks the maximum sum **ending at** `i`.
            - `maxSum`: Stores the **global maximum subarray sum**.
        """

        # P - Plan
        """
        1. Handle **edge case**: If `nums` is empty, return `0`.
        2. Initialize `dp` array where `dp[0] = nums[0]`.
        3. Iterate over `nums`, updating `dp[i]`:
           - `dp[i] = max(dp[i-1] + nums[i], nums[i])`
        4. Return `max(dp)` as the final answer.
        """

        if not nums:
            return 0  # Edge case: Empty array

        dp = [0] * len(nums)  # Step 2: Initialize DP array
        dp[0] = nums[0]  # First element is its own max

        for i in range(1, len(nums)):  # Step 3: Iterate and update DP
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)  # Step 4: Return the max sum found

        """
        I - Implement
        ✅ Uses **Dynamic Programming** with **O(N) time complexity**.
        ✅ Works for negative numbers.
        ✅ Avoids unnecessary brute force computations.

        R - Review
        ✅ Correctly computes **maximum subarray sum**.
        ✅ Handles all edge cases (negative values, single element, etc.).
        ✅ O(N) space complexity due to `dp` array.

        E - Evaluate
        Time Complexity: **O(N)** → One pass through `nums`.
        Space Complexity: **O(N)** → Due to `dp` array (can be optimized).

        Optimization:
        - Instead of using `dp[]`, we can use two **variables** (`maxSum` and `currentSum`) for **O(1) space**.
        """



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
          Weird way but also works, I tired ignoring DP for some reason lol
          stall passed though
        '''
        summ = nums[0]
        maxSumm = nums[0]
        for i in range(len(nums)):
            summ = max(nums[i], summ + nums[i])
            maxSumm = max(maxSumm, summ)
        return maxSumm
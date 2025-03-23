class Solution:
    """
    U - Understand the Problem
    ------------------------------------
    Problem Statement:
    - You are a professional robber planning to rob houses along a street.
    - Each house has some amount of money stashed, the only constraint is:
      you cannot rob two adjacent houses.
    - Return the maximum amount of money you can rob without alerting the police.

    Examples:
    - Input: nums = [1,2,3,1] -> Output: 4 (rob 1 and 3)
    - Input: nums = [2,7,9,3,1] -> Output: 12 (rob 2, 9, 1)

    Edge Cases:
    - Empty list → 0
    - One house → nums[0]
    - Two houses → max(nums[0], nums[1])
    """

    """
    M - Match
    ------------------------------------
    This is a classic **Dynamic Programming** problem:
    - Recurrence: At index `i`, you can choose to:
      1. Rob the house (nums[i] + dp[i+2])
      2. Skip the house (dp[i+1])
    - Base cases and transitions match well with DP.
    """

    # Pure Recursion (Exponential)
    def rob_recursive(self, nums):
        def helper(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + helper(i + 2), helper(i + 1))
        return helper(0)

    # Memoization (Top-down DP) - O(n) time, O(n) space
    def rob_memo(self, nums):
        memo = [-1] * len(nums)
        def helper(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + helper(i + 2), helper(i + 1))
            return memo[i]
        return helper(0)

    # Tabulation (Bottom-up DP) - O(n) time, O(n) space
    def rob_tabulation(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]

    # Space-Optimized DP - O(n) time, O(1) space
    def rob_optimized(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev = nums[0]
        cur = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = max(nums[i] + prev, cur)
            prev = cur
            cur = temp
        return cur

    """
    P - Plan
    ------------------------------------
    Use dynamic programming to store max loot up to each house:
    - Base Cases:
      dp[0] = nums[0]
      dp[1] = max(nums[0], nums[1])
    - Transition:
      dp[i] = max(nums[i] + dp[i-2], dp[i-1])

    I - Implement: (Above)

    R - Review
    ------------------------------------
    - Pure recursion = exponential, bad for large inputs
    - Memoization avoids recomputation
    - Tabulation iteratively builds solution
    - Optimized DP saves space by storing only last two values

    E - Evaluate
    ------------------------------------
    Time Complexity:
    - Recursion: O(2^n)
    - Memoization: O(n)
    - Tabulation: O(n)
    - Optimized DP: O(n)

    Space Complexity:
    - Recursion: O(n) stack
    - Memoization: O(n)
    - Tabulation: O(n)
    - Optimized DP: O(1)
    """

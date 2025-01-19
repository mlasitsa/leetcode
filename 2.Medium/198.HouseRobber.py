class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - A thief is deciding which houses to rob along a street.
        - Each house has a certain amount of money stashed.
        - The thief cannot rob two adjacent houses (to avoid alerting the police).
        - Determine the maximum amount of money the thief can rob without robbing two consecutive houses.

        Examples:
        Input: nums = [1,2,3,1]
        Output: 4
        Explanation:
        - Rob house 1 (money = 1) and house 3 (money = 3).
        - Total money = 1 + 3 = 4.

        Input: nums = [2,7,9,3,1]
        Output: 12
        Explanation:
        - Rob house 1 (money = 2), house 3 (money = 9), and house 5 (money = 1).
        - Total money = 2 + 9 + 1 = 12.

        Clarifications/Constraints:
        1. Can `nums` be empty? (Yes, return 0 in that case.)
        2. What if there’s only one house? (Return the value of that house.)
        3. Will there always be at least one house? (Yes, per constraints.)
        4. Negative values? (No, all values are non-negative.)

        Constraints:
        - 1 <= len(nums) <= 10^4
        - 0 <= nums[i] <= 10^4
        """

        """
        M - Match with Patterns
        Pattern Identified:
        - This is a classic **Dynamic Programming (DP)** problem.
        - At each house `i`, the thief has two options:
          1. Skip the house: Total money is the same as `dp[i-1]`.
          2. Rob the house: Total money is `nums[i] + dp[i-2]`.
        - Use a DP array to store the maximum money the thief can rob up to each house.
        """

        """
        P - Plan
        1. Handle edge cases:
           - If `nums` is empty, return 0.
           - If `nums` has only one house, return `nums[0]`.
        2. Initialize a DP array:
           - `dp[i]` represents the maximum money the thief can rob up to house `i`.
           - `dp[0] = nums[0]`: Rob the first house.
           - `dp[1] = max(nums[0], nums[1])`: Rob the house with more money.
        3. Iterate through the remaining houses:
           - For each house `i`, calculate:
             `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.
           - This chooses the maximum between robbing house `i` and skipping it.
        4. Return `dp[-1]`: The maximum money that can be robbed.
        """

        # Edge case: if nums is empty
        if len(nums) == 0:
            return 0

        # Edge case: if nums has only one house
        if len(nums) == 1:
            return nums[0]

        # Step 2: Initialize DP array
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Step 3: Iterate through remaining houses
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # Step 4: Return the maximum amount robbed
        return dp[-1]

# Example Usage:
"""
E - Evaluate
Test the solution with examples:
1. Input: nums = [1, 2, 3, 1]
   Output: 4
   Explanation:
   - Rob house 1 (money = 1) and house 3 (money = 3).
   - Total money = 1 + 3 = 4.

2. Input: nums = [2, 7, 9, 3, 1]
   Output: 12
   Explanation:
   - Rob house 1 (money = 2), house 3 (money = 9), and house 5 (money = 1).
   - Total money = 2 + 9 + 1 = 12.

Time Complexity:
- Iterating through the houses: O(n).
- Total: O(n).

Space Complexity:
- Storing the DP array: O(n).

Can we optimize? (Yes, by using only two variables to store the previous states.)
YOU CAN TRY YOURSELF :)
"""

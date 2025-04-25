class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        U - Understand the Problem
        ----------------------------------
        Problem:
        - Houses are arranged in a circle.
        - You cannot rob two adjacent houses.
        - First and last houses are neighbors, so you can’t rob both.

        Goal:
        - Return the maximum amount you can rob without triggering the alarm.

        Edge Cases:
        - Empty list → return 0
        - One house → return its value
        - Two houses → return max of them

        M - Match
        ----------------------------------
        Pattern:
        - Classic House Robber DP (linear) + circular condition
        - Dynamic Programming with two subproblems:
          1. Exclude first house (rob from 1 to n-1)
          2. Exclude last house (rob from 0 to n-2)

        P - Plan
        ----------------------------------
        1. Handle base cases for 0 or 1 house.
        2. Define a helper function `rob_linear()` that solves the classic House Robber I problem.
        3. Compute:
            - Max from robbing houses 0 to n-2
            - Max from robbing houses 1 to n-1
        4. Return the greater of the two.

        I - Implement
        ----------------------------------
        """

        dp = [0] * len(nums)

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        # Helper function to perform the regular house robber problem on a linear array
        def rob_linear(houses):
            if len(houses) == 1:
                return houses[0]

            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
            
            return dp[-1]

        # Case 1: Rob from house 0 to n-2 (exclude last house)
        case1 = rob_linear(nums[0:len(nums) - 1])
        
        # Case 2: Rob from house 1 to n-1 (exclude first house)
        case2 = rob_linear(nums[1:])

        # Return the maximum of both cases
        return max(case1, case2)

        """
        R - Review
        ----------------------------------
        - Handles circular restriction by trying two subranges
        - Uses a helper DP approach for the linear problem
        - All edge cases are addressed

        E - Evaluate
        ----------------------------------
        Time Complexity: O(n)
        - Each rob_linear call traverses up to n elements
        - Two calls total → O(n)

        Space Complexity: O(n)
        - Due to DP arrays used in both subproblems

        Optimization:
        - Can reduce space to O(1) by tracking only last two values (Space Optimized DP)
        """

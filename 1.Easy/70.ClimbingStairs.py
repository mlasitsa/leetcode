class Solution:
    def climbStairs(self, n: int) -> int:
        """
        U - Understand the Problem
        - You are climbing a staircase. Each time you can take either 1 or 2 steps.
        - Given `n` is the total number of steps, return the number of distinct ways to climb to the top.

        Examples:
        - Input: n = 2 → Output: 2  (1+1, 2)
        - Input: n = 3 → Output: 3  (1+1+1, 1+2, 2+1)

        Constraints:
        - 1 <= n <= 45
        """

        """
        M - Match
        - This is a classic **Dynamic Programming** problem.
        - We notice the recurrence relation: f(n) = f(n-1) + f(n-2)
        - Similar to Fibonacci numbers.
        """

        """
        P - Plan
        We'll implement 4 different solutions:
        1. Naive Recursion (Exponential Time)
        2. DP with memoization (Top-down)
        3. DP with tabulation (Bottom-up)
        4. Optimized DP (O(1) space)
        """

        # Naive Recursion (Exponential Time)
        def climb_recursive(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            return climb_recursive(n - 1) + climb_recursive(n - 2)

        # return climb_recursive(n)


        # Top-down DP with Memoization (O(n) time, O(n) space)
        memo = {}
        def climb_memo(n):
            if n in memo:
                return memo[n]
            if n <= 1:
                return 1
            memo[n] = climb_memo(n - 1) + climb_memo(n - 2)
            return memo[n]

        # return climb_memo(n)


        # Bottom-up DP with Tabulation (O(n) time, O(n) space)
        def climb_dp(n):
            if n == 1:
                return 1
            dp = [0] * n
            dp[0] = 1
            dp[1] = 2
            for i in range(2, n):
                dp[i] = dp[i - 1] + dp[i - 2]
            return dp[n - 1]

        # return climb_dp(n)


        # Space-Optimized DP (O(n) time, O(1) space)
        def climb_optimized(n):
            if n == 1:
                return 1
            prev, cur = 1, 2
            for i in range(2, n):
                num = prev + cur
                prev = cur
                cur = num
            return cur


        """
        R - Review
        All approaches implement the same recurrence relation f(n) = f(n-1) + f(n-2)

        E - Evaluate
        Time Complexity:
        - Naive recursion: O(2^n)
        - Memoization: O(n)
        - Tabulation: O(n)
        - Space optimized: O(n) time, O(1) space

        Space Complexity:
        - Naive recursion: O(n) call stack
        - Memoization: O(n)
        - Tabulation: O(n)
        - Optimized: O(1)
        """

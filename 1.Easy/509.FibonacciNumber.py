# ========================================================
# U - Understand the Problem
# ========================================================
# Problem Statement:
# Calculate the nth Fibonacci number where:
# F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n >= 2

# Constraints:
# - 0 <= n <= 30 (for most LeetCode versions of this problem)
# - Input is always valid
# - May require optimization for larger values of n

# Clarifying Questions:
# - Should we optimize for time, space, or both?
# - Can we use caching or libraries?
# - What should F(0) and F(1) return? (Given.)

# ========================================================
# M - Match with Patterns
# ========================================================
# Pattern: Dynamic Programming (DP) / Recursion with Memoization
# Choices:
# - Pure recursion (brute force)
# - Recursion with memoization (top-down DP)
# - Bottom-up dynamic programming (tabulation)
# - Space-optimized DP

# ========================================================
# P - Plan + I - Implement
# ========================================================

# Brute Force Recursive (Exponential Time)
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

# Time Complexity: O(2^n) — exponential due to repeated subproblems
# Space Complexity: O(n) — recursion stack
# Not optimal for large n (TLE)

# --------------------------------------------------------

# Top-Down DP with Manual Memoization (Dictionary Cache)
class Solution:
    def fib(self, n: int) -> int:
        hmap = {0: 0, 1: 1}

        def helper(n):
            if n in hmap:
                return hmap[n]
            hmap[n] = helper(n - 1) + helper(n - 2)
            return hmap[n]

        return helper(n)

# Time Complexity: O(n)
# Space Complexity: O(n) for recursion stack and memo dictionary
# Great balance of clarity and efficiency

# --------------------------------------------------------

# Bottom-Up Dynamic Programming (Tabulation)
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Simple and avoids recursion, great for interview

# --------------------------------------------------------

# Space Optimized Iterative DP
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        prev = 0
        cur = 1

        for _ in range(2, n + 1):
            prev, cur = cur, prev + cur
        return cur if n > 0 else prev

# Time Complexity: O(n)
# Space Complexity: O(1)
# Most optimal solution in terms of both time and space

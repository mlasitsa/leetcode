# ✅ 1. Pure Recursion (Top-Down, No Memoization)
def minCostClimbingStairs_recursive(cost):
    """
    U - Understand:
    - Start from index 0 or 1.
    - You can climb 1 or 2 steps at a time.
    - Cost is paid at each step.
    - Goal: Reach the top (beyond last index) with minimum cost.

    M - Match:
    - Classic recursion tree with overlapping subproblems.

    P - Plan:
    - Try both paths (1 step, 2 steps) recursively.
    - Base case: If beyond length, cost is 0.

    I - Implement:
    """
    def helper(i):
        if i >= len(cost):
            return 0
        return cost[i] + min(helper(i + 1), helper(i + 2))
    
    return min(helper(0), helper(1))

    """
    R - Brute force, highly redundant calls.

    E - Time: O(2^n), Space: O(n) call stack
    """


# ✅ 2. Recursion + Memoization (Top-Down DP)
def minCostClimbingStairs_memo(cost):
    """
    M - Add memo array to store computed results.

    P - Same as recursion, but avoid recomputation.

    I - Implement:
    """
    memo = [-1] * len(cost)

    def helper(i):
        if i >= len(cost):
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = cost[i] + min(helper(i + 1), helper(i + 2))
        return memo[i]
    
    return min(helper(0), helper(1))

    """
    R - Optimized recursion

    E - Time: O(n), Space: O(n)
    """


# ✅ 3. Tabulation (Bottom-Up DP)
def minCostClimbingStairs_tab(cost):
    """
    M - Bottom-up solution

    P - dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

    I - Implement:
    """
    n = len(cost)
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    return dp[n]

    """
    E - Time: O(n), Space: O(n)
    """


# ✅ 4. Space-Optimized DP (O(1) Space)
def minCostClimbingStairs_optimized(cost):
    """
    M - Only need two variables instead of dp array

    P - Track prev1 and prev2 and update at each step

    I - Implement:
    """
    prev2, prev1 = 0, 0  # Correspond to dp[i-2], dp[i-1]

    for i in range(2, len(cost) + 1):
        curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        prev2, prev1 = prev1, curr

    return prev1

    """
    E - Time: O(n), Space: O(1)
    """

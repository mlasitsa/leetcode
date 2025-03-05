# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - You are given `n` versions (1 to n).
        - There exists a function `isBadVersion(version)` that tells if a version is bad.
        - Find the first bad version **in the most efficient way possible**.

        Constraints:
        - `1 <= bad <= n <= 2^31 - 1` (Large input size, needs an efficient solution).
        - Calling `isBadVersion(version)` should be minimized.

        Example:
        Input: `n = 5, bad = 4`
        Output: `4`
        Explanation:
        - `isBadVersion(1) -> False`
        - `isBadVersion(2) -> False`
        - `isBadVersion(3) -> False`
        - `isBadVersion(4) -> True` (First bad version)

        Edge Cases:
        - `n = 1`: Only one version, return 1 if bad.
        - First version is bad (`bad = 1`).
        - All versions are good (`bad = n + 1` is invalid in constraints).
        """

        # M - Match with Patterns
        """
        - This is a **search problem** where we need to find the first bad version.
        - Since the versions are **sorted (good → bad)**, **Binary Search** is a good choice.
        - Binary search helps reduce unnecessary calls to `isBadVersion()`.
        """

        # P - Plan
        """
        Approach: **Binary Search**
        1. Initialize `left = 1` and `right = n`.
        2. While `left < right`:
           - Compute `mid = (left + right) // 2`.
           - If `isBadVersion(mid) == False`: Move `left` to `mid + 1` (bad version is further right).
           - Else: Move `right` to `mid` (bad version is in left half).
        3. Return `left` when `left == right` (smallest bad version).
        """

        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if not isBadVersion(mid):  # Mid is a good version, move right boundary
                left = mid + 1
            else:  # Mid is bad, potential first bad version found, move left boundary
                right = mid

        return left  # Left is now the first bad version

        """
        R - Review
        - Uses **binary search**, reducing search space from `O(N)` to `O(log N)`.
        - Minimizes API calls to `isBadVersion()`.
        - Works correctly for edge cases like `n=1` and `bad=1`.

        E - Evaluate
        Time Complexity: **O(log N)** (Binary search halves the search space each step).
        Space Complexity: **O(1)** (Constant extra space used).
        
        Edge Cases:
        - `n = 1, bad = 1`: Should return `1`.
        - `n = 1000000, bad = 999999`: Should return `999999`.
        - `n = 10, bad = 10`: Should return `10`.

        Optimizations:
        - We could use `left <= right`, but `left < right` avoids extra checks.
        - Ensuring `right = mid` instead of `right = mid - 1` prevents skipping the first bad version.
        """

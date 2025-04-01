class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
        U - Understand:
        ------------------
        Problem:
        - Count the number of lexicographically sorted strings of length `n` using only vowels ["a", "e", "i", "o", "u"].
        - A string is lexicographically sorted if s[i] <= s[i+1] for all i.

        Clarifications:
        - Only vowels allowed: 5 characters max.
        - Strings must be non-decreasing.
        - Return number of such strings of length `n`.

        Examples:
        n = 1 → Output: 5  (["a", "e", "i", "o", "u"])
        n = 2 → Output: 15 (["aa", "ae", ..., "uu"])

        M - Match:
        ------------------
        - This is a **combinatorics + dynamic programming** problem.
        - Can be modeled as a 2D DP matrix: dp[i][j] = number of ways to build string of length i using first j vowels.
        - Subproblem: At each level, we choose to either:
            - Extend a shorter string with current vowel.
            - Build using fewer vowels.

        P - Plan:
        ------------------
        1. Initialize a 2D matrix `dp` with size (n+1) x 5 (rows = lengths, cols = vowels).
        2. Base cases:
            - dp[0][j] = 1 (1 way to build empty string with any vowels)
            - dp[i][0] = 1 (Only 'a' is used → only 1 sorted string)
        3. Fill the table:
            - dp[i][j] = dp[i-1][j] + dp[i][j-1]
                - dp[i-1][j]: we add 1 more letter to previous string using j vowels
                - dp[i][j-1]: extend string using fewer vowels
        4. Return dp[n][4], the number of ways to build a string of length n using all 5 vowels.

        I - Implementation:
        ------------------
        """
        matrix = []
        for i in range(n + 1):
            row = [0] * 5
            matrix.append(row)

        for i in range(n + 1):
            matrix[i][0] = 1  # Only 'a' used
        for j in range(5):
            matrix[0][j] = 1  # Empty string

        for i in range(1, n + 1):
            for j in range(1, 5):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[n][4]

        """
        R - Review:
        ------------------
        - dp[i][j] = # of lexicographically sorted strings of length i using j+1 vowels
        - Built bottom-up with recurrence relation.

        E - Evaluate:
        ------------------
        Time Complexity: O(n * 5) → O(n)
        Space Complexity: O(n * 5) → O(n)
        - Optimizable to O(1) space with 1D array since we only use previous row and column
        """

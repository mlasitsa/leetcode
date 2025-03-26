class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        U - Understand the Problem
        --------------------------
        Problem: Given an unsigned integer, return the number of '1' bits it has 
        (also known as the Hamming weight).

        Input: An unsigned 32-bit integer `n`.
        Output: The number of bits set to '1' in its binary representation.

        Example:
        Input: n = 11 (binary: 1011)
        Output: 3

        Constraints:
        - We are dealing with 32-bit unsigned integers (e.g., 0 <= n <= 2^32 - 1).
        - The number is non-negative.

        M - Match with Patterns
        ------------------------
        This is a classic **bit manipulation** problem. There are multiple ways to solve:
        - Naively check bit-by-bit with modulo/division (your current approach).
        - Use `n & 1` and `n >> 1` for a more optimal binary check.
        - Use `n & (n - 1)` trick to count only the set bits.

        P - Plan
        --------
        - Initialize a `count` variable.
        - While `n` is not zero:
            - If the last bit is 1 (check with `n % 2 == 1`), increment the count.
            - Divide `n` by 2 (floor division) to drop the last bit.
        - Return the total count.

        I - Implement
        -------------
        Already implemented below.
        """

        count = 0
        while n != 0:
            if n % 2 == 1:
                count += 1
            n = n // 2
        return count

        """
        R - Review
        ----------
        - Works for all unsigned integers in 32-bit range.
        - Simple and readable implementation.

        E - Evaluate
        ------------
        Time Complexity: O(log n) — where n is the input number (log base 2 due to division).
        Space Complexity: O(1) — constant space used.

        Optimization:
        -------------
        Instead of using division and modulo, we can optimize this using bitwise operators:

        while n:
            count += n & 1
            n >>= 1

        OR the Brian Kernighan’s algorithm:

        while n:
            n &= (n - 1)
            count += 1

        This runs in O(number of 1 bits), which is faster when there are fewer 1s.
        """

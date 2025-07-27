class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        U - Understand the Problem
        --------------------------
        Problem Statement:
        - Given two binary strings `a` and `b`, return their sum as a binary string.
        - Binary addition must be performed manually, simulating bit-wise logic.

        Clarifications / Constraints:
        - Inputs are strings consisting only of '0' and '1'.
        - Return the result as a binary string.
        - Do not use built-in functions like `bin()` or `int(a, 2)`.

        Examples:
        a = "11", b = "1"       => Output: "100"
        a = "1010", b = "1011"  => Output: "10101"
        """

        """
        M - Match
        --------------------------
        This is a **Binary Addition / Two-Pointer** problem:
        - You need to simulate the binary addition bit-by-bit from right to left.
        - Use two pointers starting from the end of both strings and track carry.

        Common patterns:
        - Two-pointer
        - Carry management
        - Simulated arithmetic
        """

        # I - Implement
        carry = 0
        res = []
        
        idxA, idxB = len(a) - 1, len(b) - 1
        
        while idxA >= 0 or idxB >= 0 or carry == 1:
            if idxA >= 0:
                carry += int(a[idxA])
                idxA -= 1            
            if idxB >= 0:
                carry += int(b[idxB])
                idxB -= 1            

            res.append(str(carry % 2))
            carry = carry // 2
            
        return "".join(res[::-1])

        """
        P - Plan
        --------------------------
        1. Initialize two pointers at the ends of `a` and `b`.
        2. Initialize a carry = 0.
        3. Loop until both pointers are exhausted AND no carry is left.
        4. Add corresponding bits and carry.
        5. Append `carry % 2` to result.
        6. Update carry = carry // 2.
        7. Reverse result list and return as string.
        """

        """
        R - Review
        --------------------------
        Handles unequal string lengths
        Correctly manages carry over bits
        Appends from LSB to MSB then reverses
        Doesn't mutate input
        Handles edge case: a = "0", b = "0"
        """

        """
        E - Evaluate
        --------------------------
        Time Complexity:
        - O(max(len(a), len(b)))

        Space Complexity:
        - O(max(len(a), len(b))) to store result

        Edge Cases:
        - a = "0", b = "0"         => "0"
        - a = "1", b = "1111"      => "10000"
        - Large strings (10^4 bits) handled efficiently
        """

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        U - Understand the Problem
        Problem Statement:
        - Given two strings `str1` and `str2`, find the greatest common divisor (GCD) string that can be concatenated
          repeatedly to form both `str1` and `str2`.
        - If no such string exists, return an empty string.

        Clarifications/Constraints:
        - The GCD string must be a prefix of both strings.
        - The concatenation of the strings in either order (`str1 + str2` and `str2 + str1`) must be the same
          for a GCD string to exist.
        - If there is no GCD string, return "".

        Examples:
        Input: str1 = "ABCABC", str2 = "ABC" -> Output: "ABC"
        Input: str1 = "ABABAB", str2 = "ABAB" -> Output: "AB"
        Input: str1 = "LEET", str2 = "CODE" -> Output: ""

        Potential clarifying questions for an interview:
        1. Can the input strings contain non-alphabetic characters? (Assume yes.)
        2. Are the strings guaranteed to have a valid GCD string? (No, return "" if none exists.)
        3. Should the function handle large strings efficiently? (Yes.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Mathematical GCD concept can be applied here:
        #   * The GCD of two strings exists if and only if `str1 + str2 == str2 + str1`.
        #   * The length of the GCD string is equal to the GCD of the lengths of `str1` and `str2`.

        """
        P - Plan
        1. Check if `str1 + str2` is equal to `str2 + str1`. If not, return "" as there is no common divisor.
        2. Find the GCD of the lengths of `str1` and `str2`.
        3. Return the substring of `str1` from index 0 to `gcd_length` as the GCD string.
        """

        # Step 1: Check if concatenated strings are equal
        if str1 + str2 != str2 + str1:
            return ""

        # Step 2: Compute the GCD of the lengths of the strings
        gcd_length = gcd(len(str1), len(str2))

        # Step 3: Return the GCD substring
        return str1[:gcd_length]

# Example Usage
sol = Solution()

"""
E - Evaluate
Test the solution with examples:
1. Input: str1 = "ABCABC", str2 = "ABC" -> Output: "ABC"
2. Input: str1 = "ABABAB", str2 = "ABAB" -> Output: "AB"
3. Input: str1 = "LEET", str2 = "CODE" -> Output: ""

Edge Cases:
1. One of the strings is empty -> Output: ""
2. Both strings are the same -> Output: str1 (or str2)
3. No common divisor -> Output: ""

Time Complexity:
- O(n + m): String concatenation checks take O(n + m) where n and m are lengths of str1 and str2.
- GCD computation takes O(log(min(n, m))).

Space Complexity:
- O(1): Only uses a few variables for computation.
"""

res = sol.gcdOfStrings("ABCABC", "ABC")

if res == "ABC":
    print("Success!")
else:
    print("Fail...")

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
        - A string is a palindrome if it reads the same forward and backward after normalization.

        Clarifications/Constraints:
        - The input string may contain non-alphanumeric characters, which should be ignored.
        - Empty strings are considered palindromes.

        Examples:
        Input: s = "A man, a plan, a canal: Panama" -> Output: True
        Input: s = "race a car" -> Output: False
        Input: s = " " -> Output: True

        Potential clarifying questions for an interview:
        1. Should spaces and punctuation be ignored? (Yes, consider only alphanumeric characters.)
        2. Is the comparison case-sensitive? (No, convert to lowercase before comparison.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use two pointers to traverse the string from both ends.
        # - Skip non-alphanumeric characters using the `isalnum` method.
        # - Compare the lowercase versions of characters to ensure case insensitivity.

        """
        P - Plan
        1. Handle the edge case where the string is empty or has one character (return `True`).
        2. Initialize two pointers:
           - `left` at the start of the string.
           - `right` at the end of the string.
        3. Traverse the string:
           - Skip non-alphanumeric characters by incrementing/decrementing `left` and `right`.
           - Compare the lowercase values of characters pointed to by `left` and `right`.
           - If they are not equal, return `False`.
           - Move the pointers closer together.
        4. If the loop completes without mismatches, return `True`.
        """

        # Step 1: Handle edge cases for empty or single-character strings
        if len(s) == 0 or len(s) == 1:
            return True

        # Step 2: Initialize pointers
        left = 0
        right = len(s) - 1

        # Step 3: Traverse the string
        while left < right:
            # Skip non-alphanumeric characters
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            # Move pointers closer
            left += 1
            right -= 1

        # Step 4: Return True if no mismatches are found
        return True

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: s = "A man, a plan, a canal: Panama" -> Output: True
2. Input: s = "race a car" -> Output: False
3. Input: s = " " -> Output: True

Edge Cases:
1. Empty string -> Output: True.
2. String with only spaces -> Output: True.
3. String with mixed alphanumeric and punctuation -> Correctly ignore non-alphanumeric.

Time Complexity:
- O(n): Traverse the string once.

Space Complexity:
- O(1): Use constant space with two pointers.
"""

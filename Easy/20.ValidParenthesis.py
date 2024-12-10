class Solution:
    def isValid(self, s: str) -> bool:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a string `s` containing only the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        - A string is valid if:
          1. Open brackets are closed by the same type of brackets.
          2. Open brackets are closed in the correct order.

        Clarifications/Constraints:
        - The string may be empty. If it is, return `True`.
        - The string length does not exceed 10^4.

        Examples:
        Input: s = "()" -> Output: True
        Input: s = "()[]{}" -> Output: True
        Input: s = "(]" -> Output: False

        Potential clarifying questions for an interview:
        1. Can the string be empty? (Yes, an empty string is considered valid.)
        2. Can there be mismatched or unbalanced parentheses? (Yes, the function should return `False` in such cases.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a stack to keep track of opening brackets.
        # - For every closing bracket, check if it matches the last opening bracket.
        # - If the stack is empty at the end, the string is valid.

        """
        P - Plan
        1. Handle the edge case where the string is empty (return `True`).
        2. Use a dictionary to map closing brackets to their corresponding opening brackets.
        3. Initialize an empty stack.
        4. Traverse each character in the string:
           - If the character is a closing bracket:
             - Check if the stack is not empty and its top matches the corresponding opening bracket.
             - If not, return `False`.
             - If it matches, pop the stack.
           - If the character is an opening bracket, push it onto the stack.
        5. After traversal, return `True` if the stack is empty (all brackets matched).
        """

        # Step 1: Dictionary to map closing brackets to opening brackets
        closeToOpen = {")": "(", "}": "{", "]": "["}
        stack = []

        # Step 4: Traverse the string
        for ch in s:
            if stack and ch in closeToOpen:  # If the character is a closing bracket
                # Check if the top of the stack matches
                if closeToOpen[ch] != stack[-1]:
                    return False  # Mismatch found
                stack.pop()  # Match found, pop the stack
            else:
                # Push opening brackets onto the stack
                stack.append(ch)

        # Step 5: Return True if the stack is empty
        return not stack

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: s = "()" -> Output: True
2. Input: s = "()[]{}" -> Output: True
3. Input: s = "(]" -> Output: False
4. Input: s = "{[()]}" -> Output: True
5. Input: s = "" -> Output: True

Edge Cases:
1. Empty string -> Output: True.
2. Single closing bracket -> Output: False.
3. Mismatched or unbalanced brackets -> Output: False.

Time Complexity:
- O(n): Traverse the string once.

Space Complexity:
- O(n): Space for the stack (in the worst case).
"""

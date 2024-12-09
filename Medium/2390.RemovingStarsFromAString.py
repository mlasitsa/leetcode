class Solution:
    def removeStars(self, s: str) -> str:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a string `s`, remove the characters that are "erased" by asterisks (`*`).
        - Each `*` removes the character immediately before it. The string is guaranteed to contain only valid operations.

        Clarifications/Constraints:
        - The `*` always has a preceding character to erase.
        - The input string can contain any combination of lowercase letters and `*`.
        - The result should be returned as a single string.

        Examples:
        Input: "leet**cod*e" -> Output: "lecoe"
        Input: "erase*****" -> Output: ""

        Potential clarifying questions for an interview:
        1. Can the input string start with a `*`? (No, as per constraints.)
        2. What should be returned if the entire string is erased? (Return an empty string.)
        3. Should the solution handle very large strings? (Yes, use an efficient approach.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a stack to manage the operations:
        #   * Append characters to the stack as they appear.
        #   * Pop the stack when encountering a `*`.
        # - The stack will contain the resulting characters after processing the input.

        """
        P - Plan
        1. Initialize an empty stack to store characters.
        2. Traverse each character in the string:
           - If the character is a letter, append it to the stack.
           - If the character is `*`:
             * Check if the stack is non-empty and pop the last character.
             * If the stack is empty, continue without performing any operation.
        3. After traversal, join the stack into a string and return it.
        """

        stack = []  # Stack to store the resulting characters

        # I - Implement
        for ch in s:
            # Handle the `*` case
            if ch == "*":
                if stack:  # Pop the last character if the stack is not empty
                    stack.pop()
            else:
                # Append regular characters to the stack
                stack.append(ch)

        # Join the stack into a string and return
        return "".join(stack)

# Example Usage
sol = Solution()

"""
E - Evaluate
Test the solution with examples:
1. Input: "leet**cod*e" -> Output: "lecoe"
2. Input: "erase*****" -> Output: ""
3. Input: "abc*de*" -> Output: "ad"

Edge Cases:
1. All characters erased -> Output: ""
2. String with no stars -> Output: Original string
3. String with consecutive stars -> Ensure all appropriate characters are erased.

Time Complexity:
- O(n): Each character is processed once.

Space Complexity:
- O(n): Stack space for storing characters.
"""

res = sol.removeStars("leet**cod*e")

if res == 'lecoe':
    print("Good Job")
else:
    print("Try Again...")

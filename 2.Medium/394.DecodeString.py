class Solution:
    def decodeString(self, s: str) -> str:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a string `s` representing an encoded format (e.g., `3[a]2[bc]`), decode it and return the expanded string.
        - The encoded format is `k[encoded_string]`, where `k` is a positive integer representing the number of times
          the `encoded_string` is repeated.
        - Nested encodings are possible (e.g., `2[3[a]b]`).

        Clarifications/Constraints:
        - Input string is guaranteed to be well-formed.
        - Input only contains digits, letters, and square brackets.
        - Digits represent integers >= 1.

        Examples:
        Input: "3[a]2[bc]" -> Output: "aaabcbc"
        Input: "3[a2[c]]" -> Output: "accaccacc"
        Input: "2[abc]3[cd]ef" -> Output: "abcabccdcdcdef"

        Potential clarifying questions for an interview:
        1. Can the input string contain spaces or invalid characters? (No, assume valid input.)
        2. How large can the input string be? (Assume reasonable size for simulation.)
        3. Should the function handle edge cases like empty strings? (Yes, return an empty string if input is empty.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use stacks to handle nested encodings:
        #   * `num_stack` to store the repeat counts (`k` values).
        #   * `str_stack` to store partially decoded strings when encountering nested encodings.
        # - Traverse the string and build the result iteratively.

        """
        P - Plan
        1. Initialize two stacks: `num_stack` for repeat counts and `str_stack` for substrings.
        2. Initialize `current_str` and `current_num` to track the current substring and number being built.
        3. Traverse the string:
           - If the character is a digit, build the `current_num`.
           - If the character is '[', push `current_num` and `current_str` to their stacks, then reset them.
           - If the character is ']', pop from the stacks, repeat the `current_str` by the popped number,
             and append it to the popped string.
           - Otherwise, append the character to `current_str`.
        4. Return the final `current_str` after traversal.
        """

        # Initialize stacks and variables
        num_stack = []      # Stack to store numbers (k)
        str_stack = []      # Stack to store substrings
        current_str = ""    # Current substring being built
        current_num = 0     # Current number being built

        # I - Implement
        for char in s:
            if char.isdigit():
                # Build the number, since it can be more than one digit (e.g., 12[a])
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current number and string to their respective stacks
                num_stack.append(current_num)
                str_stack.append(current_str)
                # Reset current_str and current_num for the next encoded part
                current_str = ""
                current_num = 0
            elif char == ']':
                # Pop the number and the string from stacks
                repeat_num = num_stack.pop()
                last_str = str_stack.pop()
                # Repeat the current string and append it to the last string
                current_str = last_str + current_str * repeat_num
            else:
                # Build the current string
                current_str += char

        return current_str

# Example Usage
sol = Solution()

"""
E - Evaluate
Test the solution with examples:
1. Input: "3[a]2[bc]" -> Output: "aaabcbc"
2. Input: "3[a2[c]]" -> Output: "accaccacc"
3. Input: "2[abc]3[cd]ef" -> Output: "abcabccdcdcdef"

Edge Cases:
1. Empty string -> Output: ""
2. Single character string -> Output: Character itself
3. No nested encodings -> Output: Concatenated result

Time Complexity:
- O(n): Each character is processed once.

Space Complexity:
- O(n): Additional space for stacks in the worst case (nested encodings).
"""

res = sol.decodeString("3[a]2[bc]")

if res == 'aaabcbc':
    print('Good Job')
else:
    print('Try again')
    print('Your result is', res)

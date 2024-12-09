class Solution:
    def reverseWords(self, s: str) -> str:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a string `s`, reverse the order of words.
        - Words are separated by one or more spaces.
        - Leading and trailing spaces should be removed, and only a single space should separate words in the result.

        Clarifications/Constraints:
        - Input string may contain multiple spaces between words.
        - Words consist of English letters and punctuation.
        - The result should not have leading/trailing spaces.

        Examples:
        Input: "the sky is blue" -> Output: "blue is sky the"
        Input: "  hello world  " -> Output: "world hello"
        Input: "a good   example" -> Output: "example good a"

        Potential clarifying questions for an interview:
        1. Can the input string contain special characters? (Yes, treat them as part of words.)
        2. How do we handle multiple spaces? (Collapse them into a single space in the output.)
        3. Can the input string be empty? (Return an empty string.)
        4. Should the input be modified in place? (No, return a new string.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Two-pointer traversal from the end of the string to collect words.
        # - Use a stack to reverse the word while parsing it.
        # - Use an additional list to construct the result.

        """
        P - Plan
        1. Start a pointer (`right`) at the end of the string.
        2. Use a stack to collect characters of each word.
        3. Skip trailing and in-between spaces.
        4. Collect characters of the current word into the stack.
        5. Append the reversed word from the stack to the result list.
        6. Add a space after each word (except the last one).
        7. Join the words in the result list to form the final reversed string.
        """

        # Initialize pointers and structures
        right = len(s) - 1
        stack = []  # To reverse individual words
        answer = []  # To store the result

        # I - Implement
        while right >= 0:
            # Skip spaces
            while right >= 0 and s[right] == " ":
                right -= 1
            
            # If we are out of bounds, break
            if right < 0:
                break
            
            # Collect characters of the current word
            while right >= 0 and s[right] != " ":
                stack.append(s[right])
                right -= 1
            
            # Append the collected word in the correct order
            while stack:
                answer.append(stack.pop())
            
            # Skip spaces to check if there are more words
            while right >= 0 and s[right] == " ":
                right -= 1
            
            # Add a space if there are more words to process
            if right >= 0:
                answer.append(" ")

        # Return the final result as a string
        return "".join(answer)

# Example Usage
sol = Solution()

"""
E - Evaluate
Test the solution with examples:
1. Input: "the sky is blue" -> Output: "blue is sky the"
2. Input: "  hello world  " -> Output: "world hello"
3. Input: "a good   example" -> Output: "example good a"

Edge Cases:
1. Empty string -> Output: ""
2. String with only spaces -> Output: ""
3. Single word -> Output: Word itself

Time Complexity:
- O(n): Single traversal of the string.

Space Complexity:
- O(n): Stack and result list require additional space proportional to the input size.
"""

res = sol.reverseWords("the sky is blue")

if res == "blue is sky the":
    print("Good Job!")
else:
    print("Try Again...")

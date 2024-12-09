class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        U - Understand the Problem
        Problem Statement:
        - Given two strings `word1` and `word2`, merge them alternately. Characters should be taken one by one
          from each string until one string runs out of characters. Append the remaining characters from the
          longer string at the end.

        Clarifications/Constraints:
        - The length of `word1` and `word2` can be different.
        - If one string is shorter, append the rest of the longer string.
        - Inputs are guaranteed to be valid strings consisting of lowercase English letters.

        Examples:
        Input: word1 = "abc", word2 = "pqr" -> Output: "apbqcr"
        Input: word1 = "ab", word2 = "pqrs" -> Output: "apbqrs"
        Input: word1 = "abcd", word2 = "pq" -> Output: "apbqcd"

        Potential clarifying questions for an interview:
        1. Can the input strings be empty? (Assume yes, handle appropriately.)
        2. Are there any restrictions on the input string characters? (Assume only lowercase English letters.)
        3. What should be the output format? (A single string.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - This is a simple merging problem with sequential access to characters.
        # - It can be solved using two pointers to alternate between characters of `word1` and `word2`.

        """
        P - Plan
        1. Initialize an empty list `merged` to store the characters alternately.
        2. Use two pointers (`one` and `two`) to traverse `word1` and `word2`, respectively.
        3. Iterate until both pointers reach the end of their respective strings:
           - Append the current character from `word1` if `one` is within bounds.
           - Append the current character from `word2` if `two` is within bounds.
           - Increment the corresponding pointer after appending.
        4. At the end of the loop, convert the `merged` list to a string and return it.
        """

        # Initialize the merged list and pointers
        merged = []  # To store the merged characters
        char1 = list(word1)  # Convert word1 into a list of characters
        char2 = list(word2)  # Convert word2 into a list of characters
        one = 0  # Pointer for word1
        two = 0  # Pointer for word2

        # I - Implement
        while (one < len(char1) or two < len(char2)):
            # Append character from word1 if within bounds
            if one < len(char1):
                merged.append(char1[one])
                one += 1
            # Append character from word2 if within bounds
            if two < len(char2):
                merged.append(char2[two])
                two += 1

        # Join the merged characters into a single string
        return ''.join(merged)

# Example Usage
sol = Solution()

"""
E - Evaluate
Test the solution with examples:
1. Input: word1 = "abc", word2 = "pqr" -> Output: "apbqcr"
2. Input: word1 = "ab", word2 = "pqrs" -> Output: "apbqrs"
3. Input: word1 = "abcd", word2 = "pq" -> Output: "apbqcd"

Edge Cases:
1. word1 = "", word2 = "xyz" -> Output: "xyz"
2. word1 = "abc", word2 = "" -> Output: "abc"
3. word1 = "", word2 = "" -> Output: ""
"""

res = sol.mergeAlternately("abc", "pqr")

if res == "apbqcr":
    print("Success")
else:
    print("Failed")

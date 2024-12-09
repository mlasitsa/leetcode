class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a string `s`, reverse only the vowels (a, e, i, o, u) in the string.
        - Both uppercase and lowercase vowels are considered valid vowels.
        - Other characters in the string remain in their original positions.

        Clarifications/Constraints:
        - The input can contain letters, numbers, and special characters.
        - The function should preserve the case and position of non-vowel characters.
        - An empty string or a single-character string should return as is.

        Examples:
        Input: "hello" -> Output: "holle"
        Input: "IceCreAm" -> Output: "AceCreIm"
        Input: "b" -> Output: "b"

        Potential clarifying questions for an interview:
        1. Should uppercase and lowercase vowels both be considered? (Yes.)
        2. How do we handle strings with no vowels? (Return the original string.)
        3. What is the expected time complexity? (Aim for O(n).)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Two-pointer approach:
        #   * Use a left pointer starting from the beginning and a right pointer starting from the end.
        #   * Swap the vowels at the left and right pointers and move them inward.
        #   * Skip non-vowel characters using conditional checks.

        """
        P - Plan
        1. Initialize a hash map or set to store the vowels for quick lookup.
        2. Convert the string `s` into a list (`word`) for easier swapping.
        3. Use two pointers (`left` and `right`) to traverse the string from both ends.
        4. While `left` is less than `right`:
           - If both `word[left]` and `word[right]` are vowels:
             * Swap them and move both pointers inward.
           - If `word[left]` is not a vowel, increment `left`.
           - If `word[right]` is not a vowel, decrement `right`.
        5. Return the modified list as a string.
        """

        # Handle edge cases
        if len(s) == 0:  # Empty string
            return "None"
        if len(s) == 1:  # Single character
            return s[0]

        # Initialize the set of vowels for quick lookup
        hmap = {'a', 'e', 'i', 'o', 'u'}

        # Convert the string to a list for easier manipulation
        word = list(s)

        # Initialize two pointers
        left = 0
        right = len(s) - 1

        # I - Implement
        # Traverse and reverse vowels using the two-pointer technique
        while left < right:
            # Check if both characters are vowels
            if word[left].lower() in hmap and word[right].lower() in hmap:
                # Swap vowels
                word[left], word[right] = word[right], word[left]
                # Move both pointers inward
                left += 1
                right -= 1
            # Move the right pointer if the character is not a vowel
            elif word[right].lower() not in hmap:
                right -= 1
            # Move the left pointer if the character is not a vowel
            elif word[left].lower() not in hmap:
                left += 1

        # Join the list back into a string and return it
        return "".join(word)

# Example Usage
sol = Solution()

"""
E - Evaluate
Test the solution with examples:
1. Input: "IceCreAm" -> Output: "AceCreIm"
2. Input: "hello" -> Output: "holle"
3. Input: "b" -> Output: "b"

Edge Cases:
1. Empty string -> Output: "None"
2. Single character (vowel) -> Output: Character itself
3. Single character (non-vowel) -> Output: Character itself
4. String with no vowels -> Output: Original string

Time Complexity:
- O(n): Single traversal of the string using two pointers.

Space Complexity:
- O(n): Temporary list representation of the string.
"""

res = sol.reverseVowels("IceCreAm")

if res == "AceCreIm":
    print("Good Job")
else:
    print("Try again")

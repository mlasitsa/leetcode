from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given an array of characters, compress it in-place such that consecutive duplicate characters
          are replaced by the character followed by the count of duplicates (e.g., "aa" becomes "a2").
        - If a character appears only once, it remains as is.
        - The function should return the new length of the array after compression.

        Clarifications/Constraints:
        - The input array must be modified in-place with O(1) additional space.
        - The count should be appended as individual digits (e.g., "a12" becomes ['a', '1', '2']).
        - Characters are lowercase English letters.

        Examples:
        Input: ["a", "a", "b", "b", "c", "c", "c"] -> Output: ["a", "2", "b", "2", "c", "3"]
        Input: ["a"] -> Output: ["a"]
        Input: ["a", "b", "c"] -> Output: ["a", "b", "c"]

        Potential clarifying questions for an interview:
        1. What is the expected behavior for empty input arrays? (Return length 0.)
        2. Are all characters guaranteed to be lowercase letters? (Assume yes.)
        3. Should the result array always be smaller than or equal to the input? (Yes, due to compression.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a two-pointer approach to modify the array in-place:
        #   * One pointer to traverse the input array.
        #   * Another pointer to write the compressed characters.

        """
        P - Plan
        1. Initialize a pointer (`write`) to track the position in the array where compressed data is written.
        2. Use another pointer (`read`) to traverse the array.
        3. For each character:
           - Count consecutive duplicates using a loop.
           - Write the character to the `write` pointer.
           - If the count > 1, write the count as individual digits.
        4. Return the value of `write` as the new length of the array.
        """

        # I - Implement
        write = 0  # Pointer for writing compressed data
        read = 0  # Pointer for reading input

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count consecutive duplicates
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

# Example Usage
sol = Solution()

"""
E - Evaluate
Test the solution with examples:
1. Input: ["a", "a", "b", "b", "c", "c", "c"] -> Output: ["a", "2", "b", "2", "c", "3"]
2. Input: ["a"] -> Output: ["a"]
3. Input: ["a", "b", "c"] -> Output: ["a", "b", "c"]

Edge Cases:
1. Empty input array -> Output: 0
2. Single character array -> Output: ["a"]
3. All characters are the same -> Input: ["a", "a", "a", "a"] -> Output: ["a", "4"]

Time Complexity:
- O(n): Each character is processed once.

Space Complexity:
- O(1): Compression is done in-place without additional space.
"""

res = sol.compress(["a", "a", "b", "b", "c", "c", "c"])

if res == 6:  # Length of the compressed array
    print("Good Job")
else:
    print("Try Again...")

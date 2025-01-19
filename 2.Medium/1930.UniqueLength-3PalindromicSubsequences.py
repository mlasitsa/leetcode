class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a string `s`, return the number of unique palindromic subsequences of length 3.
        - A palindromic subsequence of length 3 is defined as:
          * The first and third characters are the same.
          * The second character can be any character between the first and third.

        Examples:
        Input: s = "aabca"
        Output: 3
        Explanation:
        - Unique palindromic subsequences are: "aba", "aaa", "aca".

        Input: s = "abc"
        Output: 0
        Explanation:
        - No palindromic subsequences of length 3 exist.

        Clarifications/Constraints:
        1. The string length is between 3 and 100,000.
        2. Characters are lowercase English letters.
        3. We only care about **unique** palindromic subsequences of length 3.
        4. Subsequence: Non-contiguous, but order-preserving selection of characters.

        Potential clarifying questions:
        1. Are all inputs valid? (Yes, string length and character constraints are guaranteed.)
        2. What happens if no valid subsequences exist? (Return 0.)
        """

        """
        M - Match with Patterns
        Pattern Identified:
        - Use a **set** to ensure uniqueness.
        - Iterate through all unique characters (`letters`) in `s`.
        - Find the first and last occurrence of each character.
        - Count unique characters in between these positions.
        """

        """
        P - Plan
        1. Identify all unique characters in `s`.
        2. For each character:
           - Find its first (`i`) and last (`j`) occurrence in `s`.
           - Count the unique characters between these positions using a `set`.
        3. Sum up the size of the sets for all characters.
        4. Return the total count.
        """

        letters = set(s)  # Step 1: Extract unique characters from `s`
        ans = 0  # Initialize the result

        for letter in letters:
            # Step 2: Find first and last occurrence of `letter`
            i, j = s.index(letter), s.rindex(letter)
            between = set()  # Step 3: Store unique characters between `i` and `j`
            
            # Step 4: Iterate between the first and last occurrence
            for k in range(i + 1, j):
                between.add(s[k])
            
            # Step 5: Add the count of unique characters to the result
            ans += len(between)

        return ans  # Step 6: Return the total count

# Example Usage:
"""
E - Evaluate
Test the solution with examples:
1. Input: s = "aabca"
   Output: 3
   Explanation:
   - Unique palindromic subsequences:
     * "aba" (a's at index 0 and 4, b in between),
     * "aaa" (a's at index 0 and 4, a in between),
     * "aca" (a's at index 0 and 4, c in between).

2. Input: s = "abc"
   Output: 0
   Explanation:
   - No characters repeat, so no palindromic subsequences exist.

3. Edge Case: s = "aaa"
   Output: 1
   Explanation:
   - Unique palindromic subsequence is "aaa".

Time Complexity:
- Extracting unique characters: O(n) (depends on the number of unique letters).
- Finding `index` and `rindex` for each character: O(n) per unique letter.
- Iterating between `i` and `j` for each unique letter: O(n) in total.
- Overall: O(n * u), where `u` is the number of unique characters (bounded by 26).

Space Complexity:
- `letters`: O(26) (unique letters).
- `between`: O(n) in the worst case (size of `s`).
"""

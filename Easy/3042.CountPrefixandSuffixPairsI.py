class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        U - Understand:
        - Problem: Given a list of words, count the number of pairs `(i, j)` such that:
          1. `words[i]` is a prefix of `words[j]`, and
          2. `words[i]` is also a suffix of `words[j]`.
        - Clarifications/Constraints:
          1. `words` contains at least one word.
          2. `i` and `j` are distinct indices in the list.
          3. Strings are case-sensitive.

        Examples:
        Input: words = ["a", "abc", "ca", "abca"]
        Output: 2
        Explanation:
        - Pairs:
          1. ("a", "abc"): "a" is both prefix and suffix of "abc".
          2. ("a", "abca"): "a" is both prefix and suffix of "abca".

        M - Match:
        - Use a brute-force approach to iterate through all pairs of words.
        - Check if one word is both the prefix and suffix of the other.

        P - Plan:
        1. Iterate through all pairs of words (nested loops).
        2. For each pair `(i, j)`, check if:
           - `words[i]` is a prefix of `words[j]` using `startswith`.
           - `words[i]` is a suffix of `words[j]` using `endswith`.
        3. Count pairs satisfying both conditions.
        4. Return the count.

        I - Implement:
        """
        n = len(words)
        count = 0

        # Step 1: Iterate through each pair of words
        for i in range(n):
            for j in range(i + 1, n):
                str1 = words[i]
                str2 = words[j]

                # Step 2: Skip if the first string is larger than the second
                if len(str1) > len(str2):
                    continue

                # Step 3: Check if str1 is both the prefix and suffix of str2
                if str2.startswith(str1) and str2.endswith(str1):
                    count += 1

        # Step 4: Return the total count of prefix-suffix pairs
        return count

# Example Usage:
"""
E - Evaluate:
1. Input: words = ["a", "abc", "ca", "abca"]
   Output: 2
   Explanation:
   - Pairs:
     1. ("a", "abc"): "a" is both prefix and suffix of "abc".
     2. ("a", "abca"): "a" is both prefix and suffix of "abca".

2. Input: words = ["x", "y", "xy", "yx"]
   Output: 0
   Explanation:
   - No pairs where one word is both prefix and suffix of another.

Time Complexity:
- O(n^2) for iterating through all pairs of words.

Space Complexity:
- O(1) extra space.
"""

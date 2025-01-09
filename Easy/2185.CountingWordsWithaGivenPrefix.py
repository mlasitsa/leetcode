class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        """
        U - Understand:
        - Problem: Given a list of `words` and a string `pref`, count the number of words in `words` that start with `pref`.
        - Clarifications/Constraints:
          1. All words and `pref` consist of lowercase English letters.
          2. 1 <= len(words) <= 10^5, 1 <= len(pref) <= 100.
          3. The prefix must match the first characters of the word.
        - Examples:
          Input: words = ["pay", "attention", "practice", "attend"], pref = "at"
          Output: 2
          Explanation:
          - Words starting with "at": ["attention", "attend"].

        M - Match:
        - Use a loop to iterate through all words and check if each word starts with `pref` using the `startswith` method.

        P - Plan:
        1. Initialize a variable `count` to 0.
        2. Loop through each word in `words`.
        3. If the word starts with `pref`, increment `count`.
        4. Return `count` as the result.

        I - Implement:
        """
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count

# Example Usage:
"""
E - Evaluate:
1. Input: words = ["pay", "attention", "practice", "attend"], pref = "at"
   Output: 2
   Explanation:
   - Words starting with "at": ["attention", "attend"].

2. Input: words = ["dog", "deer", "deal"], pref = "de"
   Output: 2
   Explanation:
   - Words starting with "de": ["deer", "deal"].

3. Edge Case: words = ["apple", "banana", "cherry"], pref = "z"
   Output: 0
   Explanation:
   - No words start with "z".

Time Complexity:
- O(n * p), where `n` is the number of words and `p` is the length of the prefix (for the `startswith` check).

Space Complexity:
- O(1) extra space.
"""

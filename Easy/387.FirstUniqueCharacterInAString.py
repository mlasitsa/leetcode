class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a string `s`, find the first non-repeating character and return its index.
        - If no such character exists, return -1.

        Clarifications/Constraints:
        - The input string contains only lowercase English letters.
        - The function should return the 0-based index of the first unique character.

        Examples:
        Input: s = "leetcode"
        Output: 0

        Input: s = "loveleetcode"
        Output: 2

        Input: s = "aabb"
        Output: -1

        Potential clarifying questions for an interview:
        1. What should be returned if the string is empty? (-1.)
        2. Can the input contain uppercase or special characters? (No, assume lowercase English letters only.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a hashmap to count the occurrences of each character.
        # - Traverse the string again to find the first character with a count of 1.

        """
        P - Plan
        1. Handle the edge case where the string is empty (return -1).
        2. Use a hashmap to count the frequency of each character in the string.
        3. Traverse the string and check the frequency of each character:
           - If a character has a frequency of 1, return its index.
        4. If no unique character is found, return -1.
        """

        # Step 1: Handle the edge case
        if not s:
            return -1

        # Step 2: Count the frequency of each character
        hmap = {}
        for ch in s:
            if ch in hmap:
                hmap[ch] += 1
            else:
                hmap[ch] = 1

        # Step 3: Find the first unique character
        for i, ch in enumerate(s):
            if hmap[ch] == 1:
                return i

        # Step 4: If no unique character is found, return -1
        return -1

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: s = "leetcode" -> Output: 0
2. Input: s = "loveleetcode" -> Output: 2
3. Input: s = "aabb" -> Output: -1

Edge Cases:
1. Empty string -> Output: -1.
2. String with all repeating characters -> Output: -1.
3. String with one unique character -> Return its index.

Time Complexity:
- O(n): Traverse the string twice (once to count frequencies, once to find the unique character).

Space Complexity:
- O(1): Since the input is limited to lowercase English letters, the hashmap size is bounded by 26.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a string `s`, return the length of the **longest palindrome** that can be built.
        - A palindrome is a string that reads the same forward and backward.
        - We can rearrange characters to form a palindrome.

        Clarifications:
        - Characters with even counts can **always** be used in full.
        - Characters with odd counts contribute `(count - 1)`, except for **one odd character**, which can go in the middle.
        - The result must be an **integer** (not the actual palindrome).

        Example Walkthrough:
        Example 1:
        Input: "abccccdd"
        Output: 7
        Explanation: The longest palindrome is "dccaccd".

        Example 2:
        Input: "a"
        Output: 1
        Explanation: Only one character → itself is a palindrome.

        Example 3:
        Input: "ccc"
        Output: 3
        Explanation: Since all are the same, "ccc" is already a palindrome.
        """

        # M - Match with Patterns
        """
        - This problem deals with **frequency counting** (best solved with a HashMap).
        - If we count each character:
          - Even occurrences contribute fully to the palindrome.
          - Odd occurrences contribute `count - 1` to ensure symmetry.
          - **At most one odd-count character can be placed in the center**.
        """

        # P - Plan
        """
        1. Create a frequency dictionary (`hmap`) to count occurrences of each character.
        2. Initialize `length = 0` and a flag (`useOdd = 1`) to allow one odd character.
        3. Iterate over character counts:
           - If even, add the entire count to `length`.
           - If odd:
             - If `useOdd > 0`, add the full count (since one odd can be in the center).
             - Otherwise, add `count - 1` to maintain symmetry.
        4. Return `length`.
        """

        hmap = {}

        for ch in s:  # Step 1: Count occurrences
            if ch in hmap:
                hmap[ch] += 1
            else:
                hmap[ch] = 1

        length = 0
        useOdd = 1

        for value in hmap.values():  # Step 3: Calculate palindrome length
            if value % 2 == 0:
                length += value
            else:
                if useOdd > 0:  
                    length += value  # Use one odd count fully (place in center)
                    useOdd -= 1
                else:
                    length += value - 1  # Only take even part of odd counts

        return length

        """
        I - Implement
        - The solution correctly counts frequencies and uses the strategy of taking even counts + one odd count.

        R - Review
        - Time Complexity: O(N) (we iterate over `s` once and over `hmap` once).
        - Space Complexity: O(1) (since we store at most 26 lowercase letters).

        E - Evaluate
        Edge Cases:
        ✅ Single character → "a" → Output: 1 (itself is a palindrome).
        ✅ All unique characters → "abc" → Output: 1 (can only pick one for the middle).
        ✅ All identical characters → "cccc" → Output: 4 (already a palindrome).
        ✅ Mix of even and odd → "abccccdd" → Output: 7 (one odd placed in center).
        """

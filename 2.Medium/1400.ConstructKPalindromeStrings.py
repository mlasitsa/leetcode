class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        '''
        U - Understand:
        - I need to determine if it's possible to construct exactly `k` palindromes using all characters in `s`.
        - A palindrome can have at most one character with an odd frequency in its center.
        - Key observations:
            - If the number of odd frequencies is greater than `k`, return False.
            - If `k` is greater than the length of the string, it's impossible to construct `k` palindromes.
        - Edge cases:
            - `k > len(s)`: Impossible, return False.
            - `k == len(s)`: Always True because each character can form its own palindrome.

        M - Match:
        - This problem fits frequency counting:
            - Count the frequency of each character in the string.
            - Identify how many characters have odd frequencies.
            - Compare the count of odd frequencies with `k`.

        P - Plan:
        1. Handle edge cases:
            - If `len(s) < k`, return False.
            - If `len(s) == k`, return True.
        2. Count character frequencies using a dictionary.
        3. Count how many characters have odd frequencies (`oddCount`).
        4. If `oddCount > k`, return False.
        5. Otherwise, return True.

        I - Implement:
        '''
        if len(s) < k:
            return False
        if len(s) == k:
            return True

        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        oddCount = 0

        for value in freq.values():
            if value % 2 != 0:
                oddCount += 1

        if oddCount > k:
            return False
        else:
            return True

# Example Usage:
'''
E - Evaluate:
Input: s = "annabelle", k = 2
Output: True
Explanation:
- Character frequencies: {'a': 2, 'n': 2, 'b': 1, 'e': 2, 'l': 2}
- OddCount = 1 ('b').
- We can form two palindromes: "anna" and "belle".

Input: s = "leetcode", k = 3
Output: False
Explanation:
- Character frequencies: {'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1}
- OddCount = 5.
- OddCount > k, so it's not possible to form 3 palindromes.

Time Complexity:
- Counting character frequencies: O(n).
- Calculating `oddCount`: O(26) = O(1) (constant for lowercase letters).
- Total: O(n).

Space Complexity:
- Dictionary to store frequencies: O(26) = O(1).
'''

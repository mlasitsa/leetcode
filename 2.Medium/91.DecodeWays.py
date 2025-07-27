class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        U - Understand:
        - Problem: Given a string `s` representing a message encoded with numbers (1 to 26 mapped to 'A' to 'Z'), find the total number of ways to decode it.
        - Key Points:
          1. Each character in `s` can be decoded if it corresponds to a valid single-digit (1-9).
          2. Pairs of consecutive characters can be decoded if they form a valid two-digit number (10-26).
          3. Strings starting with '0' or containing invalid pairs (e.g., "30") cannot be decoded.
        - Examples:
          - Input: "226"
            Output: 3
            Explanation: Possible decodings are "BZ", "VF", "BBF".
          - Input: "0"
            Output: 0
            Explanation: No valid decoding.

        M - Match:
        - Use **Dynamic Programming**:
          1. Use a DP array where `dp[i]` represents the number of ways to decode the substring `s[:i+1]`.
          2. Base cases:
             - `dp[0] = 1` if the first character is valid (not '0').
          3. Transition:
             - Single-character decoding: If `s[i]` is valid (1-9), then `dp[i] += dp[i-1]`.
             - Two-character decoding: If `s[i-1:i+1]` is valid (10-26), then `dp[i] += dp[i-2]`.

        P - Plan:
        1. Handle edge case: If `s` starts with '0', return 0.
        2. Initialize a DP array with size `len(s)` and set `dp[0] = 1`.
        3. Iterate through the string starting from index 1:
           - Check if `s[i]` can be decoded as a single digit.
           - Check if `s[i-1:i+1]` can be decoded as a two-digit number.
           - Update `dp[i]` accordingly.
        4. Return `dp[-1]` as the total number of ways to decode `s`.

        I - Implement:
        '''
        if s[0] == '0':
            return 0  # No valid decoding for strings starting with '0'

        dp = [0] * len(s)
        dp[0] = 1  # One way to decode the first character if valid

        for i in range(1, len(s)):
            cur = s[i]
            prev = s[i - 1]

            # Single-digit decoding
            if '1' <= cur <= '9':
                dp[i] = dp[i - 1]

            # Two-digit decoding
            if prev == '1' or (prev == '2' and '0' <= cur <= '6'):
                dp[i] += dp[i - 2] if i - 2 >= 0 else 1

        return dp[-1]

# Example Usage:
'''
E - Evaluate:
1. Input: "226"
   Output: 3
   Explanation:
   - Decodings: "BZ", "VF", "BBF".

2. Input: "0"
   Output: 0
   Explanation:
   - Strings starting with '0' cannot be decoded.

3. Input: "1212"
   Output: 5
   Explanation:
   - Decodings: "ABAB", "AUBL", "LUB", "LAB", "AVAB".

Time Complexity:
- O(n): Iterate through the string once.

Space Complexity:
- O(n): DP array of size `len(s)`.

Alternative:
- Space Optimization: Use two variables to store `dp[i-1]` and `dp[i-2]` to reduce space complexity to O(1).
'''

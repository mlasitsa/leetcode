class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        U - Understand:
        - Problem: Given a string `s`, find the length of the **longest substring** without repeating characters.
        - Key Observations:
          1. A substring is a **contiguous** sequence of characters.
          2. We need to find the longest substring with all unique characters.
          3. Using a **sliding window** technique with a **set** can help track seen characters efficiently.

        Examples:
        - Input: "abcabcbb"
          Output: 3
          Explanation: "abc" is the longest substring with unique characters.
        - Input: "bbbbb"
          Output: 1
          Explanation: The longest substring is "b".
        - Input: "pwwkew"
          Output: 3
          Explanation: The longest substring is "wke".

        M - Match:
        - **Sliding Window (Two Pointers Approach)**:
          1. Expand the `right` pointer until a duplicate is found.
          2. Once a duplicate appears, move the `left` pointer to shrink the window.
          3. Use a **set** to keep track of unique characters efficiently.
        - **Alternative Approaches**:
          - Brute Force: Try all substrings (**O(n²)**, inefficient).
          - HashMap + Sliding Window: Optimize by tracking indices (**O(n)**).

        P - Plan:
        1. Initialize:
           - `maxLen` to track the longest substring length.
           - `storeCharacters` (set) to track unique characters.
           - `left` pointer to mark the start of the window.
        2. Iterate with the `right` pointer over `s`:
           - If `s[right]` is already in the set:
             - Remove `s[left]` from the set.
             - Move `left` pointer forward to maintain uniqueness.
           - Add `s[right]` to the set.
           - Update `maxLen` with the current window size.
        3. Return `maxLen`.

        I - Implement:
        '''
        if not s:
            return 0

        maxLen = 0
        storeCharacters = set()
        left = 0

        for right in range(len(s)):
            while s[right] in storeCharacters:
                storeCharacters.remove(s[left])
                left += 1  # Shrink the window

            storeCharacters.add(s[right])
            maxLen = max(maxLen, right - left + 1)  # Update max length in each iteration

        return maxLen


    '''
    Alternative Solution: HashMap + Sliding Window
    - Instead of a set, use a **dictionary** to store character indices.
    - When a duplicate is found, move `left` pointer to **max of current left and last index + 1**.

    P - Plan:
    1. Use a dictionary to track the last index of each character.
    2. Iterate with `right` pointer:
       - If `s[right]` is in the dictionary:
         - Move `left` pointer to `max(left, dict[s[right]] + 1)`.
       - Update the character index in the dictionary.
       - Update `maxLen`.

    I - Implement:
    '''
    def lengthOfLongestSubstringAlt(self, s: str) -> int:
        if not s:
            return 0

        maxLen = 0
        charIndexMap = {}
        left = 0

        for right in range(len(s)):
            if s[right] in charIndexMap:
                left = max(left, charIndexMap[s[right]] + 1)  # Ensure left pointer doesn't move backward

            charIndexMap[s[right]] = right  # Store/update last index of character
            maxLen = max(maxLen, right - left + 1)

        return maxLen

# Example Usage:
'''
E - Evaluate:
1. Input: "abcabcbb"
   Output: 3
   Explanation:
   - Substring: "abc" is the longest unique substring.

2. Input: "bbbbbb"
   Output: 1
   Explanation:
   - Only "b" is unique.

3. Input: "pwwkew"
   Output: 3
   Explanation:
   - "wke" is the longest unique substring.

Time Complexity:
- **O(n)**: Each character is processed at most twice (once for adding, once for removing).
- **O(n²)** for brute force.

Space Complexity:
- **O(n)**: Set or dictionary stores unique characters.
'''

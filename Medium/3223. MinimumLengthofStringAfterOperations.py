class Solution:
    def minimumLength(self, s: str) -> int:
        '''
        U - Understand:
        - Problem: Perform a series of operations on string `s` to remove characters. The process is:
          1. Select a character `s[i]`.
          2. Remove the closest equal characters to the left and right of `s[i]`.
          3. Repeat until no more valid operations can be performed.
        - Return the minimum length of the resulting string.
        - Constraints:
          1. The string contains only lowercase letters.
          2. `s` is non-empty.

        Examples:
        - Input: s = "ca"
          Output: 2
          Explanation: No operations can be performed; return the length of `s`.

        - Input: s = "cabaabac"
          Output: 0
          Explanation: Remove characters symmetrically until no characters remain.

        M - Match:
        - Two solutions can be considered:
          1. **Frequency Hashmap (Your solution)**:
             - Use a hashmap to store the indices of each character.
             - Iterate over the characters and simulate removing pairs.
          2. **Two-pointer approach (Alternative)**:
             - Use two pointers starting at the ends of the string.
             - Remove characters symmetrically if the leftmost and rightmost characters match.

        P - Plan:
        - Your solution:
          1. Build a frequency hashmap with character indices.
          2. Iterate over each character and simulate removing pairs symmetrically.
          3. Keep track of the remaining string length.
        - Alternative solution:
          1. Use two pointers (`left` and `right`) starting at the ends of the string.
          2. Remove matching characters from both ends until no valid operations can be performed.
          3. Return the remaining string length.

        I - Implement:
        '''

        # Frequency Hashmap Solution
        def using_hashmap(s: str) -> int:
            hmap = {}
            for i in range(len(s)):
                if s[i] in hmap:
                    hmap[s[i]].append(i)
                else:
                    hmap[s[i]] = [i]

            remaining_length = 0
            for char, indices in hmap.items():
                n = len(indices)
                while n > 2:
                    n -= 2  # Remove pairs symmetrically
                remaining_length += n  # Add leftover characters
            
            return remaining_length

        # Two-pointer Approach
        def using_two_pointers(s: str) -> int:
            left, right = 0, len(s) - 1

            while left < right and s[left] == s[right]:
                char = s[left]
                while left <= right and s[left] == char:
                    left += 1
                while left <= right and s[right] == char:
                    right -= 1

            return right - left + 1

# Example Usage:
'''
E - Evaluate:
1. Input: s = "ca"
   Output: 2
   Explanation:
   - No valid operations can be performed. Minimum length is 2.

2. Input: s = "cabaabac"
   Output: 0
   Explanation:
   - Remove characters symmetrically until no characters remain.

3. Input: s = "aabccabba"
   Output: 3
   Explanation:
   - Remove "a...a" symmetrically, resulting in "bccab".
   - Remove "b...b", resulting in "cca".
   - Remove "c...c", resulting in an empty string.

Time Complexity:
- Hashmap solution: O(n).
- Two-pointer solution: O(n).

Space Complexity:
- Hashmap solution: O(n) for storing indices.
- Two-pointer solution: O(1) (no additional data structures used).
'''

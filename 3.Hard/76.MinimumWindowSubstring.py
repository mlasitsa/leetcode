class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        U - Understand the Problem
        Problem Statement:
        - Given two strings `s` and `t`, find the **minimum substring** in `s` that contains all characters of `t`.
        - If no such substring exists, return `""`.
        
        Constraints:
        - The order of characters in `t` **does not** matter.
        - If multiple valid substrings exist, return the **smallest length** one.
        - Both `s` and `t` consist of uppercase and lowercase English letters.

        Clarifications:
        - Can `t` be longer than `s`? → Yes, return `""` immediately.
        - Are characters case-sensitive? → Yes.
        - Can `t` contain duplicate characters? → Yes.

        Example Walkthrough:
        Example 1:
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        Explanation:
        - The substring "BANC" contains all letters of "ABC" and is the shortest.

        Example 2:
        Input: s = "a", t = "a"
        Output: "a"

        Example 3:
        Input: s = "a", t = "aa"
        Output: ""
        Explanation:
        - `t` has more 'a's than `s`, so it's impossible.
        """

        # M - Match with Patterns
        """
        - **Sliding Window** technique is a perfect fit:
          - Expand `right` pointer until all `t` characters are found.
          - Shrink `left` pointer to minimize the window.
        - **HashMap (Frequency Counting)**
          - Use `countT` to track occurrences in `t`.
          - Use `window` to track occurrences in the current substring.
        """

        # P - Plan
        """
        1. **Edge Case:** If `t` is empty, return `""`.
        2. **Initialize:** Create frequency hashmap `countT` for `t`.
        3. **Sliding Window:**
           - Expand `right` pointer (`r`) until all characters are found.
           - Once all characters are found:
             - Try to **shrink** the window from `left` (`l`).
             - Update `res` if the new window is smaller.
        4. **Return the substring** using the stored indices.
        """

        if t == "":  # Step 1: Edge Case
            return ""

        countT, window = {}, {}  # Step 2: Frequency maps
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)  # Step 3: Track matches
        res, resLen = [-1, -1], float("infinity")
        l = 0
        
        for r in range(len(s)):  # Step 3: Expand right pointer
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:  # Valid character match
                have += 1

            while have == need:  # Step 4: Try shrinking the window
                if (r - l + 1) < resLen:  # Update result if new window is smaller
                    res = [l, r]
                    resLen = r - l + 1

                # Shrink window from the left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""  # Step 5: Return final substring

        """
        I - Implement
        - The algorithm uses **sliding window** to efficiently expand/shrink the substring.
        - **Time Complexity:** O(N), where N is the length of `s`.
        - **Space Complexity:** O(1), since at most 26 characters are stored.

        R - Review
        ✅ Handles case where `t` is larger than `s` → Output: `""`
        ✅ Handles cases where multiple valid substrings exist → Picks the **smallest** one.
        ✅ Uses **optimal** O(N) solution instead of brute force O(N²).

        E - Evaluate
        Edge Cases:
        1. `s = "a", t = "a"` → Output: `"a"`
        2. `s = "abc", t = "xyz"` → Output: `""`
        3. `s = "ADOBECODEBANC", t = "ABC"` → Output: `"BANC"`
        4. Large input case → **O(N) efficiency holds up**.
        """

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        ✅ U - Understand the Problem:
        - Given two strings `s` and `t`, compare them after applying backspace characters (`#`).
        - '#' means delete the character before it, if any.
        - Return True if final processed strings are equal, else False.

        Clarifying Questions:
        - Can there be multiple '#'s in a row? Yes.
        - Can '#' appear at the beginning of the string? Yes.
        - Do we need to return a new string or just compare them? Just compare them.

        ✅ M - Match the Pattern:
        - Stack-based approach is ideal:
          - We process characters, and if we hit `#`, we pop from the stack.
          - This replicates typing with backspaces.

        ✅ P - Plan:
        1. Use two stacks (`stack1`, `stack2`) for both strings.
        2. Traverse each string:
            - If char is '#': pop if stack not empty.
            - Else: push character to stack.
        3. Compare the final content of both stacks.

        ✅ I - Implement
        """
        stack1 = []
        stack2 = []

        for ch in s:
            if ch == "#" and not stack1:
                continue
            if ch == "#":
                stack1.pop()
            else:
                stack1.append(ch)

        for ch in t:
            if ch == "#" and not stack2:
                continue
            if ch == "#":
                stack2.pop()
            else:
                stack2.append(ch)

        return stack1 == stack2

        """
        ✅ R - Review:
        - If both stacks are equal after processing, return True.
        - Otherwise, return False.

        ✅ E - Evaluate:
        Time Complexity: O(n + m) — n is len(s), m is len(t)
        Space Complexity: O(n + m) — worst case stacks store all characters

        ✅ Edge Cases:
        - s = "ab#c", t = "ad#c" => True
        - s = "a##", t = "#" => True
        - s = "a#c", t = "b" => False
        """


"MORE OPTIMAL APPROACH COMING SOON"
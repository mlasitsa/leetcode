class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # U - Understand the Problem
        # Problem: Given a string of digits from 2–9, return all possible letter combinations 
        # based on the mapping of a telephone keypad. Each digit maps to 3-4 characters.
        #
        # Example:
        # Input: "23"
        # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        #
        # Constraints:
        # - Digits only range from '2' to '9'
        # - Return all possible combinations in any order
        # - If input is empty, return []

        # M - Match with Patterns
        # This is a classic **backtracking** problem where we explore all possible combinations.
        # Each digit maps to a fixed number of characters => leads to a tree of depth `len(digits)`

        # P - Plan
        # 1. Create a hashmap for digit-to-letter mapping
        # 2. Use backtracking to explore all letter combinations
        # 3. At each level of recursion, append a letter from the current digit
        # 4. If a combination reaches the same length as digits, add it to the result

        hmap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        if not digits:
            return []

        final = []
        digits = list(digits)

        # I - Implement
        def backtrack(start: int, combo: str):
            # Base case: if the combination is complete, store it
            if len(combo) == len(digits):
                final.append(combo)
                return

            # Recurse on all options for the current digit
            for i in range(start, len(digits)):
                for ch in hmap[digits[i]]:
                    combo += ch
                    backtrack(i + 1, combo)
                    combo = combo[:-1]  # Backtrack to previous state

        backtrack(0, "")

        # R - Review
        # We use a list for `final` and string slicing to undo choices (backtrack)
        # Handles duplicate digits and combinations cleanly

        # E - Evaluate
        # Time Complexity: O(4^n), where n = len(digits), since each digit maps to max 4 letters
        # Space Complexity: O(n) for the recursion stack, plus O(4^n) for the result list

        return final

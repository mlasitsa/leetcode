from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        U - Understand the Problem
        ----------------------------------
        Problem:
        - Given a list of candidates (may contain duplicates) and a target,
          return all unique combinations where the numbers sum up to the target.
        - Each number in candidates may be used **only once** in the combination.

        Clarifications:
        - Output must not contain duplicate combinations.
        - Elements can repeat in the input, but must not repeat in result if used already
        - Order of output combinations doesn't matter.
        
        Examples:
        Input: candidates = [10,1,2,7,6,1,5], target = 8
        Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
        """

        """
        M - Match with Patterns
        ----------------------------------
        This is a **Backtracking + Deduplication** problem:
        - Explore combinations recursively.
        - Since each number can only be used once, we must move to `i+1` in recursion.
        - To avoid duplicate combinations due to repeated numbers in input,
          we skip repeated values **at the same depth** of recursion.

        P - Plan
        ----------------------------------
        1. Sort the candidates list to handle duplicates easily.
        2. Use backtracking with:
            - `start`: index to begin from.
            - `combo`: current combination being built.
            - `total`: running sum.
        3. Base case:
            - If `total == target`, store a deep copy of combo.
            - If `total > target`, return early.
        4. Inside the loop:
            - Skip duplicates with: `if i > start and candidates[i] == candidates[i - 1]: continue`
            - Recurse with `i + 1` (no reuse).
            - Backtrack (pop from combo).
        """

        res = []
        candidates.sort()

        def backtrack(start, combo, total):
            if total == target:
                res.append(list(combo))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combo.append(candidates[i])
                backtrack(i + 1, combo, total + candidates[i])
                combo.pop()

        backtrack(0, [], 0)
        return res

        """
        R - Review
        ----------------------------------
        - We ensure duplicates are avoided by sorting and skipping same elements at the same depth.
        - Recursion is correctly controlled to not reuse elements.

        E - Evaluate
        ----------------------------------
        Time Complexity: 
        - O(2^n) in worst-case for exploring all subsets.
        Space Complexity: 
        - O(n) recursion stack and O(k) for output.
        """



# Alternative version using a Set to avoid duplicates
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        This version uses a Set to store unique combinations.
        Difference: Deduplication is done using a set of tuples.
        """

        res = set()
        candidates.sort()

        def backtrack(start, combo, total):
            if total == target:
                res.add(tuple(combo))  # Set ensures uniqueness
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                backtrack(i + 1, combo, total + candidates[i])
                combo.pop()

        backtrack(0, [], 0)
        return [list(t) for t in res]

        """
        E - Evaluate
        ----------------------------------
        Time Complexity: Still O(2^n) due to recursion.
        Space Complexity: Higher than deduplication-in-loop due to set.
        Tradeoff: Simpler logic but less space-efficient.
        """

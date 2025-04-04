class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        U - Understand the Problem
        ----------------------------------
        Problem:
        - Given a list of distinct integers `nums`, return all possible permutations.
        - A permutation is an ordered arrangement of elements.

        Constraints:
        - All elements in `nums` are unique.
        - Return list of lists containing all unique orderings.
        
        Example:
        Input: [1, 2, 3]
        Output: [
            [1,2,3], [1,3,2],
            [2,1,3], [2,3,1],
            [3,1,2], [3,2,1]
        ]
        """

        """
        M - Match with Patterns
        ----------------------------------
        - This is a classic **backtracking / recursion** problem.
        - Each position in the result can be filled with one of the unused elements.
        - Base case: If current array length equals original length, store a copy.
        - Avoid reusing the same element in the same permutation.
        """

        final = []
        seen = set()

        def helper(start, arr):
            nonlocal final, seen

            # P - Plan: Build each permutation recursively
            if len(arr) == len(nums):
                if tuple(arr) not in seen:
                    final.append(list(arr))  # Save a copy
                    seen.add(tuple(arr))     # Prevent duplicate permutations
                return

            for i in range(start, len(nums)):
                if nums[i] not in arr:  # Avoid using the same number twice in a single permutation
                    arr.append(nums[i])
                    helper(0, arr)      # Start index reset since we can choose any number again
                    arr.pop()           # Backtrack

        helper(0, [])
        return final

        """
        R - Review
        ----------------------------------
        - You correctly implemented a backtracking approach.
        - Using `tuple(arr)` in `seen` avoids duplicate permutations.
        - The extra `start` parameter is not necessary since you are checking `not in arr`.

        E - Evaluate
        ----------------------------------
        Time Complexity: O(n!) - where n is the length of `nums`.
        Space Complexity: O(n!) for output and O(n) for call stack.
        
        Optimization:
        - You can remove the `seen` set and the `start` parameter since all nums are distinct.
        - Instead of checking `if nums[i] not in arr`, use a `used` boolean array to improve lookup to O(1).
        """

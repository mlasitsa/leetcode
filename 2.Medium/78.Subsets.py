class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        U - Understand:
        ------------------
        Problem:
        - Given an integer array `nums`, return all possible subsets (the power set).
        - The solution must not contain duplicate subsets.
        - Order of elements in a subset doesn't matter, but each element can either be included or not.

        Clarifications:
        - No duplicate elements in `nums`.
        - Return result in any order.
        - Each subset is a unique combination of the input elements.

        Examples:
        Input: nums = [1,2,3]
        Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

        M - Match:
        ------------------
        - This is a classic **Backtracking / DFS / Combinatorics** problem.
        - We're generating all combinations → power set → 2^n subsets for n elements.
        - Pattern: Recursively include or exclude each element, building up subsets.

        P - Plan:
        ------------------
        - Initialize an empty result list `final`.
        - Use a recursive helper function:
            1. Append the current subset `res` to the result.
            2. Iterate through `nums` starting from `start` index:
                - Include current number
                - Recurse to the next element
                - Backtrack (remove the element to explore other paths)

        I - Implementation:
        ------------------
        """
        final = []

        def helper(start, res, final, nums):
            final.append(list(res))  # Add current subset (copy)
            for i in range(start, len(nums)):
                res.append(nums[i])           # Include nums[i]
                helper(i + 1, res, final, nums)
                res.pop()                     # Backtrack

        helper(0, [], final, nums)
        return final

        """
        R - Review:
        ------------------
        - All combinations are explored.
        - No duplicates due to increasing index traversal.
        - Backtracking ensures each path is fully explored.

        E - Evaluate:
        ------------------
        Time Complexity:
        - O(2^n): Each element can be included or not → 2^n subsets.

        Space Complexity:
        - O(n) recursion stack + O(2^n * n) for output storage.

        Notes:
        - Elegant recursive solution.
        - If duplicates were allowed, additional checks would be needed.
        """

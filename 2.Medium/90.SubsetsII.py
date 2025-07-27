class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        U - Understand the Problem
        ----------------------------------
        Problem:
        - Given a list of integers `nums` that may contain duplicates,
          return all possible subsets (the power set) without duplicate subsets.

        Constraints:
        - The result must not contain duplicate subsets.
        - Each subset can be in any order.
        - Input may include duplicate numbers.

        Example:
        Input: [1,2,2]
        Output: [[], [1], [2], [1,2], [2,2], [1,2,2]]
        """

        """
        M - Match with Patterns
        ----------------------------------
        Pattern: Backtracking (Subset generation)
        - Classic subset generation via recursion/backtracking.
        - To handle duplicates, we **sort** the array and **skip duplicate elements** during iteration
          if they are the same as the previous element at the same recursive level.
        """

        final = []
        nums.sort()  # Sorting helps to easily skip duplicates

        """
        P - Plan
        ----------------------------------
        1. Sort the input array to group duplicates together.
        2. Use backtracking to generate all subsets.
        3. At each recursive level:
            - Add the current subset to the final result.
            - Iterate from current `start` index to the end:
                - Skip elements that are equal to the previous element (if `i > start`)
                  to avoid duplicate subsets.
            - Add the current element to path, recurse deeper, then backtrack.
        """

        def helper(start, arr):
            final.append(arr[:])  # Add a copy of current subset

            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue

                arr.append(nums[i])
                helper(i + 1, arr)
                arr.pop()  # Backtrack

        helper(0, [])
        return final

        """
        R - Review
        ----------------------------------
        - Sorting the input ensures that duplicates are adjacent.
        - Skipping when `nums[i] == nums[i-1]` avoids repeated subsets.
        - Correct use of backtracking with clean recursion and backtracking.

        E - Evaluate
        ----------------------------------
        Time Complexity: O(2^n)
          - In the worst case (all elements unique), we generate 2^n subsets.
          - The duplicate-skipping logic avoids exponential duplication.

        Space Complexity: O(n) recursion depth + O(2^n * n) for result.

        Edge Cases:
        - Empty input: should return `[[]]`
        - All elements the same: should return unique subset combinations like `[[], [1], [1,1], [1,1,1]]`
        """

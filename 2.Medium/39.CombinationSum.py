class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        U - Understand the Problem:
        ---------------------------------
        Problem:
        - You're given a list of distinct integers `nums` and a target integer.
        - Return all **unique combinations** where chosen numbers sum to target.
        - You may reuse the same number an unlimited number of times.

        Clarifications:
        - All numbers are positive.
        - The same number can be chosen multiple times.
        - Combinations must be in non-descending order (implicitly handled by looping from current index).
        - Input does not contain duplicates, so we don't need extra handling for that.

        Example:
        Input: nums = [2,3,6,7], target = 7
        Output: [[2,2,3], [7]]

        M - Match with Patterns:
        ---------------------------------
        - Classic **Backtracking** problem (choose/not-choose each candidate).
        - DFS with a running `sum` and a current path.
        - Allow repeating elements → keep using `i` in recursive call (not `i+1`).
        - This is a **combination** problem (order of elements in each combination doesn't matter).

        P - Plan:
        ---------------------------------
        1. Use a recursive helper function with the following parameters:
            - `start`: index to control which elements can be reused (to avoid duplicates).
            - `summ`: current sum so far.
            - `arr`: current combination being built.
        2. If sum exceeds target → stop.
        3. If sum == target → add current path to result.
        4. Loop from `start` to `len(nums)`:
            - Add current number to `arr`.
            - Recurse with updated sum and same index `i` (reuse allowed).
            - Backtrack (remove the number and subtract from sum).

        I - Implement:
        ---------------------------------
        """
        final = []
        def helper(start, summ, arr):
            nonlocal final
            if summ > target:
                return
            if summ == target:
                final.append(list(arr))
                return  # return after valid combo

            for i in range(start, len(nums)):
                summ += nums[i]
                arr.append(nums[i])
                helper(i, summ, arr)  # NOT i+1 since we can reuse same element
                arr.pop()
                summ -= nums[i]

        helper(0, 0, [])
        return final

        """
        R - Review:
        ---------------------------------
        - Recursion is properly backtracking by popping and subtracting after each call.
        - Handles duplicate prevention by controlling index range.
        - Correctly terminates on overshoot or exact match.

        E - Evaluate:
        ---------------------------------
        Time Complexity:
        - O(2^T) where T = target: Worst-case is exponential due to the number of combinations explored.

        Space Complexity:
        - O(T) for the recursion depth and O(K) for storing combinations (K = total output length).

        Notes:
        - To further optimize, you can sort `nums` first and break early if `nums[i] > target - summ`.
        - Very clean implementation with classic backtracking template.
        """

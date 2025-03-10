from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given an array `nums`, find **all unique triplets** (i, j, k) such that:
          - nums[i] + nums[j] + nums[k] = 0.
          - i, j, and k are distinct indices.
          - The solution set must not contain duplicate triplets.

        Clarifications:
        - Can numbers be negative? → Yes.
        - Can we use the same element more than once? → No, indices must be distinct.
        - Should the triplets be in sorted order? → No, but output must be unique.
        - Can `nums` contain duplicate values? → Yes.
        - What if there are no triplets? → Return an empty list.

        Example Walkthrough:
        Example 1:
        Input: nums = [-1, 0, 1, 2, -1, -4]
        Output: [[-1, -1, 2], [-1, 0, 1]]
        Explanation: 
        - Two triplets sum to zero: [-1, -1, 2] and [-1, 0, 1].

        Example 2:
        Input: nums = [0, 1, 1]
        Output: []
        Explanation: No three numbers sum to zero.

        Example 3:
        Input: nums = [0, 0, 0]
        Output: [[0, 0, 0]]
        Explanation: Only one valid triplet.
        """

        # M - Match with Patterns
        """
        - Sorting + Two Pointers pattern works best here:
          - Sorting helps avoid duplicates.
          - Two-pointer approach efficiently finds valid triplets.
        - We avoid **O(N^3) brute force** by reducing complexity to **O(N^2)**.
        """

        # P - Plan
        """
        1. Sort `nums` → Helps with duplicate elimination.
        2. Iterate over `nums` using `left` pointer.
           - Skip duplicates to avoid duplicate triplets.
        3. Use two pointers:
           - `mid` starts from `left + 1`, `right` starts from the end.
           - Calculate `sum = nums[left] + nums[mid] + nums[right]`.
           - If sum < 0 → Move `mid` forward (increase sum).
           - If sum > 0 → Move `right` backward (decrease sum).
           - If sum == 0 → Store triplet and update both `mid` and `right` (avoid duplicates).
        4. Convert set to list and return.
        """

        final = set()
        nums.sort()  # Step 1: Sort input

        for left in range(len(nums) - 2):  # Step 2: Iterate over `left`
            mid, right = left + 1, len(nums) - 1  # Step 3: Two pointers

            while mid < right:  # Step 3: Find valid triplets
                summ = nums[left] + nums[mid] + nums[right]

                if summ < 0:
                    mid += 1  # Increase sum
                elif summ > 0:
                    right -= 1  # Decrease sum
                else:
                    final.add((nums[left], nums[mid], nums[right]))  # Store triplet
                    mid += 1
                    right -= 1

        return list(final)  # Step 4: Convert set to list

        """
        I - Implement
        - The code sorts `nums`, then uses a **two-pointer** approach to efficiently find triplets.

        R - Review
        - Time Complexity: **O(N^2)**
          - Sorting takes **O(N log N)**.
          - Two-pointer search runs in **O(N)** for each element → **O(N^2)** overall.
        - Space Complexity: **O(N)** (for storing results in a set).

        E - Evaluate
        Edge Cases:
        ✅ No valid triplet → `nums = [1, 2, 3]` → Output: `[]`
        ✅ All numbers are zero → `nums = [0, 0, 0, 0]` → Output: `[[0,0,0]]`
        ✅ Already sorted input → `nums = [-4, -1, -1, 0, 1, 2]` → Output: `[[-1, -1, 2], [-1, 0, 1]]`
        ✅ Large input case → Ensure efficiency holds for `nums` with 10⁵ elements.
        """

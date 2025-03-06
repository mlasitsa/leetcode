from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given an array of size `n`, find the majority element.
        - The majority element appears more than `n / 2` times.
        - The problem guarantees that a majority element **always** exists.

        Clarifications/Constraints:
        - `1 ≤ nums.length ≤ 5 * 10⁴`
        - The array contains **only integers** (positive or negative).
        - We must find the element **in O(N) time**.
        - **Must return a single element** (not a list).

        Example Walkthrough:
        Example 1:
        Input: nums = [3, 2, 3]
        Output: 3
        Explanation: 3 appears twice (more than 3/2 = 1.5 times).

        Example 2:
        Input: nums = [2, 2, 1, 1, 1, 2, 2]
        Output: 2
        Explanation: 2 appears 4 times (more than 7/2 = 3.5 times).
        """

        # M - Match with Patterns
        """
        - We need **counting** because we must determine frequency.
        - A **HashMap (Dictionary)** is ideal because:
          - O(1) lookup for checking occurrences.
          - O(N) time complexity for traversing the list once.
        - Alternative approaches (not used here):
          - Sorting (O(N log N), but we need O(N)).
          - Boyer-Moore Voting Algorithm (O(N) time, O(1) space).
        """

        # P - Plan
        """
        1. Create a frequency dictionary (`hmap`) using `Counter`.
        2. Determine the majority threshold (`n // 2`).
        3. Iterate over the dictionary and return the element that appears more than `n // 2` times.
        """

        hmap = Counter(nums)  # Step 1: Count occurrences

        majority = len(nums) // 2  # Step 2: Majority threshold

        for key, value in hmap.items():  # Step 3: Find the majority element
            if value > majority:
                return key

        """
        I - Implement
        - We implemented the **HashMap approach** using Python’s `Counter`.
        - We iterate through the dictionary to find the majority element.

        R - Review
        - Time Complexity: O(N) (since we iterate through `nums` once).
        - Space Complexity: O(N) (since we store counts in a dictionary).

        E - Evaluate
        - Edge Cases:
          ✅ Only one element in `nums` → Should return that element.
          ✅ All elements are identical → Should return that element.
          ✅ Large `nums` input → Should run efficiently in O(N).
          ✅ Negative numbers in `nums` → Works correctly.
        """

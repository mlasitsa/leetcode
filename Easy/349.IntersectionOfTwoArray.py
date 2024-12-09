class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given two arrays, return their intersection as a list.
        - Each element in the result must be unique.

        Clarifications/Constraints:
        - Input arrays can contain duplicates.
        - Result should only contain unique elements, even if an element appears multiple times in the input arrays.
        - Order of the result does not matter.

        Examples:
        Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2] -> Output: [2]
        Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4] -> Output: [4, 9]

        Potential clarifying questions for an interview:
        1. Can the arrays contain negative numbers? (Yes.)
        2. Can the result contain duplicates? (No, only unique elements in the intersection.)
        3. Should the result be sorted? (No specific order is required.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use sets to handle uniqueness efficiently:
        #   * Add elements of the first array to a set (`store`).
        #   * Traverse the second array and check for intersection with `store`.
        #   * Add matching elements to a result set (`arr`) to ensure uniqueness.

        """
        P - Plan
        1. Initialize two sets:
           - `store` to store unique elements of `nums1`.
           - `arr` to store the intersection of `nums1` and `nums2`.
        2. Traverse `nums1` and add its elements to `store`.
        3. Traverse `nums2`:
           - If an element exists in `store`, add it to `arr`.
        4. Convert `arr` to a list and return it.
        """

        arr = set()  # Set to store intersection elements
        store = set()  # Set to store unique elements from nums1

        # Step 2: Add elements of nums1 to `store`
        for num in nums1:
            store.add(num)

        # Step 3: Find intersection by checking nums2 against `store`
        for num in nums2:
            if num in store:
                arr.add(num)

        # Step 4: Convert result set to list and return
        return list(arr)

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2] -> Output: [2]
2. Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4] -> Output: [4, 9]
3. Input: nums1 = [], nums2 = [] -> Output: []

Edge Cases:
1. One or both arrays are empty -> Output: []
2. Arrays with no intersection -> Output: []
3. Arrays with all elements intersecting -> Output: Unique elements of either array.

Time Complexity:
- O(n + m): Traverse `nums1` (n elements) and `nums2` (m elements).

Space Complexity:
- O(n): Space for the `store` set to hold unique elements from `nums1`.
"""

sol = Solution()
res = sol.intersection([1, 2, 2, 1], [2, 2])

if res == [2] or res == [2]:  # Acceptable as order does not matter
    print("Good Job")
else:
    print("Try Again...")

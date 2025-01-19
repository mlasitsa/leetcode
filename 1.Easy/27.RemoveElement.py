class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given an array `nums` and an integer `val`, remove all occurrences of `val` in-place.
        - The relative order of elements not equal to `val` may be changed.
        - Return the number of elements that are not equal to `val`.

        Clarifications/Constraints:
        - You must do this in-place with O(1) extra memory.
        - The function should modify `nums` directly, and only the first `k` elements of `nums` should be considered valid.

        Examples:
        Input: nums = [3, 2, 2, 3], val = 3 -> Output: 2, nums = [2, 2, _, _]
        Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2 -> Output: 5, nums = [0, 1, 3, 0, 4, _, _, _]

        Potential clarifying questions for an interview:
        1. Can `val` be absent from the array? (Yes, return the length of the array.)
        2. What should be done with the unused elements of `nums`? (They can be left as is, as only the first `k` elements are valid.)
        3. Can the array be empty? (Yes, return 0.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Two-pointer technique:
        #   * One pointer (`k`) to track the position of valid elements.
        #   * Another pointer (`i`) to iterate through the array.

        """
        P - Plan
        1. Initialize a pointer `k` to track the position for valid elements in `nums`.
        2. Iterate through `nums` using a loop:
           - If the current element is not equal to `val`, copy it to index `k` and increment `k`.
        3. Return `k`, which represents the number of valid elements in `nums`.
        """

        k = 0  # Step 1: Initialize pointer to track valid elements

        # Step 2: Iterate through the array
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move valid element to the position `k`
                k += 1  # Increment `k`

        # Step 3: Return the count of valid elements
        return k

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: nums = [3, 2, 2, 3], val = 3 -> Output: 2, nums = [2, 2, _, _]
2. Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2 -> Output: 5, nums = [0, 1, 3, 0, 4, _, _, _]
3. Input: nums = [], val = 0 -> Output: 0, nums = []

Edge Cases:
1. Array with all elements equal to `val` -> Output: 0.
2. Array with no elements equal to `val` -> Output: Length of the array.
3. Empty array -> Output: 0.

Time Complexity:
- O(n): The array is traversed once.

Space Complexity:
- O(1): The operation is done in-place without using extra memory.
"""

sol = Solution()
nums = [3, 2, 2, 3]
val = 3
res = sol.removeElement(nums, val)

if res == 2 and nums[:res] == [2, 2]:
    print("Good Job")
else:
    print("Try Again...")

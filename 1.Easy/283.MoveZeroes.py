# Problem: Move all zeros to the end of the array while maintaining the relative order of non-zero elements.
# Constraints:
# - Modify in-place.
# - Must minimize operations.
# - Return nothing.

# U - Understand
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# We can only use O(1) extra space and must do this in-place.
# Maintain relative order of non-zero elements.
# Edge cases:
# - All elements are zeros
# - No zero at all
# - One element

# M - Match
# - This problem matches the **in-place array manipulation** pattern.
# - Often solved with **two-pointer** or **partitioning** logic.

# P - Plan (Your Approach)
# 1. Count total number of zeros.
# 2. Iterate through the array.
#    - If an element is zero, remove it and append to the end.
#    - Adjust index if popped.
#    - Only iterate up to len(nums) - zeroCount since rest will be filled.
# 3. Time complexity is O(n^2) due to pop and append operations in-place.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for n in nums:
            if n == 0:
                count += 1

        i = 0
        while i < len(nums) - count:
            if nums[i] == 0:
                el = nums.pop(i)
                nums.append(el)
                i -= 1  # recheck the new value at index i
            i += 1

# E - Evaluate (Your Approach)
# Time: O(n^2) due to pop(i)
# Space: O(1)
# Correct, but inefficient for large input sizes.

# --------------------------------------------------------------------

# P - Plan (Optimal Two-Pointer Approach)
# 1. Use `insertPos` to track the next position for a non-zero element.
# 2. First loop: Move all non-zero values to the front.
# 3. Second loop: Fill the rest with 0s.
# 4. Time: O(n), Space: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insertPos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insertPos] = nums[i]
                insertPos += 1
        for i in range(insertPos, len(nums)):
            nums[i] = 0

# E - Evaluate (Optimal)
# Time: O(n)
# Space: O(1)
# Efficient for large inputs and passes all constraints.

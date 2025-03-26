'''
I DIDNT SOLVE THIS PROBLEM IN O(N) AND O(1) TIME, TO ACCOMPLISH THIS, YOU NEED TO CHECK XOR OPERATOR
I HAVENT WORKED THAT MUCH WITH XOR, SO DO YOUR JOB, GOOD LUCK :)
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        U - Understand the Problem
        --------------------------
        Problem:
        - In an array where every element appears exactly twice except one, return the element that appears only once.

        Clarifications:
        - The array is non-empty.
        - All elements except one appear exactly twice.
        - No use of extra space (O(1) space preferred).
        
        Examples:
        - Input: [4,1,2,1,2] → Output: 4
        - Input: [2,2,1] → Output: 1
        """

        # M - Match with Pattern
        # ----------------------
        # - Sorting helps to bring duplicates next to each other.
        # - Use a pointer to iterate in pairs (i and i+1). The unique number will break the pattern.

        # P - Plan
        # --------
        # 1. Sort the array.
        # 2. Traverse in steps of 2. If nums[i] != nums[i+1], return nums[i].
        # 3. If no mismatch is found, return the last element (guaranteed to be unique).

        nums.sort()

        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 2

        # Last element must be the unique one if not found earlier
        return nums[-1]

        """
        R - Review
        ----------
        - Sorting places all duplicates adjacent to each other.
        - A mismatch in pairs reveals the unique element.

        E - Evaluate
        ------------
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1) (assuming in-place sorting is allowed)
        Avoids extra memory
        Works with two-pointer idea
        Not linear time, but acceptable if O(n log n) is okay
        """

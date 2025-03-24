class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        U - Understand the Problem
        Problem Statement:
        - Return True if there are any duplicate elements in the list.
        - Otherwise, return False.
        
        Clarifications:
        - Can be positive or negative integers.
        - Return True as soon as any duplicate is found.

        M - Match
        - This is a common "Duplicate Detection" pattern.
        - HashSet provides O(1) average time lookup and insertion.

        P - Plan
        1. Create an empty set.
        2. Traverse the array.
        3. If the number already exists in the set, return True.
        4. Otherwise, add it to the set.
        5. Return False if no duplicates found.

        I - Implement
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        """
        R - Review
        Edge Cases:
        - Empty list → return False
        - One element → return False
        - All elements same → return True

        E - Evaluate
        Time: O(n)
        Space: O(n)
        """


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        U - Understand the Problem
        Same as above

        M - Match
        - Sorting is useful when checking adjacent elements.
        - Once sorted, duplicates will appear next to each other.

        P - Plan
        1. Sort the array in-place.
        2. Traverse through it once and compare adjacent elements.
        3. If any nums[i] == nums[i+1], return True.
        4. Else return False at end.

        I - Implement
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

        """
        R - Review
        Same edge cases apply.

        E - Evaluate
        Time: O(n log n) due to sorting
        Space: O(1) if sorting in-place
        """

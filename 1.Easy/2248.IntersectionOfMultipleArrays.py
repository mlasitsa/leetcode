class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a list of integer arrays `nums`, find the intersection of all arrays.
        - Return the intersection in sorted order.
        - The intersection contains elements that appear in every array.

        Clarifications/Constraints:
        - Each array contains unique integers.
        - The length of `nums` can vary, and each sub-array can have different sizes.
        - If there is no intersection, return an empty list.

        Examples:
        Input: nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [4, 3, 2]]
        Output: [2, 3, 4]

        Input: nums = [[1, 2, 3], [4, 5, 6]] -> Output: []

        Potential clarifying questions for an interview:
        1. Can the arrays be empty? (Yes, handle accordingly.)
        2. Are there any duplicate elements within individual arrays? (No, each sub-array contains unique integers.)
        3. Should the result be sorted? (Yes, as specified in the problem.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a hash map to count the frequency of each element across all arrays.
        # - Any element with a frequency equal to the number of arrays (`len(nums)`) is part of the intersection.

        """
        P - Plan
        1. Create a hash map (`hmap`) to store the frequency of each element across all arrays.
        2. Traverse each sub-array in `nums`:
           - For each element, increment its count in the hash map.
        3. Iterate over the hash map to collect elements with frequency equal to `len(nums)`.
        4. Sort the resulting list of intersection elements.
        5. Return the sorted list.
        """

        hmap = {}  # Step 1: Initialize a hash map to store frequencies
        arr = []   # To store the final intersection elements
        n = len(nums)  # Number of arrays in `nums`

        # Step 2: Traverse each sub-array and count element frequencies
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] in hmap:
                    hmap[nums[i][j]] += 1
                else:
                    hmap[nums[i][j]] = 1
        
        # Step 3: Collect elements with frequency equal to `len(nums)`
        for key, value in hmap.items():
            if value == n:  # Element is present in all arrays
                arr.append(key)
        
        # Step 4: Sort the resulting intersection elements
        arr.sort()

        # Step 5: Return the sorted intersection list
        return arr

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [4, 3, 2]] -> Output: [2, 3, 4]
2. Input: nums = [[1, 2, 3], [4, 5, 6]] -> Output: []
3. Input: nums = [[1, 2, 3]] -> Output: [1, 2, 3]

Edge Cases:
1. Single array in `nums` -> Output: The array itself sorted.
2. No intersection between arrays -> Output: []
3. Empty input array (`nums = []`) -> Output: []

Time Complexity:
- O(n * m): Where `n` is the number of arrays and `m` is the average size of each array.

Space Complexity:
- O(k): Where `k` is the number of unique elements across all arrays.
"""

# Test example
sol = Solution()
res = sol.intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [4, 3, 2]])

if res == [2, 3, 4]:
    print("Good Job")
else:
    print("Try Again...")

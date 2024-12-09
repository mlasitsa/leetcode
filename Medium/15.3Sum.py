class Solution(object):
    def threeSum(self, nums):
        """
        U - Understand the Problem
        Problem Statement:
        - Given an integer array `nums`, find all unique triplets `[nums[i], nums[j], nums[k]]` such that:
          1. `i != j != k`
          2. `nums[i] + nums[j] + nums[k] == 0`.
        - The solution set must not contain duplicate triplets.

        Clarifications/Constraints:
        - The input array can have both positive and negative integers, including zero.
        - The result should only include unique triplets.
        - The array size can be large, so efficiency is important.

        Examples:
        Input: nums = [-1, 0, 1, 2, -1, -4]
        Output: [[-1, -1, 2], [-1, 0, 1]]
        Explanation:
        - The triplets [-1, -1, 2] and [-1, 0, 1] sum to zero. Duplicate triplets are not allowed.

        Input: nums = []
        Output: []

        Input: nums = [0]
        Output: []

        Potential clarifying questions for an interview:
        1. Can the input array contain duplicates? (Yes.)
        2. Should the result include only unique triplets? (Yes.)
        3. Can the input array be empty or contain a single element? (Yes, return an empty list in such cases.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Sort the array to enable efficient duplicate elimination and two-pointer traversal.
        # - Use a loop to fix the first element of the triplet.
        # - Use two pointers to find pairs that sum to the negative of the fixed element.

        """
        P - Plan
        1. Sort the array to simplify duplicate handling and two-pointer traversal.
        2. Iterate through the array:
           - Skip duplicates for the fixed element.
           - Use two pointers (`left` and `right`) to find pairs that sum to the negative of the fixed element.
           - Append the triplet to the result if a match is found.
           - Skip duplicates for the `left` and `right` pointers.
        3. Return the result list containing all unique triplets.
        """

        nums.sort()  # Step 1: Sort the array
        answer = []  # To store the result triplets

        for i in range(len(nums)):
            # Step 2: Skip duplicates for the fixed element
            if nums[i] > 0:  # No need to continue if the fixed element is greater than 0
                break
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue

            left = i + 1  # Pointer to the next element
            right = len(nums) - 1  # Pointer to the last element

            # Step 3: Two-pointer approach to find valid triplets
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ == 0:
                    # Found a triplet
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for `left` and `right`
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif summ > 0:
                    # If the sum is too large, move `right` left
                    right -= 1
                else:
                    # If the sum is too small, move `left` right
                    left += 1

        return answer

# Example Usage
sol = Solution()

"""
E - Evaluate
Test the solution with examples:
1. Input: nums = [-1, 0, 1, 2, -1, -4] -> Output: [[-1, -1, 2], [-1, 0, 1]]
2. Input: nums = [] -> Output: []
3. Input: nums = [0] -> Output: []

Edge Cases:
1. Empty array -> Output: []
2. Single element or two elements -> Output: []
3. Large array with many duplicates -> Ensure duplicates are handled properly.

Time Complexity:
- O(n^2): The outer loop runs O(n) times, and the two-pointer approach runs O(n) in the worst case.

Space Complexity:
- O(1): The result list is the only additional space used, and it scales with the output size.
"""

res = sol.threeSum([-1, 0, 1, 2, -1, -4])
expected = [[-1, -1, 2], [-1, 0, 1]]

if res == expected:
    print("Good Job")
else:
    print("Try Again...")

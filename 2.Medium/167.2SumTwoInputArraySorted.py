class Solution(object):
    def twoSum(self, numbers, target):
        """
        U - Understand the Problem
        Problem Statement:
        - Given a sorted array `numbers`, find two numbers such that they add up to a specific `target`.
        - Return the indices of the two numbers (1-based index) as a list `[index1, index2]`.
        - Each input has exactly one solution, and the same element cannot be used twice.

        Clarifications/Constraints:
        - The array is sorted in non-decreasing order.
        - Indices returned should be 1-based.
        - Assume there is exactly one solution.

        Examples:
        Input: numbers = [2, 7, 11, 15], target = 9 -> Output: [1, 2]
        Input: numbers = [2, 3, 4], target = 6 -> Output: [1, 3]
        Input: numbers = [-1, 0], target = -1 -> Output: [1, 2]

        Potential clarifying questions for an interview:
        1. Can the input array contain duplicates? (Yes, but only one valid pair exists.)
        2. What is the expected time complexity? (Aim for better than O(n^2), potentially O(n) or O(log n) with binary search.)
        3. How should the solution handle large input sizes? (Use efficient search techniques.)

        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Since the array is sorted, a two-pointer technique or binary search can optimize the solution.
        # - A brute-force approach with nested loops will work but is less efficient.

        """
        P - Plan
        1. Iterate through the array using an outer loop.
           - Skip duplicate elements to avoid unnecessary computations.
        2. For each element, use a pointer to check subsequent elements in the array.
           - If the sum of the current element and the pointer equals the target, return their indices (1-based).
           - Otherwise, move the pointer forward.
        3. If no solution is found during iteration (should not happen due to problem constraints), return an empty list.
        """

        for i in range(len(numbers)):
            # Skip duplicate elements
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            pointer = i + 1  # Start pointer at the next element

            # I - Implement
            while pointer < len(numbers):
                # Check if the sum matches the target
                if numbers[i] + numbers[pointer] == target:
                    return [i + 1, pointer + 1]  # Return 1-based indices
                else:
                    pointer += 1  # Move pointer forward

        # This return statement is unnecessary due to problem constraints
        return []

# Example Usage
sol = Solution()

"""
E - Evaluate
Test the solution with examples:
1. Input: numbers = [2, 7, 11, 15], target = 9 -> Output: [1, 2]
2. Input: numbers = [2, 3, 4], target = 6 -> Output: [1, 3]
3. Input: numbers = [-1, 0], target = -1 -> Output: [1, 2]

Edge Cases:
1. Smallest possible array (2 elements) -> Output: Indices of the two elements.
2. Target sum requires the first and last elements -> Ensure the indices are correct.
3. Array contains negative numbers -> Output: Valid indices if a solution exists.

Time Complexity:
- O(n^2): Iterative approach with nested loops.
- Can be optimized to O(n) using two-pointer or O(n log n) with binary search.

Space Complexity:
- O(1): Constant space used.
"""

# Test example
res = sol.twoSum([2, 7, 11, 15], 9)

if res == [1, 2]:
    print("Good Job")
else:
    print("Try Again...")

from typing import List
import collections

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given three integer arrays `arr1`, `arr2`, and `arr3`, find the intersection of these arrays.
        - Return the intersection as a list of integers sorted in ascending order.

        Clarifications/Constraints:
        - All arrays are sorted in non-decreasing order.
        - Elements in the result must appear in all three arrays.
        - No duplicates within the same array.

        Examples:
        Input: arr1 = [1, 2, 3, 4, 5], arr2 = [1, 2, 5, 7, 9], arr3 = [1, 3, 4, 5, 8]
        Output: [1, 5]

        Input: arr1 = [1, 2, 3], arr2 = [4, 5, 6], arr3 = [7, 8, 9]
        Output: []

        Potential clarifying questions for an interview:
        1. Are there any constraints on the size of the arrays? (No specific constraints.)
        2. Are the arrays always sorted? (Yes.)
        3. Should the result contain duplicates if the input arrays have duplicates? (No, return unique values in the intersection.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a `Counter` from the `collections` module to count the frequency of elements across all arrays.
        # - Elements with a frequency equal to 3 (appear in all three arrays) form the intersection.

        """
        P - Plan
        1. Concatenate all three arrays into one and use `collections.Counter` to count the frequency of each element.
        2. Iterate over the `Counter` to find elements with a frequency of 3.
        3. Append these elements to the result list.
        4. Return the result list.
        """

        # Step 1: Use Counter to count frequencies of elements across all arrays
        counter = collections.Counter(arr1 + arr2 + arr3)  # Combine all arrays and count frequencies

        # Step 2: Find elements with frequency 3
        ans = []
        for item in counter:
            if counter[item] == 3:
                ans.append(item)

        # Step 3: Return the result (it is already sorted since input arrays are sorted)
        return ans

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: arr1 = [1, 2, 3, 4, 5], arr2 = [1, 2, 5, 7, 9], arr3 = [1, 3, 4, 5, 8] -> Output: [1, 5]
2. Input: arr1 = [1, 2, 3], arr2 = [4, 5, 6], arr3 = [7, 8, 9] -> Output: []
3. Input: arr1 = [1, 1], arr2 = [1], arr3 = [1] -> Output: [1]

Edge Cases:
1. Empty arrays -> Output: []
2. Arrays with no common elements -> Output: []
3. Arrays with all elements common -> Output: Intersection of all arrays.

Time Complexity:
- O(n): Combining the arrays and iterating over the `Counter`.

Space Complexity:
- O(n): Space for the `Counter` to store unique elements and their counts.
"""

sol = Solution()
res = sol.arraysIntersection([1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8])

if res == [1, 5]:
    print("Good Job")
else:
    print("Try Again...")

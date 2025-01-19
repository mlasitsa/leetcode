class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given two arrays, return their intersection as a list.
        - Each element in the result must appear as many times as it shows in both arrays.

        Clarifications/Constraints:
        - Input arrays can contain duplicates.
        - The order of the result does not matter.

        Examples:
        Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2] -> Output: [2, 2]
        Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4] -> Output: [4, 9] or [9, 4]

        Potential clarifying questions for an interview:
        1. Should the result contain duplicates if they exist in both arrays? (Yes, based on the minimum count.)
        2. Should the result be sorted? (No specific order is required.)
        3. Can the arrays be empty? (Yes, return an empty list.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a hash map to count the frequency of elements in one array.
        # - Traverse the second array and check for intersections by decrementing the count in the hash map.

        """
        P - Plan
        1. Create a hash map (`hmap`) to store the frequency of elements in `nums1`.
        2. Traverse `nums1`:
           - Increment the count of each element in the hash map.
        3. Traverse `nums2`:
           - If an element exists in `hmap` with a count > 0, append it to the result list and decrement the count.
        4. Return the result list containing the intersection.
        """

        hmap = {}  # Hash map to store the frequency of elements in nums1
        arr = []   # To store the result intersection elements

        # Step 2: Build the hash map from nums1
        for num in nums1:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1

        # Step 3: Traverse nums2 to find the intersection
        for num in nums2:
            if num in hmap and hmap[num] > 0:  # Check if the element exists and has a positive count
                arr.append(num)  # Add the element to the result
                hmap[num] -= 1   # Decrement the count in the hash map

        # Step 4: Return the result list
        return arr

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2] -> Output: [2, 2]
2. Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4] -> Output: [4, 9]
3. Input: nums1 = [], nums2 = [] -> Output: []

Edge Cases:
1. One or both arrays are empty -> Output: []
2. Arrays with no intersection -> Output: []
3. Arrays with all elements intersecting -> Output: Intersection based on counts.

Time Complexity:
- O(n + m): Traverse `nums1` (n elements) and `nums2` (m elements).

Space Complexity:
- O(n): Space for the `hmap` to store counts of elements in `nums1`.
"""

sol = Solution()
res = sol.intersect([1, 2, 2, 1], [2, 2])

if res == [2, 2]:  # Acceptable as order does not matter
    print("Good Job")
else:
    print("Try Again...")

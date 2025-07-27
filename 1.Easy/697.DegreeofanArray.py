from typing import List
import heapq

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        U - Understand the Problem
        - We are given an array `nums`, and we need to find the smallest subarray that has the same degree as the entire array.
        - The degree of an array is the maximum frequency of any number in the array.
        - The subarray must contain all occurrences of the most frequent element.

        Constraints:
        - `nums.length` >= 1
        - `nums` contains positive integers.

        Examples:
        Input: nums = [1,2,2,3,1,4,2]
        Output: 6
        Explanation: The most frequent element is `2`, appearing 3 times. The shortest subarray containing all `2`s is `[2,2,3,1,4,2]` of length 6.

        Input: nums = [1,2,2,3,1]
        Output: 2
        Explanation: `1` and `2` both have a degree of `2`. The shortest subarray for `2` is `[2,2]` of length 2.

        """

        """
        M - Match with Patterns
        - This problem involves frequency counting (HashMap) and finding min/max values (Heap or Two Pointers).
        - Two common approaches:
            1. O(N log N) using a max heap:
                - Store frequency in a HashMap.
                - Use a max heap to retrieve the most frequent elements efficiently.
                - Extract the shortest subarray containing all occurrences of the most frequent element.
            2. O(N) using HashMap tracking first & last index (optimized approach):
                - Track the first and last occurrence of each number.
                - Compute the degree and determine the shortest subarray.
        """

        """
        P - Plan
        Approach 1: O(N log N) using a heap
        - Step 1: Store indices of each number in a dictionary.
        - Step 2: Use a max heap (inverted with negative frequency) to find the most frequent elements.
        - Step 3: Pop elements from the heap, compute subarray lengths, and return the minimum.

        Approach 2: O(N) optimized solution
        - Step 1: Store the first occurrence, last occurrence, and count of each number.
        - Step 2: Compute the degree of the array.
        - Step 3: Traverse the hashmap and find the shortest subarray with max degree.
        """

        # O(N log N) Approach: Using Max Heap
        hmap = {}

        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]].append(i)
            else:
                hmap[nums[i]] = [i]

        heap = []
        for key, value in hmap.items():
            heapq.heappush(heap, (-len(value), key))  # Use negative length for max heap
        
        item, key = heapq.heappop(heap)
        indexes = hmap[key]
        minLen = indexes[-1] - indexes[0] + 1

        while heap:
            item1, key1 = heapq.heappop(heap)
            if item < item1:
                return minLen
            else:
                minLen = min(minLen, hmap[key1][-1] - hmap[key1][0] + 1)

        return minLen


    def findShortestSubArrayOptimized(self, nums: List[int]) -> int:
        """
        O(N) Optimized Approach (HashMap without heap)
        - Store frequency, first index, and last index in a single pass.
        - Compute the degree and find the shortest subarray.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        first_seen = {}
        count = {}
        degree = 0
        minLen = float("inf")

        for i, num in enumerate(nums):
            if num not in first_seen:
                first_seen[num] = i  # Store first occurrence
            count[num] = count.get(num, 0) + 1  # Update frequency
            degree = max(degree, count[num])  # Update max degree

        # Find the minimum subarray length with max degree
        for num in count:
            if count[num] == degree:
                minLen = min(minLen, i - first_seen[num] + 1)

        return minLen

        """
        R - Review
        O(N log N) Heap Approach:
        - Time Complexity: `O(N log N)`, since heap operations take `O(log N)`.
        - Space Complexity: `O(N)`, since we store index positions in a hashmap.

        O(N) Optimized Approach:
        - Time Complexity: `O(N)`, since we process `nums` in a single pass.
        - Space Complexity: `O(N)`, since we use a dictionary.

        Edge Cases:
        - `[1,1,1,1,1]` → Already the entire array, should return `5`.
        - `[1,2,3,4,5]` → All elements have degree `1`, should return `1`.
        - `[1,2,2,3,1,4,2]` → Should return `6` (degree `3` for `2`).
        """

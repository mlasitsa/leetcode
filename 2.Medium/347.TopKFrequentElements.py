class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.
        - The output order does not need to be sorted.

        Clarifications/Constraints:
        - The input `nums` is non-empty.
        - The frequency of each element is guaranteed to be unique (no ties for frequency).
        - The value of `k` is always valid (1 <= k <= len(nums)).

        Examples:
        Input: nums = [1, 1, 1, 2, 2, 3], k = 2
        Output: [1, 2]

        Input: nums = [1], k = 1
        Output: [1]

        Potential clarifying questions:
        1. Can the input contain negative integers? (Yes.)
        2. Should the output be in any specific order? (No, any order is acceptable.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a hashmap to count the frequency of each number.
        # - Use a bucket array where the index represents the frequency.
        # - Iterate through the bucket array in reverse to retrieve the most frequent elements.

        """
        P - Plan
        1. Use a hashmap to count the frequency of each number in the input array.
        2. Create a bucket array of length `len(nums) + 1`, where each index represents a frequency.
        3. Iterate over the hashmap and append each number to the corresponding bucket based on its frequency.
        4. Traverse the bucket array in reverse order:
           - Append numbers to the result list until the result list contains `k` elements.
        5. Return the result list.
        """

        # Step 1: Count the frequency of each number
        hmap = {}
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1

        # Step 2: Create the bucket array
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in hmap.items():
            bucket[freq].append(num)

        # Step 3: Collect the top k frequent elements
        result = []
        for i in range(len(bucket) - 1, 0, -1):  # Traverse the bucket array in reverse
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: nums = [1, 1, 1, 2, 2, 3], k = 2 -> Output: [1, 2]
2. Input: nums = [1], k = 1 -> Output: [1]
3. Input: nums = [4, 1, -1, 2, -1, 2, 3], k = 2 -> Output: [-1, 2]

Edge Cases:
1. Single element array -> Output: [element itself].
2. All elements are the same -> Output: [the element itself].

Time Complexity:
- O(n): Counting frequencies and filling the bucket array.
- O(n + k): Traversing the bucket array and collecting `k` elements.

Space Complexity:
- O(n): Space for the hashmap and bucket array.
"""

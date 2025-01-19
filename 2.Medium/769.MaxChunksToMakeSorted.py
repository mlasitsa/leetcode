class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given an array `arr` of length `n` that represents a permutation of integers in the range `[0, n-1]`,
          split the array into the maximum number of chunks such that after sorting each chunk individually
          and concatenating them, the result is a sorted array.

        Clarifications/Constraints:
        - The array is always a permutation of `[0, n-1]`.
        - Each number appears exactly once in the array.
        - Chunks can be of any size.

        Examples:
        Input: arr = [1, 0, 2, 3, 4]
        Output: 4
        Explanation:
        - Chunks: [1, 0], [2], [3], [4].
        - Sorted chunks concatenated: [0, 1, 2, 3, 4].

        Input: arr = [4, 3, 2, 1, 0]
        Output: 1
        Explanation:
        - The entire array must be one chunk.

        Potential clarifying questions for an interview:
        1. Are duplicates possible? (No, array is a permutation.)
        2. Is the array always non-empty? (Yes, array length is at least 1.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Iterate through the array and track the maximum value seen so far.
        # - If at any index `i`, the maximum value seen equals `i`, we can form a chunk up to that index.

        """
        P - Plan
        1. Initialize `max_seen` to track the maximum value encountered so far.
        2. Initialize `chunk_count` to 0 to count the chunks.
        3. Traverse the array:
           - Update `max_seen` with the maximum of `max_seen` and `arr[i]`.
           - If `max_seen` equals the current index `i`, increment `chunk_count`.
        4. Return `chunk_count`.
        """

        # Step 1: Initialize variables
        max_seen = 0
        chunk_count = 0

        # Step 2: Traverse the array
        for i in range(len(arr)):
            max_seen = max(max_seen, arr[i])  # Update the maximum value seen
            if max_seen == i:  # If the maximum matches the current index
                chunk_count += 1  # Increment the chunk count

        # Step 3: Return the total chunk count
        return chunk_count

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: arr = [1, 0, 2, 3, 4] -> Output: 4
2. Input: arr = [4, 3, 2, 1, 0] -> Output: 1
3. Input: arr = [2, 0, 1, 3, 4] -> Output: 3

Edge Cases:
1. Single element array -> Output: 1.
2. Array already sorted -> Output: n (length of the array).
3. Array in reverse order -> Output: 1.

Time Complexity:
- O(n): Traverse the array once.

Space Complexity:
- O(1): Constant space usage.
"""

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


# Alternative solution using heap:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        U - Understand:
        - Problem: Given a list of integers `nums`, find the **K most frequent** elements.
        - Return the elements in **any order**.
        - Constraints:
          1. `1 <= nums.length <= 10^5`
          2. `k` is **always valid** (`1 <= k <= unique elements in nums`).
          3. The output **does not need to be sorted**.

        Examples:
        ```
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]

        Input: nums = [1], k = 1
        Output: [1]
        ```

        Edge Cases:
        1. **All elements unique:** `[1,2,3,4]` with `k=2` should return `[3,4]` (or any top 2).
        2. **All elements the same:** `[2,2,2,2]`, `k=1` should return `[2]`.
        3. **Large `k` values:** Ensure `k` is not greater than unique elements in `nums`.

        M - Match:
        - **HashMap + Heap (Priority Queue)**
          1. Use **HashMap** (`dict`) to count occurrences.
          2. Use **Min-Heap (Priority Queue)** to keep track of top `k` elements efficiently.

        P - Plan:
        1. **Build a frequency map (`hmap`)** to store `{num: frequency}`.
        2. **Use a Min-Heap (`heapq`)**:
           - Insert `(-frequency, num)` to create a **Max-Heap** using negative values.
           - Extract the **top `k` elements**.
        3. **Return the extracted elements as the final result**.

        I - Implement:
        '''
        hmap = {}

        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1

        heap = []

        for key, v in hmap.items():
            heapq.heappush(heap, (-v, key))  # Use negative frequency for max heap

        final = []

        while len(final) < k:
            count, item = heapq.heappop(heap)
            final.append(item)
        
        return final
    

    

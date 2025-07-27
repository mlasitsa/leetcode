from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        U - Understand:
        - Problem: Given an array `nums` containing only `0s`, `1s`, and `2s`, sort the array **in-place** so that:
          - All `0s` appear first.
          - All `1s` appear in the middle.
          - All `2s` appear last.
        - Constraint: Must run in **O(n) time** using **constant space** (O(1)).

        Example:
        ```
        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
        ```

        Edge Cases:
        1. **All 0s:** `[0, 0, 0]` → Already sorted.
        2. **All 1s:** `[1, 1, 1]` → No changes needed.
        3. **All 2s:** `[2, 2, 2]` → No changes needed.
        4. **Mixed values:** `[2,0,2,1,1,0]` → Sorting is required.

        M - Match:
        - **Two-pointer approach (Dutch National Flag Algorithm)**:
          1. Use **three pointers**:
             - `left` (for placing `0s` at the beginning).
             - `right` (for placing `2s` at the end).
             - `m` (middle pointer to traverse the array).
          2. Swap values to their correct positions while keeping track of boundaries.

        P - Plan:
        1. **Initialize pointers**:
           - `left = 0` (boundary for `0s`).
           - `right = len(nums) - 1` (boundary for `2s`).
           - `m = 0` (iterator for traversal).
        2. **Iterate while `m <= right`**:
           - **If `nums[m] == 0`**:
             - Swap `nums[m]` and `nums[left]`.
             - Move both `left` and `m` forward.
           - **If `nums[m] == 1`**:
             - Just move `m` forward.
           - **If `nums[m] == 2`**:
             - Swap `nums[m]` and `nums[right]`.
             - Move `right` backward.
             - **Do not increment `m` immediately** to re-evaluate swapped value.
        3. **Stop when `m > right`**.

        I - Implement:
        '''
        left = 0
        right = len(nums) - 1
        m = 0

        while m <= right:
            if nums[m] == 0:
                nums[left], nums[m] = nums[m], nums[left]
                left += 1
                m += 1
            elif nums[m] == 2:
                nums[right], nums[m] = nums[m], nums[right]
                right -= 1
                # Do not increment `m`, as the swapped value needs reevaluation
            else:
                m += 1

    '''
    Alternative Approach: Counting Sort
    - Instead of swapping in-place, count the occurrences of `0s`, `1s`, and `2s`.
    - Then, overwrite `nums` based on the counts.

    P - Plan:
    1. **Count occurrences** of `0s`, `1s`, and `2s` in `nums`.
    2. **Overwrite `nums`** with `0s`, `1s`, and `2s` based on the counts.

    I - Implement:
    '''
    def sortColorsCountingSort(self, nums: List[int]) -> None:
        count_0 = count_1 = count_2 = 0

        # Count occurrences of each number
        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            else:
                count_2 += 1

        # Overwrite the list based on counts
        nums[:count_0] = [0] * count_0
        nums[count_0:count_0 + count_1] = [1] * count_1
        nums[count_0 + count_1:] = [2] * count_2

# Example Usage:
'''
E - Evaluate:
1. Input: nums = [2,0,2,1,1,0]
   Output: [0,0,1,1,2,2]

2. Input: nums = [2,0,1]
   Output: [0,1,2]

3. Input: nums = [0,0,0]
   Output: [0,0,0] (Already sorted)

4. Input: nums = [2,2,2]
   Output: [2,2,2] (Already sorted)

Time Complexity:
- **Dutch National Flag (Optimal Approach)**: **O(n)** (single pass).
- **Counting Sort**: **O(n)** (counting + overwriting).
  
Space Complexity:
- **Dutch National Flag**: **O(1)** (in-place swapping).
- **Counting Sort**: **O(1)** (modifies `nums` directly).
'''

'''
## U - Understand the Problem
### Problem Statement:
Given a **sorted** array `arr`, an integer `k`, and a target integer `x`, find the `k` closest elements to `x`. The result should also be sorted in ascending order.

### Clarifications:
1. Is the array **sorted**? **Yes**
2. Can `x` be outside the range of `arr`? **Yes**
3. If two numbers are equally close to `x`, which one should be chosen? **The smaller number**
4. Are duplicates possible? **Yes**
5. What happens if `k == len(arr)`? **Return the entire array**

---

## M - Match the Problem to Known Techniques
This problem is similar to:
- **Sliding Window Approach** → We narrow down to `k` closest elements using a window.
- **Two Pointers** → Used to compare distances from `x`.
- **Binary Search (Alternative approach)** → Find the closest element and expand around it.

---

## P - Plan
1. **Initialize two pointers:** `left = 0` and `right = len(arr) - 1`.
2. **Shrink the window to size `k`:**
   - If `abs(arr[left] - x) > abs(arr[right] - x)`, move `left` forward.
   - Otherwise, move `right` backward.
3. **Return the subarray `arr[left:right + 1]`** as the closest `k` elements.

---

## I - Implement the Solution
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while right - left >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1  
            else:
                right -= 1  
                
        return arr[left:right + 1]

# Alternative approach, binary search:
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left + k]





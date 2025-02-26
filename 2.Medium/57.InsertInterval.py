'''
## U - Understand the Problem
### Problem Statement:
You are given a list of **non-overlapping** intervals sorted in ascending order and a new interval. Your task is to insert the new interval into the list while maintaining the order and merging any overlapping intervals.

### Clarifications:
1. Are intervals already sorted? **Yes**
2. Can intervals be empty? **No, at least one interval exists**
3. What happens if the new interval overlaps multiple intervals? **Merge them**
4. What if the new interval does not overlap? **Simply insert it at the correct position**
5. Can newInterval be at the beginning or end? **Yes, we must handle all edge cases**

---

## M - Match the Problem to Known Techniques
This problem is similar to:
- **Merge Intervals**
- **Two Pointer Approach** (since the intervals are sorted)
- **Greedy Algorithm** (merging based on conditions)

---

## P - Plan
1. **Case 1:** If the current interval ends **before** the new interval starts, simply add it to the result.
2. **Case 2:** If the current interval **overlaps** with the new interval, update `newInterval` to merge them.
3. **Case 3:** If the remaining intervals are **completely after** the new interval, add them to the result without changes.

'''

## I - Implement the Solution
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        # Case 1: No overlapping before merging intervals
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Case 2: Overlapping and merging intervals
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Case 3: No overlapping after merging newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

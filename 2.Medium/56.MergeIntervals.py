class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals.
        - Return an array of the non-overlapping intervals that cover all the intervals in the input.

        Clarifications/Constraints:
        - The input intervals may not be sorted.
        - An interval is defined by a start and end, where start <= end.
        - The output intervals must be sorted by their start time.

        Examples:
        Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        Output: [[1, 6], [8, 10], [15, 18]]
        Explanation:
        - Intervals [1, 3] and [2, 6] overlap, so they are merged into [1, 6].

        Input: intervals = [[1, 4], [4, 5]]
        Output: [[1, 5]]
        Explanation:
        - Intervals [1, 4] and [4, 5] overlap, so they are merged into [1, 5].

        Potential clarifying questions for an interview:
        1. What should be returned if the input array is empty? (Return an empty array.)
        2. Can there be duplicate intervals? (Assume no duplicates.)
        3. Should the output array be sorted? (Yes, sorted by start time.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Sort intervals by their start time.
        # - Traverse the sorted intervals and merge them if they overlap:
        #   * Two intervals overlap if the start of the current interval <= the end of the previous interval.
        #   * Update the end of the previous interval to the maximum end of the two overlapping intervals.

        """
        P - Plan
        1. Sort the intervals by their start time.
        2. Initialize an empty list `arr` to store merged intervals.
        3. Traverse the sorted intervals:
           - If `arr` is empty or the start of the current interval is greater than the end of the last interval in `arr`:
             * Append the current interval to `arr`.
           - Otherwise:
             * Merge the intervals by updating the end of the last interval in `arr`.
        4. Return `arr` as the result.
        """

        arr = []  # To store merged intervals

        # Step 1: Sort intervals by their start time
        intervals.sort(key=lambda x: x[0], reverse=False)

        # Step 3: Traverse intervals and merge them
        for interval in intervals:
            if not arr or interval[0] > arr[-1][1]:
                # No overlap, append the interval
                arr.append(interval)
            else:
                # Overlap, merge intervals
                arr[-1][1] = max(arr[-1][1], interval[1])

        # Step 4: Return the merged intervals
        return arr

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]] -> Output: [[1, 6], [8, 10], [15, 18]]
2. Input: intervals = [[1, 4], [4, 5]] -> Output: [[1, 5]]
3. Input: intervals = [] -> Output: []

Edge Cases:
1. Empty intervals array -> Output: []
2. Single interval -> Output: Interval itself.
3. All intervals non-overlapping -> Output: Sorted intervals.

Time Complexity:
- O(n log n): Sorting the intervals dominates the time complexity.

Space Complexity:
- O(n): Result list `arr` may contain all intervals in the worst case.
"""

sol = Solution()
res = sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]])

if res == [[1, 6], [8, 10], [15, 18]]:
    print("Good Job")
else:
    print("Try Again...")

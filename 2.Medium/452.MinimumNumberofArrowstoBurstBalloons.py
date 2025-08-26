class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """

        U - Understand:
            We are given intervals [x_start, x_end] representing balloons.
            An arrow at position x bursts all balloons with x_start <= x <= x_end.
            Goal: minimum number of arrows to burst all balloons.

        M - Match:
            Problem type: Interval / Greedy.
            Similar to "merge intervals" or "non-overlapping intervals".

        P - Plan:
            1. Sort balloons by start coordinate.
            2. Initialize result with total balloons (worst case each balloon needs one arrow).
            3. Keep a 'prev' interval to track overlapping balloons.
            4. Iterate:
                - If current overlaps with prev → merge (reduce arrow count).
                - Else → need new arrow.
            5. Return result.

        I - Implement:
            See code below.

        R - Review:
            Example [[10,16],[2,8],[1,6],[7,12]] → output = 2 (correct).
            Edge cases: 
                - Single balloon → 1
                - Non-overlapping → len(points)

        E - Evaluate:
            Time: O(n log n) due to sorting.
            Space: O(1) extra.
            Clean greedy approach.
        """

        # Step 1: Sort balloons by starting coordinate
        points.sort()

        # Step 2: Initialize result (worst case: each balloon needs its own arrow)
        res = len(points)
        prev = points[0]

        # Step 3: Iterate over balloons
        for i in range(1, len(points)):
            curr = points[i]

            # Overlap case: can burst with one arrow
            if curr[0] <= prev[1]:
                res -= 1  # reduce arrow count
                prev = [curr[0], min(curr[1], prev[1])]  # update overlap interval
            else:
                prev = curr  # no overlap → need new arrow
        
        return res

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a list of points in a 2D plane and an integer `k`, find the `k` closest points to the origin (0, 0).
        - Distance is calculated using the Euclidean formula: sqrt(x^2 + y^2).

        Clarifications/Constraints:
        - The list of points will contain at least `k` points.
        - Points can have the same distance to the origin.
        - The result can be returned in any order.
        - The points array is non-empty.

        Examples:
        Input: points = [[1, 3], [-2, 2]], k = 1
        Output: [[-2, 2]]

        Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
        Output: [[3, 3], [-2, 4]]

        Potential clarifying questions for an interview:
        1. What should be returned if `k == 0`? (Return an empty list.)
        2. Can the input points contain duplicates? (Yes.)
        3. Should we use the Euclidean distance formula or its squared version? (Squared version avoids unnecessary square roots.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a min-heap to efficiently find the `k` smallest elements based on distance.
        # - Push tuples of (distance, point) into the heap and extract the top `k` points.

        """
        P - Plan
        1. Handle edge cases:
           - If the list of points is empty or `k == 0`, return an empty list.
        2. Initialize a min-heap.
        3. For each point in the list:
           - Calculate its distance from the origin using the squared distance formula (x^2 + y^2).
           - Push a tuple of (distance, point) into the heap.
        4. Extract `k` elements from the heap:
           - Pop the smallest elements one by one and add their corresponding points to the result list.
        5. Return the result list containing the `k` closest points.
        """

        if not points or k == 0:
            return []

        # Step 2: Initialize a min-heap
        heap = []
        res = []

        # Step 3: Calculate distance and push to the heap
        for point in points:
            distance = (point[0]) ** 2 + (point[1]) ** 2  # Use squared distance to avoid sqrt
            heapq.heappush(heap, (distance, point))  # Push (distance, point) into the heap

        # Step 4: Extract the `k` closest points
        while k > 0:
            closest = heapq.heappop(heap)  # Pop the point with the smallest distance
            res.append(closest[1])  # Append the point (not the distance) to the result
            k -= 1

        # Step 5: Return the result
        return res

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: points = [[1, 3], [-2, 2]], k = 1 -> Output: [[-2, 2]]
2. Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2 -> Output: [[3, 3], [-2, 4]]
3. Input: points = [], k = 0 -> Output: []

Edge Cases:
1. Empty list of points -> Output: [].
2. k = 0 -> Output: [].
3. Multiple points at the same distance -> Correctly include them in the result.

Time Complexity:
- O(n log n): Push `n` points into the heap (O(log n) per insertion) and extract `k` points (O(log n) per extraction).

Space Complexity:
- O(n): Space for the heap.
"""

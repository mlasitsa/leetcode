class Solution:
    # Direction vectors: right, left, down, up (matching grid values 1, 2, 3, 4)
    _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minCost(self, grid: List[List[int]]) -> int:
        '''
        U - Understand:
        - Problem: Given an `m x n` grid, each cell has a direction (1: right, 2: left, 3: down, 4: up).
          - Starting from the top-left cell `(0, 0)`, find the minimum cost to reach the bottom-right cell `(m-1, n-1)`.
          - Moving in the direction indicated by the cell incurs no cost; moving in any other direction adds a cost of 1.
        - Input:
          - `grid`: a 2D array where `grid[i][j]` is the direction of the cell.
        - Output:
          - Minimum cost to reach the bottom-right cell.
        - Constraints:
          - 1 <= m, n <= 100.
          - grid[i][j] is one of {1, 2, 3, 4}.

        M - Match:
        - This is a **shortest path problem** where the cost depends on the direction.
        - Use **Dijkstra's Algorithm** with a priority queue (min-heap) to calculate the minimum cost:
          1. Each cell is treated as a node.
          2. Moving in the intended direction has cost 0, while changing direction has cost 1.

        P - Plan:
        1. Initialize a priority queue (min-heap) with `(0, 0, 0)` representing (cost, row, col).
        2. Create a `min_cost` 2D array to store the minimum cost to reach each cell, initialized to infinity (`inf`).
        3. Perform Dijkstra's Algorithm:
           - Pop the cell with the smallest cost from the heap.
           - For each direction, calculate the cost to move to the neighboring cell.
           - If the new cost is less than the recorded cost for the neighboring cell, update `min_cost` and push the neighbor into the heap.
        4. Return the value in `min_cost[m-1][n-1]` as the minimum cost to reach the bottom-right cell.

        I - Implement:
        '''
        num_rows, num_cols = len(grid), len(grid[0])

        # Min-heap ordered by cost. Each element is (cost, row, col)
        pq = [(0, 0, 0)]  # Using list as heap, elements are tuples
        min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
        min_cost[0][0] = 0

        while pq:
            cost, row, col = heapq.heappop(pq)

            # Skip if we've found a better path to this cell
            if min_cost[row][col] != cost:
                continue

            # Try all four directions
            for d, (dx, dy) in enumerate(self._dirs):
                new_row, new_col = row + dx, col + dy

                # Check if new position is valid
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                    # Add cost=1 if we need to change direction
                    new_cost = cost + (d != (grid[row][col] - 1))

                    # Update if we found a better path
                    if min_cost[new_row][new_col] > new_cost:
                        min_cost[new_row][new_col] = new_cost
                        heapq.heappush(pq, (new_cost, new_row, new_col))

        return min_cost[num_rows - 1][num_cols - 1]

# Example Usage:
'''
E - Evaluate:
1. Input: grid = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
   Output: 0
   Explanation:
   - No direction changes are required to reach the bottom-right corner.

2. Input: grid = [[1, 2], [4, 3]]
   Output: 1
   Explanation:
   - Change the direction of the first cell to move left, then move down and right.

3. Input: grid = [[2, 2, 2], [2, 2, 2]]
   Output: 3
   Explanation:
   - Change directions at each step to move left and down.

Time Complexity:
- O(m * n * log(m * n)): The heap processes each cell once, and heap operations take logarithmic time.

Space Complexity:
- O(m * n): To store the `min_cost` array and heap.
'''

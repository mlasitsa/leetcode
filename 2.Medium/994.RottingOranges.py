from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        U - Understand:
        - Given a `grid` where:
          - `0` → **empty cell**.
          - `1` → **fresh orange**.
          - `2` → **rotten orange**.
        - Each minute, **fresh oranges adjacent (4-directionally) to rotten ones rot**.
        - Goal: Find **minimum time** required to rot all oranges.
        - If **some fresh oranges remain**, return `-1`.

        Example:
        - Input:
          ```
          grid = [[2,1,1],
                  [1,1,0],
                  [0,1,1]]
          ```
        - Output: `4`

        Edge Cases:
        - If `grid` contains **only fresh oranges and no rotten ones**, return `-1`.
        - If `grid` contains **no fresh oranges**, return `0`.
        - If `grid` is empty, return `0`.

        M - Match:
        - **Graph Traversal (BFS)**
          - Use **multi-source BFS** to process all initially **rotten oranges at once**.
          - Track fresh oranges (`fresh_count`).
          - Expand level-by-level (each level = 1 minute).

        P - Plan:
        1. **Initialize**:
           - Count `fresh_count` (fresh oranges).
           - Add all `rotten` oranges to a queue (`deque`).
        2. **BFS Processing**:
           - Process all rotten oranges at the current time step.
           - For each rotten orange, **spread the rot** to adjacent fresh oranges.
           - **Decrement `fresh_count`**.
           - **Increment time**.
        3. **Return**:
           - If all fresh oranges rotted, return `time`.
           - If `fresh_count > 0`, return `-1`.

        I - Implement:
        '''
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        time = 0

        # Step 1: Count fresh oranges and enqueue all rotten ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        # If no fresh oranges, return 0 immediately
        if fresh_count == 0:
            return 0

        # Step 2: BFS traversal to spread rot
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc

                    # If in bounds and is a fresh orange, rot it
                    if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
                        fresh_count -= 1  # Reduce fresh orange count

            time += 1  # Increase time after each BFS level

        # Step 3: Return time if all oranges rotted, otherwise -1
        return time if fresh_count == 0 else -1

    '''
    Alternative Approach: Using a `visited` set (Less optimal)
    - Instead of modifying the grid, we can use a `visited` set to track rotten oranges.
    - This approach requires **extra space** but avoids modifying input.

    P - Plan:
    1. Use a queue to store **initial rotten oranges**.
    2. Perform BFS, marking fresh oranges as rotten using `visited`.
    3. Stop when all fresh oranges are processed.

    I - Implement:
    '''
    def orangesRottingAlt(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        # Initialize queue with all rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

        return time if fresh == 0 else -1

# Example Usage:
'''
E - Evaluate:
1. Input:
   grid = [[2,1,1],
           [1,1,0],
           [0,1,1]]
   Output: 4
   Explanation:
   - Minute 1: [[2,2,1],[2,1,0],[0,1,1]]
   - Minute 2: [[2,2,2],[2,2,0],[0,1,1]]
   - Minute 3: [[2,2,2],[2,2,0],[0,2,1]]
   - Minute 4: [[2,2,2],[2,2,0],[0,2,2]] (All rotten).

2. Edge Case:
   grid = [[0,2]] (No fresh oranges)
   Output: 0

3. Edge Case:
   grid = [[1,0,2]]
   Output: -1 (Fresh orange cannot rot).

Time Complexity:
- **O(m * n)**: We process every cell once in BFS.
- **O(m * n) Space** for the queue (in worst case when all are fresh).
'''

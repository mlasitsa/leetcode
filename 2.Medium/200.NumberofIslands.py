class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        U - Understand:
        - Problem: Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
          - An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
          - You may assume that all four edges of the grid are surrounded by water.
        - Key Observations:
          1. A DFS or BFS traversal can mark all cells of an island as visited.
          2. Start DFS/BFS from every unvisited land cell ('1') and count it as a new island.

        Examples:
        - Input:
          grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
          ]
          Output: 1
        - Input:
          grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
          ]
          Output: 3

        M - Match:
        - **Graph traversal problem**:
          1. Treat each cell as a node in a graph.
          2. Use **DFS or BFS** to explore connected land cells and mark them visited.
        - **Flood-fill algorithm**:
          - Change visited land ('1') to water ('0') to avoid revisiting.

        P - Plan:
        1. Initialize `numberOfIslands = 0`.
        2. Define a recursive DFS function:
           - If out of bounds or water ('0'), return.
           - Mark current cell as visited ('0').
           - Recursively call DFS on its four neighbors (up, down, left, right).
        3. Iterate through the grid:
           - When an unvisited land ('1') is found, call DFS and increase `numberOfIslands`.
        4. Return `numberOfIslands`.

        I - Implement:
        '''
        def dfs(row, col):
            # Out of bounds or already visited (water)
            if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0"):
                return
            
            # Mark the current cell as visited
            grid[row][col] = "0"

            # Explore all four directions
            dfs(row + 1, col)  # Down
            dfs(row, col + 1)  # Right
            dfs(row - 1, col)  # Up
            dfs(row, col - 1)  # Left

        numberOfIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)  # Start DFS for the new island
                    numberOfIslands += 1  # Increment island count
        
        return numberOfIslands


    '''
    Alternative Solution: BFS
    - Instead of DFS, we use a queue (BFS) to traverse the grid.
    - BFS is more memory efficient in some cases.

    P - Plan:
    1. Initialize `numberOfIslands = 0`.
    2. Define a BFS function:
       - Use a queue to process all connected land cells.
       - Mark visited cells as '0' to avoid revisiting.
    3. Iterate through the grid:
       - If an unvisited land ('1') is found, call BFS and increment `numberOfIslands`.
    4. Return `numberOfIslands`.

    I - Implement:
    '''
    from collections import deque

    def numIslandsBFS(grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        numberOfIslands = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Down, Right, Up, Left

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"  # Mark visited

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == "1":
                        grid[new_x][new_y] = "0"  # Mark visited
                        queue.append((new_x, new_y))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)  # Start BFS for the new island
                    numberOfIslands += 1  # Increment island count

        return numberOfIslands

# Example Usage:
'''
E - Evaluate:
1. Input: grid = [
   ["1","1","0","0","0"],
   ["1","1","0","0","0"],
   ["0","0","1","0","0"],
   ["0","0","0","1","1"]
   ]
   Output: 3
   Explanation:
   - Three separate islands.

2. Input: grid = [["0","0","0"],["0","0","0"],["0","0","0"]]
   Output: 0
   Explanation:
   - No islands.

Time Complexity:
- O(m * n): Each cell is visited once.

Space Complexity:
- O(m * n) for DFS recursion stack (worst case) or BFS queue.
'''

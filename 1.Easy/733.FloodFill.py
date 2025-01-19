class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        U - Understand the Problem
        Problem Statement:
        - Perform a flood fill on a 2D grid `image`.
        - Start from pixel `(sr, sc)` and replace its connected component (same color) with `color`.
        - Connections are considered 4-directionally (up, down, left, right).

        Clarifications/Constraints:
        - The input grid is non-empty.
        - If the target pixel `(sr, sc)` already has the desired `color`, return the grid as-is.

        Examples:
        Input: image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color = 2
        Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

        Input: image = [[0, 0, 0], [0, 0, 0]], sr = 0, sc = 0, color = 0
        Output: [[0, 0, 0], [0, 0, 0]]

        Potential clarifying questions for an interview:
        1. Can the input grid be empty? (No, assume a valid grid is provided.)
        2. Should diagonally connected pixels be considered? (No, only 4-directional connections.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use BFS or DFS to traverse the connected component and modify cells directly in the grid.
        # - Avoid using extra space for visited nodes since we can modify the grid in-place.

        """
        P - Plan
        1. Handle the edge case where the grid is empty (return None).
        2. If the starting pixel `(sr, sc)` already has the desired color, return the grid as-is.
        3. Define a helper function `validateCell` to:
           - Check bounds and ensure the cell matches the starting color.
           - Add valid neighbors to the BFS queue.
        4. Use BFS to process all connected pixels.
        5. Return the modified grid.
        """

        # Step 1: Handle the edge case where the grid is empty
        if not image:
            return None

        # Step 2: Retrieve the starting pixel's color
        original_color = image[sr][sc]
        if original_color == color:  # No need to fill if the target color is already the same
            return image

        # Step 3: Initialize BFS queue
        dq = collections.deque()
        dq.append((sr, sc))

        # Step 4: Helper function for validation and adding neighbors
        def validateCell(row, col, dq, colorCheck):
            # Ensure the cell is within bounds and matches the starting color
            if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == colorCheck:
                dq.append((row, col))

        # Step 5: Perform BFS
        while dq:
            row, col = dq.popleft()

            # Change the color of the current cell
            image[row][col] = color

            # Check neighbors using the helper function
            validateCell(row + 1, col, dq, original_color)  # Down
            validateCell(row, col + 1, dq, original_color)  # Right
            validateCell(row - 1, col, dq, original_color)  # Up
            validateCell(row, col - 1, dq, original_color)  # Left

        # Step 6: Return the modified grid
        return image

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color = 2
   Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

2. Input: image = [[0, 0, 0], [0, 0, 0]], sr = 0, sc = 0, color = 0
   Output: [[0, 0, 0], [0, 0, 0]]

Edge Cases:
1. No connected component to update -> Output: Original grid.
2. Starting pixel already has the target color -> Output: Original grid.
3. Single-pixel grid -> Correctly update the pixel.

Time Complexity:
- O(m * n): Visit each cell at most once.

Space Complexity:
- O(m * n): Queue space in the worst case (if all cells are connected).
"""

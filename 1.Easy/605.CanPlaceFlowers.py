class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a flowerbed array (1 = flower, 0 = empty) and an integer `n` (number of flowers to plant), 
          determine if `n` flowers can be planted such that no two flowers are adjacent.

        Clarifications/Constraints:
        - You can plant a flower only if both adjacent spots are empty or out of bounds.
        - `n = 0` should always return True since no flowers need planting.
        - An empty array (`flowerbed = []`) should return False.

        Potential clarifying questions to ask in an interview:
        1. Are we guaranteed to only have 1s and 0s in the `flowerbed` array? (Assume yes.)
        2. Can the input be very large, and do we need an optimized solution? (Assume reasonable size.)
        3. Should the function modify the original array, or should we work with a copy? (Modify in place is fine.)
        4. How do we handle edge cases like:
           - A completely empty flowerbed?
           - `n` being larger than the number of empty spots?
           - All positions in `flowerbed` are already filled?

        Examples:
        Input: flowerbed = [1, 0, 0, 0, 1], n = 1 -> Output: True
        Input: flowerbed = [1, 0, 0, 0, 1], n = 2 -> Output: False
        Input: flowerbed = [0, 0, 0, 0, 0], n = 3 -> Output: True
        """

        # Handle edge cases:
        if len(flowerbed) == 0:
            return False  # Empty flowerbed can't accommodate any flowers
        if n == 0:
            return True  # No flowers to plant is always valid

        """
        M - Match with Patterns
        Observations:
        - This problem aligns with a greedy approach:
          - Traverse the array and plant a flower wherever possible.
          - Move the pointer efficiently to skip unnecessary checks.
        - Greedy algorithms work well here because we only care about whether planting `n` flowers is possible.

        Approach:
        - Use a single pointer to traverse the flowerbed.
        - For each position:
          1. If it's empty and its neighbors are also empty (or out of bounds), plant a flower.
          2. Skip positions that can't accommodate a flower.
          3. Stop early if `n` becomes 0 (all flowers are planted).
        """
        
        pointer = 0  # Start at the beginning of the flowerbed

        """
        P - Plan
        1. Iterate through the `flowerbed` array with a pointer.
        2. For each position:
           - If the current position is empty (`0`):
             * Check if the previous and next positions are also empty (or out of bounds).
             * If conditions are met, plant a flower (`1`) and decrement `n`.
             * Move the pointer by 2 to avoid adjacent planting.
           - If the current position is already occupied (`1`), move the pointer by 2.
        3. If `n` becomes 0 during the traversal, return True.
        4. If the loop ends and `n > 0`, return False.
        """

        # I - Implement
        while pointer < len(flowerbed):
            if flowerbed[pointer] == 0:  # Current position is empty
                # Check neighbors
                nextTo = pointer + 1
                prevTo = pointer - 1

                # Ensure adjacent spots are empty or out of bounds
                if (pointer == 0 or flowerbed[prevTo] == 0) and (nextTo == len(flowerbed) or flowerbed[nextTo] == 0):
                    # Plant a flower and decrement n
                    flowerbed[pointer] = 1
                    n -= 1
                    # Move pointer by 2 to skip adjacent positions
                    pointer += 2
                else:
                    # Move to the next position
                    pointer += 1
            else:
                # Current position is occupied; skip this and next position
                pointer += 2

            # Early exit if all flowers are planted
            if n == 0:
                return True

        # R - Review
        # If the loop ends and we still have flowers left to plant, return False
        return False

        """
        E - Evaluate
        Time Complexity:
        - O(n): We traverse the `flowerbed` array once, performing O(1) operations per position.

        Space Complexity:
        - O(1): We modify the `flowerbed` array in place and use a constant amount of extra space.

        Edge Cases:
        1. flowerbed = [1, 1, 1], n = 0 -> Output: True (No flowers to plant)
        2. flowerbed = [], n = 1 -> Output: False (Empty flowerbed can't accommodate flowers)
        3. flowerbed = [0, 0, 0, 0, 0], n = 3 -> Output: True (Can plant 3 flowers)

        Optimizations:
        - Early exit when `n` becomes 0 reduces unnecessary computations.
        """

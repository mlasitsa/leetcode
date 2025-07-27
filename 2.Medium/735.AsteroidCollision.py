from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        U - Understand the Problem
        Problem Statement:
        - You are given an array `asteroids`, where each element represents the size and direction of an asteroid.
          - Positive integers move to the right.
          - Negative integers move to the left.
        - If two asteroids collide:
          - The smaller one explodes.
          - If they are of the same size, both explode.
          - If they move in the same direction, no collision occurs.
        - Return the state of the asteroids after all collisions are resolved.

        Clarifications/Constraints:
        - Asteroids moving in opposite directions only collide if the left-moving one comes after a right-moving one.
        - Input sizes are reasonably small for simulation.
        - The solution must handle repeated collisions efficiently.

        Examples:
        Input: [5, 10, -5] -> Output: [5, 10]
        Input: [10, 2, -5] -> Output: [10]
        Input: [-2, -1, 1, 2] -> Output: [-2, -1, 1, 2]

        Potential clarifying questions for an interview:
        1. What should the function return if all asteroids explode? (Return an empty list.)
        2. Are there guarantees on the order of input? (Yes, input order must be preserved where no collisions occur.)
        3. Can the input contain zeroes? (No, assume only non-zero integers.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a stack to simulate the process:
        #   * Positive asteroids are pushed onto the stack (moving right).
        #   * Negative asteroids check for collisions with the top of the stack.
        #   * Handle collisions using absolute values and remove destroyed asteroids from the stack.

        """
        P - Plan
        1. Initialize an empty stack to keep track of surviving asteroids.
        2. Iterate through each asteroid in the list:
           - If the current asteroid moves left (negative) and the top of the stack moves right (positive):
             * Compare their absolute values to resolve the collision.
             * Remove the smaller asteroid(s) from the stack and continue checking.
           - If the top of the stack is larger, the current asteroid is destroyed.
           - If both asteroids are the same size, destroy both and stop the loop.
        3. If no collision occurs (or the stack is empty), append the current asteroid to the stack.
        4. Return the stack as the result.
        """

        stack = []  # Stack to store surviving asteroids
        
        for asteroid in asteroids:
            # Handle the case of collisions with a negative asteroid
            while stack and asteroid < 0 and stack[-1] > 0:
                # Compare the top of the stack with the current asteroid
                if abs(asteroid) > stack[-1]:  # Current asteroid is larger (it destroys the one on the stack)
                    stack.pop()  # Remove the top of the stack (destroyed)
                    continue  # Keep checking for further collisions
                elif abs(asteroid) == stack[-1]:  # Both asteroids are the same size
                    stack.pop()  # Destroy both asteroids
                    break  # No further collisions to handle
                else:  # The top of the stack asteroid is larger
                    break  # Current asteroid is destroyed, stop the loop
            else:
                # No collision or asteroid moves in the same direction
                stack.append(asteroid)
        
        return stack

# Example Usage
sol = Solution()

"""
E - Evaluate
Test the solution with examples:
1. Input: [5, 10, -5] -> Output: [5, 10]
2. Input: [10, 2, -5] -> Output: [10]
3. Input: [-2, -1, 1, 2] -> Output: [-2, -1, 1, 2]

Edge Cases:
1. Empty input -> Output: []
2. All asteroids move in the same direction -> Output: Original list
3. All asteroids explode -> Output: []

Time Complexity:
- O(n): Each asteroid is processed once (pushed/popped from the stack).

Space Complexity:
- O(n): Stack to store surviving asteroids.
"""

res = sol.asteroidCollision([5, 10, -5])
answer = [5, 10]

if res == answer:
    print("Good Job")
else: 
    print("Try Again...")

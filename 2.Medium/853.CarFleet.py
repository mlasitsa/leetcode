class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        U - Understand:
        - Problem: Given a target distance, an array `position` of starting positions, and an array `speed` of car speeds:
          - Each car moves towards the target.
          - A fleet is formed when two or more cars arrive at the target at the same time.
          - Cars in a fleet move together, maintaining the fleet's slowest speed.
          - Return the number of car fleets that will arrive at the target.
        - Key Observations:
          1. Sort the cars by their starting positions in descending order.
          2. Calculate the time it takes for each car to reach the target.
          3. Use a stack to track fleets:
             - If the current car catches up with the fleet ahead, they form a single fleet.

        Examples:
        - Input: target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
          Output: 3
          Explanation:
          - Cars at 10 and 8 form separate fleets.
          - Cars at 5 and 3 form a single fleet.
          - Car at 0 is a separate fleet.

        M - Match:
        - **Sorting Problem**:
          - Sort cars by their position in descending order.
        - **Greedy Algorithm**:
          - Use a stack to track the arrival times of fleets.
          - Merge cars into fleets based on their times.

        P - Plan:
        1. Create a list of pairs `pair` with `(position, speed)` for each car.
        2. Sort `pair` in descending order by position.
        3. Iterate over the sorted `pair` and calculate the time for each car to reach the target:
           - If the current car's time is greater than the top of the stack, it forms a new fleet.
           - Otherwise, it merges with the fleet at the top of the stack.
        4. Return the size of the stack as the number of fleets.

        I - Implement:
        '''
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

# Example Usage:
'''
E - Evaluate:
1. Input: target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
   Output: 3
   Explanation:
   - Car 10 takes 1 hour, car 8 takes 1 hour, and car 0 takes 12 hours.
   - Fleet 1: Cars at 5 and 3 (3 hours).
   - Fleet 2: Car at 8 (1 hour).
   - Fleet 3: Car at 10 (1 hour).

2. Input: target = 10, position = [3], speed = [3]
   Output: 1
   Explanation:
   - One car forms one fleet.

3. Input: target = 100, position = [0, 2, 4], speed = [4, 2, 1]
   Output: 1
   Explanation:
   - All cars merge into one fleet.

Time Complexity:
- O(n log n): Sorting the `position` array dominates the time complexity.
- O(n): Iterating through the sorted list to calculate times.

Space Complexity:
- O(n): Space used for the `pair` list and stack.
'''

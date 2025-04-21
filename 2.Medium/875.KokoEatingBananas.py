class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        U - Understand the Problem
        - Koko can eat bananas at an integer speed `k` (bananas per hour).
        - She has `h` hours to eat all the bananas in `piles`.
        - Each pile `p` takes ceil(p / k) hours to finish at speed `k`.
        - Find the minimum speed `k` such that Koko finishes all piles within `h` hours.

        Clarifications:
        - Can she eat part of a pile? No. She eats at most `k` bananas per hour per pile.
        - Is `h` always greater than or equal to the number of piles? Yes (based on constraints).
        - Edge case: If piles = [30], h = 5 → output should be ceil(30 / 5) = 6

        M - Match
        - This is a **search problem** over possible speeds (integers).
        - We're looking for the minimum valid speed → use **Binary Search**.
        - We cant sort the piles or use greedy directly — binary search on the answer fits best.

        P - Plan
        1. Define the range of possible speeds: [1, max(piles)]
        2. Use binary search to find the smallest k such that total hours <= h
        3. At each guess k, simulate the total hours required
        4. If within time, shrink right to find smaller valid k
        5. If not within time, increase left to try bigger k
        6. Track minimum valid k in a result variable
        """

        l, r = 1, max(piles)         # Search space: speed from 1 to max pile
        res = float('inf')          # Initialize result with infinity

        while l <= r:
            k = (l + r) // 2        # Guess the middle speed
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)  # Time to eat each pile at speed k
            
            if hours <= h:
                res = min(res, k)   # Try smaller speed if it still works
                r = k - 1
            else:
                l = k + 1           # Need more speed to finish in time

        return res

        """
        R - Review
        - The loop ensures binary search explores all valid speed values.
        - `math.ceil(p / k)` ensures partial piles take full hours.
        - `res` stores the best (lowest) valid eating speed.

        E - Evaluate
        Time Complexity:
        - O(n * log m) where n = number of piles, m = max(piles)
          → For each binary search guess, we compute total time in O(n)

        Space Complexity:
        - O(1): Only uses a few variables

        Edge Cases:
        - piles = [1], h = 1 → k = 1
        - piles = [3,6,7,11], h = 8 → k = 4
        - piles = [30,11,23,4,20], h = 6 → k = 23
        """

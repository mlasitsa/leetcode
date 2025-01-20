class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        '''
        U - Understand:
        - Problem: Given a `derived` array, determine if a valid original array exists.
          - Each element in the `derived` array is calculated as:
            `derived[i] = original[i] XOR original[(i + 1) % n]`
          - A valid `original` array exists if the XOR conditions can be satisfied.
        - Key Observation:
          1. The XOR operation's parity (odd/even) affects the sum of elements in `derived`.
          2. If the sum of `derived` is even, a valid `original` array exists.
        - Input: 
          - `derived`: List[int] where each value is either 0 or 1.
        - Output:
          - Return `True` if a valid original array exists, otherwise `False`.
        - Constraints:
          - `1 <= len(derived) <= 10^5`
          - All values in `derived` are either 0 or 1.

        M - Match:
        - Use a parity check:
          1. The XOR condition allows checking parity (even or odd).
          2. If the sum of `derived` is even, a valid `original` array exists.
          3. If the sum is odd, no valid `original` array can exist.

        P - Plan:
        1. Compute the sum of elements in `derived`.
        2. Check if the sum is even:
           - If even, return `True`.
           - If odd, return `False`.

        I - Implement:
        '''
        return sum(derived) % 2 == 0


    '''
    Alternative Solution:
    - Instead of calculating the entire sum, track parity directly while iterating through `derived`:
    P - Plan:
    1. Use a variable `parity` initialized to 0.
    2. Iterate through `derived`:
       - Toggle `parity` (0 <-> 1) for each `1` in `derived`.
    3. Return `True` if `parity == 0`, otherwise `False`.

    I - Implement:
    '''
    def doesValidArrayExistAlt(self, derived: List[int]) -> bool:
        parity = 0
        for num in derived:
            parity ^= num  # Toggle parity
        return parity == 0

# Example Usage:
'''
E - Evaluate:
1. Input: derived = [1, 0, 1]
   Output: True
   Explanation:
   - `derived` has an even sum (1 + 0 + 1 = 2).
   - A valid `original` array exists.

2. Input: derived = [1, 1, 1]
   Output: False
   Explanation:
   - `derived` has an odd sum (1 + 1 + 1 = 3).
   - No valid `original` array exists.

3. Input: derived = [0, 0, 0]
   Output: True
   Explanation:
   - `derived` has a sum of 0, which is even.
   - A valid `original` array exists.

Time Complexity:
- O(n): Iterate through the `derived` array once.

Space Complexity:
- O(1): Constant space used.
'''

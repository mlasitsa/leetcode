class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        '''
        U - Understand:
        - Problem: Given two integers `num1` and `num2`, minimize the XOR value of `num1` and a new number `x` such that:
          - The number of set bits (1s) in `x` is equal to the number of set bits in `num2`.
        - Key Points:
          1. XOR between two numbers is minimized when bits match as much as possible.
          2. Prioritize using the set bits of `num1` to build the result.
          3. If additional set bits are needed, fill from the least significant bit (LSB) upwards.

        Examples:
        - Input: num1 = 3, num2 = 5
          Output: 3
          Explanation:
          - Binary: num1 = 11, num2 = 101 (set bits = 2).
          - Result: 11 (XOR = 0).

        - Input: num1 = 28, num2 = 7
          Output: 27
          Explanation:
          - Binary: num1 = 11100, num2 = 111 (set bits = 3).
          - Result: 11011 (XOR minimized).

        M - Match:
        - Bit manipulation problem:
          1. Calculate the number of set bits in `num2`.
          2. Build `result` using the set bits of `num1` from the most significant bit (MSB) downward.
          3. If more bits are required, set bits from the least significant bit (LSB) upward.

        P - Plan:
        1. Calculate the number of set bits in `num2` using `bin(num2).count("1")`.
        2. Initialize `result` to 0 and start from the MSB of `num1`.
        3. Traverse bits of `num1`:
           - If the bit in `num1` is set, set it in `result` and decrement the remaining set bit count.
        4. If additional bits are needed, set them in `result` from the LSB upward.
        5. Return `result`.

        I - Implement:
        '''
        result = 0
        target_set_bits_count = bin(num2).count("1")
        set_bits_count = 0
        current_bit = 31  # Start from the most significant bit.

        # While result has fewer set bits than num2
        while set_bits_count < target_set_bits_count:
            # If the current bit of num1 is set or we must set all remaining bits in result
            if self._is_set(num1, current_bit) or (
                target_set_bits_count - set_bits_count > current_bit
            ):
                result = self._set_bit(result, current_bit)
                set_bits_count += 1
            current_bit -= 1  # Move to the next bit.

        return result

    # Helper function to check if the given bit position in x is set (1).
    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    # Helper function to set the given bit position in x to 1.
    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)

# Example Usage:
'''
E - Evaluate:
1. Input: num1 = 3, num2 = 5
   Output: 3
   Explanation:
   - Binary: num1 = 11, num2 = 101.
   - Result: 11 (matches the set bit count and minimizes XOR).

2. Input: num1 = 28, num2 = 7
   Output: 27
   Explanation:
   - Binary: num1 = 11100, num2 = 111.
   - Result: 11011 (matches set bits and minimizes XOR).

Time Complexity:
- O(32): Traverse 32 bits of `num1` (constant for integers).

Space Complexity:
- O(1): Constant space usage.
'''

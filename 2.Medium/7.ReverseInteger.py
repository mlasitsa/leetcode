class Solution:
    def reverse(self, x: int) -> int:
        '''
        U - Understand:
        - Given a 32-bit signed integer `x`, return its reversed digits.
        - If reversing causes overflow beyond `[-2^31, 2^31 - 1]`, return `0`.
        
        Example:
        - Input: `x = 123`
        - Output: `321`

        - Input: `x = -123`
        - Output: `-321`

        - Input: `x = 120`
        - Output: `21` (No leading zeros in result)

        - Input: `x = 1534236469`
        - Output: `0` (Overflow case)

        Edge Cases:
        1. If `x` is `0`, return `0`.
        2. If `x` is negative, preserve its sign.
        3. Handle overflow by ensuring the reversed number stays within `[-2^31, 2^31 - 1]`.

        M - Match:
        - **Mathematical manipulation** (Digit extraction & reconstruction).
        - **Checking overflow conditions** before performing operations.

        P - Plan:
        1. **Extract digits one by one from right to left** using modulus (`% 10`).
        2. **Build the reversed number** by multiplying the current result by `10` and adding the extracted digit.
        3. **Check for overflow** before updating the reversed number.
        4. **Return `0` if overflow occurs**, otherwise return the reversed integer.

        I - Implement:
        '''
        INT_MAX = 2**31 - 1  # Define the 32-bit signed integer range
        reversed_num = 0
        is_negative = x < 0  # Check if the number is negative
        x = abs(x)           # Work with the positive equivalent

        while x != 0:
            digit = x % 10         # Get the last digit
            x //= 10               # Remove the last digit

            # Check for overflow before adding the digit
            if (reversed_num > INT_MAX // 10) or (reversed_num == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0

            reversed_num = reversed_num * 10 + digit  # Build the reversed number

        return -reversed_num if is_negative else reversed_num

    '''
    Alternative Solution: Convert to String
    - Convert the integer to a string and reverse it.
    - Check for overflow before returning.

    P - Plan:
    1. Convert `x` to string and reverse it.
    2. Handle negative numbers by preserving the sign.
    3. Convert back to integer and check overflow.

    I - Implement:
    '''
    def reverseAlt(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        is_negative = x < 0
        reversed_str = str(abs(x))[::-1]
        reversed_num = int(reversed_str) * (-1 if is_negative else 1)

        return reversed_num if INT_MIN <= reversed_num <= INT_MAX else 0

# Example Usage:
'''
E - Evaluate:
1. Input: `123`
   Output: `321`

2. Input: `-123`
   Output: `-321`

3. Input: `120`
   Output: `21`

4. Overflow case:
   Input: `1534236469`
   Output: `0`

Time Complexity:
- **O(log x)**: We extract digits one by one (number of digits ~ log₁₀(x)).
- **O(1) space**, since we use only integer variables.

Alternative:
- Using string conversion takes **O(n)** time and **O(n)** space.
'''

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        '''
        U - Understand:
        - Given two numbers `n` and `x`, construct the **smallest** possible integer `y` such that:
          1. `y >= x`
          2. There exist exactly `n` distinct numbers in the sequence `{x, x+2, x+4, ...}` up to `y`.
        - The goal is to determine `y` based on the binary representation of `x` and `n-1`.
        
        Example:
        ```
        Input: n = 4, x = 2
        Output: 10

        Input: n = 5, x = 3
        Output: 19
        ```

        Constraints:
        - `1 ≤ n ≤ 10^9`
        - `1 ≤ x ≤ 10^18`

        Edge Cases:
        1. **n = 1** → `y = x` (as `x` itself satisfies the condition).
        2. **Power of Two `x`** → Behavior depends on bit manipulation of `n-1`.

        M - Match:
        - **Bit Manipulation** (Binary representation to control bit positions).
        - **Greedy approach** (Choose the smallest `y` that satisfies conditions).
        - **Mathematical Insights** (Using `x` as a base and modifying bits with `n-1`).

        P - Plan:
        1. **Convert `x` and `n-1` to binary arrays.**
        2. **Identify the first `0` bit in `x`** and use bits of `n-1` to update `x`.
        3. **Construct the final integer** by converting the modified binary array back to decimal.

        I - Implement:
        '''
        result = 0
        n -= 1  # Reduce n by 1 to get the offset count

        # Step 1: Initialize binary representations
        binaryX = [0] * 64  # Binary representation of x
        binaryN = [0] * 64  # Binary representation of n-1

        # Step 2: Convert `x` and `n-1` into binary arrays
        for i in range(64):
            binaryX[i] = (x >> i) & 1  # Extract i-th bit of x
            binaryN[i] = (n >> i) & 1  # Extract i-th bit of n-1

        posX = 0
        posN = 0

        # Step 3: Combine `x` and `n-1` to construct `y`
        while posX < 63:
            # Traverse `binaryX` until a 0-bit is found
            while posX < 63 and binaryX[posX] != 0:
                posX += 1
            # Insert `binaryN` bits into `binaryX`
            binaryX[posX] = binaryN[posN]
            posX += 1
            posN += 1

        # Step 4: Convert modified binary array to decimal
        for i in range(64):
            if binaryX[i] == 1:
                result += pow(2, i)

        return result

    '''
    Alternative Approach: Bitwise Construction without Arrays
    - Instead of storing binary arrays, use direct bitwise operations.

    P - Plan:
    1. **Initialize `y = x`**.
    2. **Use `n-1` to set free bits** in `x`.
    3. **Construct `y` in-place using bitwise shifts**.

    I - Implement:
    '''
    def minEndOptimized(self, n: int, x: int) -> int:
        n -= 1  # Reduce `n` for offset handling
        result = x
        bit = 1  # Start from least significant bit

        while n > 0:
            if result & bit == 0:  # If this bit in `x` is 0, modify it using `n`
                if n & 1:
                    result |= bit  # Set the bit in `result`
                n >>= 1  # Move to the next bit
            bit <<= 1  # Move to the next power of 2

        return result

# Example Usage:
'''
E - Evaluate:
1. Input: n = 4, x = 2
   Binary:
   x = 2 → `00000010`
   n-1 = 3 → `00000011`
   Modified result: `00001010`
   Output: `10`

2. Edge Case:
   - Input: n = 1, x = 3
   - Output: `3` (since `y = x` when `n=1`).

Time Complexity:
- **O(64) = O(1)** since there are at most 64 bits.
- **Space Complexity**:
  - **O(1)** for optimized approach (bitwise operations).
  - **O(64) = O(1)** for array-based approach.
'''

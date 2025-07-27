class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        '''
        U - Understand:
        - Problem: Determine if a string `s` with locked and unlocked characters can be rearranged to form a valid parentheses string.
        - Valid parentheses:
          1. "()" is valid.
          2. "AB" (A concatenated with B) is valid if both A and B are valid.
          3. "(A)" is valid if A is valid.
        - `locked[i] == '1'`: The character at index `i` cannot be changed.
        - `locked[i] == '0'`: The character at index `i` can be changed to '(' or ')'.
        - Constraints:
          - `len(s)` is even; otherwise, it's impossible to form valid parentheses.

        Example:
        Input: s = "))())(", locked = "010100"
        Output: True
        Explanation:
        - Unlock the second ')' and change it to '(' to form "(()())".

        M - Match:
        - Use a two-pass greedy approach:
          1. Left-to-right pass:
             - Track the balance of open and unlocked parentheses.
             - Ensure that at any point, the number of ')' does not exceed the available '(' + unlocked positions.
          2. Right-to-left pass:
             - Similar logic to ensure balance from the opposite direction.
          3. If both passes succeed, the string can be valid.

        P - Plan:
        1. Handle edge cases:
           - If `len(s) % 2 == 1`, return False (impossible to form valid parentheses).
        2. Perform a left-to-right pass:
           - Track `open_balance` for '(' and `unlock_balance` for unlocked characters.
           - Ensure that ')' never exceeds the available '(' + unlocked positions.
           - Return False if invalid.
        3. Perform a right-to-left pass:
           - Track `close_balance` for ')' and `unlock_balance` for unlocked characters.
           - Ensure that '(' never exceeds the available ')' + unlocked positions.
           - Return False if invalid.
        4. If both passes are valid, return True.

        I - Implement:
        '''
        if len(s) % 2 == 1:
            return False

        # Step 2: Left-to-right pass
        open_balance = 0 
        unlock_balance = 0  
        for i in range(len(s)):
            if locked[i] == '0':
                unlock_balance += 1  # This can be changed to '(' or ')'.
            elif s[i] == '(':
                open_balance += 1  # Increment for an open parenthesis.
            else:  # s[i] == ')'
                if open_balance > 0:
                    open_balance -= 1  # Use an open parenthesis to balance.
                elif unlock_balance > 0:
                    unlock_balance -= 1  # Use an unlocked position to balance.
                else:
                    return False  # Not enough resources to balance.

        # Step 3: Right-to-left pass
        close_balance = 0 
        unlock_balance = 0 
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                unlock_balance += 1  # This can be changed to '(' or ')'.
            elif s[i] == ')':
                close_balance += 1  # Increment for a closing parenthesis.
            else:  # s[i] == '('
                if close_balance > 0:
                    close_balance -= 1  # Use a closing parenthesis to balance.
                elif unlock_balance > 0:
                    unlock_balance -= 1  # Use an unlocked position to balance.
                else:
                    return False  # Not enough resources to balance.

        return True

# Example Usage:
'''
E - Evaluate:
1. Input: s = "))())(", locked = "010100"
   Output: True
   Explanation:
   - Change the second ')' to '(' to form "(()())".

2. Input: s = ")(", locked = "11"
   Output: False
   Explanation:
   - Locked characters cannot be rearranged.

3. Input: s = "())", locked = "000"
   Output: True
   Explanation:
   - All characters are unlocked, so it can be rearranged to "()".

Time Complexity:
- O(n): Single pass from left to right and right to left.

Space Complexity:
- O(1): No additional data structures used.
'''

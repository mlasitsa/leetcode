class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Evaluate a Reverse Polish Notation (RPN) expression.
        - The valid operators are '+', '-', '*', and '/'.
        - Division should truncate toward zero for integers.
        - Input is guaranteed to be a valid RPN expression.

        Clarifications/Constraints:
        - Operands are integers (positive, negative, or zero).
        - The input expression is non-empty.
        - The output fits within a 32-bit signed integer.

        Examples:
        Input: tokens = ["2", "1", "+", "3", "*"]
        Output: 9
        Explanation: (2 + 1) * 3 = 9

        Input: tokens = ["4", "13", "5", "/", "+"]
        Output: 6
        Explanation: 4 + (13 / 5) = 6 (division truncates toward zero).

        Input: tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        Output: 22
        Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22

        Potential clarifying questions for an interview:
        1. Are there invalid inputs? (No, the input is guaranteed to be valid.)
        2. Can the expression contain invalid operators? (No, only '+', '-', '*', '/'.)
        3. Should division be rounded or truncated? (Truncated toward zero.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a stack to evaluate the RPN expression:
        #   * Push operands onto the stack.
        #   * When encountering an operator, pop the last two operands, apply the operator, and push the result back onto the stack.

        """
        P - Plan
        1. Initialize an empty stack.
        2. Traverse the input tokens:
           - If the token is a number, push it onto the stack.
           - If the token is an operator:
             * Pop the top two numbers from the stack.
             * Apply the operation using the operator.
             * Push the result back onto the stack.
        3. After traversal, the stack should contain exactly one element, which is the result.
        4. Return the result.
        """

        # Step 1: Initialize an empty stack
        stack = []

        # Step 2: Define valid operators and their corresponding operations
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),  # Use int to truncate toward zero
        }

        # Step 3: Traverse the tokens
        for token in tokens:
            if token in operations:
                # It's an operator: pop two numbers, apply the operation
                b = stack.pop()
                a = stack.pop()
                result = operations[token](a, b)
                stack.append(result)  # Push the result back onto the stack
            else:
                # It's a number: push it onto the stack
                stack.append(int(token))

        # Step 4: The stack should contain exactly one element (the result)
        return stack.pop()

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: tokens = ["2", "1", "+", "3", "*"]
   Output: 9

2. Input: tokens = ["4", "13", "5", "/", "+"]
   Output: 6

3. Input: tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
   Output: 22

Edge Cases:
1. Single number -> Output: The number itself.
2. Expression with multiple operations -> Correctly evaluate in RPN order.

Time Complexity:
- O(n): Traverse the tokens once.

Space Complexity:
- O(n): Stack size in the worst case.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        U - Understand the Problem
        Problem Statement:
        - Given two non-empty linked lists representing two non-negative integers.
        - The digits are stored in reverse order, and each node contains a single digit.
        - Add the two numbers and return the result as a linked list.
        - Handle carry if the sum of two digits exceeds 9.

        Clarifications/Constraints:
        - Each input list represents a number in reverse order.
        - Neither number will have leading zeros except the number 0 itself.

        Examples:
        Input: l1 = [2, 4, 3], l2 = [5, 6, 4] -> Output: [7, 0, 8]
        Explanation: 342 + 465 = 807 (stored in reverse order).

        Input: l1 = [0], l2 = [0] -> Output: [0]
        Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9] -> Output: [8, 9, 9, 9, 0, 0, 0, 1]
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a dummy node to simplify the linked list construction.
        # - Traverse both linked lists simultaneously, adding their values along with any carry.
        # - Handle carry to ensure the sum is correct for digits exceeding 9.

        """
        P - Plan
        1. Create a dummy node to simplify the construction of the result linked list.
        2. Initialize a pointer (`curr`) to build the result and a variable (`carry`) to store overflow from additions.
        3. Traverse both linked lists while either list has nodes or there is a carry:
           - Add values from `l1` and `l2` (if they exist) and the carry.
           - Compute the new carry and the digit to store in the result.
           - Create a new node with the computed digit and link it to the result list.
           - Move to the next nodes in `l1` and `l2` (if they exist).
        4. Return the linked list starting from `dummyHead.next`.
        """

        # Step 1: Initialize the dummy node and the carry
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0

        # Step 3: Traverse both lists and handle carry
        while l1 is not None or l2 is not None or carry != 0:
            # Get values from l1 and l2 if they exist
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            # Compute the column sum and the carry
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            currentDigit = columnSum % 10

            # Create a new node for the current digit
            curr.next = ListNode(currentDigit)
            curr = curr.next

            # Move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Step 4: Return the result linked list
        return dummyHead.next

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: l1 = [2, 4, 3], l2 = [5, 6, 4] -> Output: [7, 0, 8]
2. Input: l1 = [0], l2 = [0] -> Output: [0]
3. Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9] -> Output: [8, 9, 9, 9, 0, 0, 0, 1]

Edge Cases:
1. Different lengths of `l1` and `l2` -> Correct sum.
2. Carry-over from one digit to the next -> Ensure no truncation.
3. Single-element linked lists -> Output correct sum.

Time Complexity:
- O(max(n, m)): Traverse the longer of the two linked lists.

Space Complexity:
- O(max(n, m)): Space for the resulting linked list.
"""

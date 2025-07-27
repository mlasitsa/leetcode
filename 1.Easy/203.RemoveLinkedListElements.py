# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given the head of a linked list and an integer `val`, remove all nodes of the linked list that have `val` as their value.
        - Return the new head of the modified linked list.

        Clarifications/Constraints:
        - The input list may be empty.
        - The function should remove all occurrences of `val` from the list.
        - If the list contains no nodes with value `val`, return the original list.

        Examples:
        Input: head = [1, 2, 6, 3, 4, 5, 6], val = 6 -> Output: [1, 2, 3, 4, 5]
        Input: head = [], val = 1 -> Output: []
        Input: head = [7, 7, 7, 7], val = 7 -> Output: []

        Potential clarifying questions for an interview:
        1. What should the function return if the input list is empty? (Return `None`.)
        2. Can `val` be present multiple times in the list? (Yes, remove all occurrences.)
        3. Is the input list guaranteed to be sorted? (No.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a dummy node to simplify the removal process, including cases where the head node needs to be removed.
        # - Traverse the list and check each node’s value against `val`.

        """
        P - Plan
        1. Create a dummy node pointing to the head of the list to handle edge cases where the head node needs removal.
        2. Use two pointers:
           - `dummy` to maintain the start of the list.
           - `cur` to traverse the original list.
        3. Traverse the list:
           - If the value of the current node is not equal to `val`, append it to the result list.
           - Move the pointers forward.
        4. Ensure the result list terminates correctly by setting the `next` pointer of the last node to `None`.
        5. Return the modified list starting from `dummy.next`.
        """

        # Step 1: Initialize a dummy node to handle edge cases
        temp = ListNode(0)  # Dummy node to simplify the process
        dummy = temp  # Save the dummy node reference
        cur = head  # Pointer to traverse the list

        # Step 3: Traverse the list and build the new list without `val`
        while cur is not None:
            if cur.val != val:  # If the current node’s value is not `val`
                temp.next = cur  # Append it to the result list
                temp = cur  # Move the `temp` pointer forward
            cur = cur.next  # Move to the next node in the original list

        # Step 4: Ensure the last node's `next` pointer is `None`
        temp.next = None

        # Step 5: Return the modified list starting from `dummy.next`
        return dummy.next

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: head = [1, 2, 6, 3, 4, 5, 6], val = 6 -> Output: [1, 2, 3, 4, 5]
2. Input: head = [], val = 1 -> Output: []
3. Input: head = [7, 7, 7, 7], val = 7 -> Output: []

Edge Cases:
1. Empty list -> Output: None.
2. All nodes have value `val` -> Output: None.
3. No nodes have value `val` -> Return the original list.

Time Complexity:
- O(n): Traverse the list once.

Space Complexity:
- O(1): In-place modification using pointers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        U - Understand the Problem
        Problem Statement:
        - Determine if a linked list has a cycle.
        - A cycle exists if a node’s `next` pointer points back to a previous node.

        Clarifications/Constraints:
        - The linked list may be empty.
        - If the list has only one node, it has a cycle if the node points to itself.

        Examples:
        Input: head = [3, 2, 0, -4], pos = 1 -> Output: True
        Explanation: The `next` pointer of the last node points to the second node, forming a cycle.

        Input: head = [1, 2], pos = 0 -> Output: True
        Input: head = [1], pos = -1 -> Output: False

        Potential clarifying questions for an interview:
        1. Can the list be empty? (Yes, return `False`.)
        2. What should the function return if the list contains one node pointing to itself? (Return `True`.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use Floyd's Tortoise and Hare algorithm:
        #   * Use two pointers, `slow` and `fast`.
        #   * `slow` moves one step at a time, while `fast` moves two steps.
        #   * If a cycle exists, `slow` and `fast` will meet.
        #   * If `fast` or `fast.next` becomes `None`, the list has no cycle.

        """
        P - Plan
        1. Handle the edge case: If the linked list is empty, return `False`.
        2. Initialize two pointers:
           - `slow` moves one step at a time.
           - `fast` moves two steps at a time.
        3. Traverse the linked list:
           - If `slow` and `fast` meet, a cycle exists (return `True`).
           - If `fast` or `fast.next` is `None`, the list has no cycle (return `False`).
        """

        # Step 1: Handle the edge case of an empty list
        if not head:
            return False

        # Step 2: Initialize slow and fast pointers
        slow = head
        fast = head

        # Step 3: Traverse the linked list
        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow one step
            fast = fast.next.next  # Move fast two steps

            if slow == fast:  # Cycle detected
                return True

        # Step 4: If fast reaches the end, there is no cycle
        return False

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: head = [3, 2, 0, -4], pos = 1 -> Output: True
2. Input: head = [1, 2], pos = 0 -> Output: True
3. Input: head = [1], pos = -1 -> Output: False

Edge Cases:
1. Empty list -> Output: False.
2. Single node pointing to itself -> Output: True.
3. Multiple nodes with no cycle -> Output: False.

Time Complexity:
- O(n): Traverse the linked list with two pointers.

Space Complexity:
- O(1): Only uses two pointers (constant space).
"""

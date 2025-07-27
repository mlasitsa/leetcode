# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        U - Understand the Problem
        Problem Statement:
        - Rearrange a linked list such that all nodes at odd indices come before nodes at even indices.
        - Maintain the relative order of the odd and even indexed nodes.
        - Return the reordered list.

        Clarifications/Constraints:
        - The input list can be empty.
        - Odd and even indices are based on 1-based indexing (1, 3, 5 are odd; 2, 4, 6 are even).
        - The function should reorder the list in-place.

        Examples:
        Input: head = [1, 2, 3, 4, 5] -> Output: [1, 3, 5, 2, 4]
        Input: head = [2, 1, 3, 5, 6, 4, 7] -> Output: [2, 3, 6, 7, 1, 5, 4]
        Input: head = [] -> Output: []

        Potential clarifying questions for an interview:
        1. Can the input list be empty? (Yes, return `None`.)
        2. Should the relative order of odd and even nodes be preserved? (Yes.)
        3. Can the list have only one node? (Yes, return the list itself.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use two pointers (`odd` and `even`) to traverse the list.
        # - Separate odd and even indexed nodes, maintaining their relative order.
        # - Reconnect the even list at the end of the odd list.

        """
        P - Plan
        1. Handle the edge case where the list is empty or contains a single node (return the list itself).
        2. Use two pointers:
           - `odd` points to the head of the list (odd indexed nodes).
           - `even` points to the second node (even indexed nodes).
        3. Traverse the list:
           - Link `odd` to `even.next` to skip the even node.
           - Move the `odd` pointer forward.
           - Link `even` to `odd.next` to skip the odd node.
           - Move the `even` pointer forward.
        4. After traversal, link the end of the odd list to the head of the even list.
        5. Return the head of the reordered list.
        """

        # Step 1: Handle the edge case where the list is empty
        if not head:
            return None

        # Step 2: Initialize pointers
        odd = head
        even = odd.next
        evenHead = even  # Save the head of the even list

        # Step 3: Traverse the list and rearrange nodes
        while even is not None and even.next is not None:
            odd.next = even.next  # Link odd to the next odd node
            odd = odd.next  # Move odd pointer forward
            even.next = odd.next  # Link even to the next even node
            even = even.next  # Move even pointer forward

        # Step 4: Connect the even list to the end of the odd list
        odd.next = evenHead

        # Step 5: Return the head of the reordered list
        return head

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: head = [1, 2, 3, 4, 5] -> Output: [1, 3, 5, 2, 4]
2. Input: head = [2, 1, 3, 5, 6, 4, 7] -> Output: [2, 3, 6, 7, 1, 5, 4]
3. Input: head = [] -> Output: []

Edge Cases:
1. Empty list -> Output: None.
2. Single node -> Output: The node itself.
3. Lists with alternating odd and even nodes -> Correctly rearrange.

Time Complexity:
- O(n): Traverse the list once.

Space Complexity:
- O(1): Reordering is done in-place using pointers.
"""

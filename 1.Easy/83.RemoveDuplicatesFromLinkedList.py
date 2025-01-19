# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a sorted linked list, remove all duplicates such that each element appears only once.
        - Return the modified linked list.

        Clarifications/Constraints:
        - The input list is sorted in non-decreasing order.
        - The function should modify the linked list in-place.
        - The function should return the head of the modified list.

        Examples:
        Input: head = [1, 1, 2] -> Output: [1, 2]
        Input: head = [1, 1, 2, 3, 3] -> Output: [1, 2, 3]
        Input: head = [] -> Output: []

        Potential clarifying questions for an interview:
        1. What should be returned if the input list is empty? (Return `None`.)
        2. Can there be multiple duplicates of the same value? (Yes, remove all duplicates.)
        3. Is the input list always sorted? (Yes.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Traverse the list using two pointers:
        #   * `prev` to keep track of the last unique node.
        #   * `cur` to traverse the list and identify duplicates.
        # - Skip duplicate nodes by updating `prev.next` to `cur.next`.

        """
        P - Plan
        1. Handle the edge case where the list is empty (return `None`).
        2. Use two pointers:
           - `prev` starts at the head of the list (last unique node).
           - `cur` starts at `head.next` (current node being checked for duplication).
        3. Traverse the list:
           - If `cur.val` is the same as `prev.val`, skip `cur` by updating `prev.next`.
           - Otherwise, move `prev` to `cur`.
           - Always move `cur` to the next node.
        4. Return the modified list starting at `head`.
        """

        # Step 1: Handle the edge case where the list is empty
        if head is None:
            return None

        # Step 2: Initialize pointers
        prev = head  # Points to the last unique node
        cur = head.next  # Traverses the list

        # Step 3: Traverse the list
        while cur is not None:
            if prev.val == cur.val:
                # Duplicate found, skip the current node
                prev.next = cur.next
            else:
                # Move `prev` to `cur` when a unique value is found
                prev = cur

            # Always move `cur` to the next node
            cur = cur.next

        # Step 4: Return the modified list
        return head

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: head = [1, 1, 2] -> Output: [1, 2]
2. Input: head = [1, 1, 2, 3, 3] -> Output: [1, 2, 3]
3. Input: head = [] -> Output: []

Edge Cases:
1. Empty list -> Output: None.
2. Single node -> Output: The node itself.
3. All nodes have the same value -> Output: A single node.

Time Complexity:
- O(n): Traverse the list once.

Space Complexity:
- O(1): In-place modification.
"""

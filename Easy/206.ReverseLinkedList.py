# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given the head of a singly linked list, reverse the list, and return the new head.

        Clarifications/Constraints:
        - The input is a singly linked list (each node has a `val` and `next` pointer).
        - If the list is empty, return `None`.
        - The function should modify the list in place without using additional memory.

        Examples:
        Input: [1 -> 2 -> 3 -> 4 -> 5] -> Output: [5 -> 4 -> 3 -> 2 -> 1]
        Input: [] -> Output: []
        Input: [1] -> Output: [1]

        Potential clarifying questions for an interview:
        1. Can the input list contain duplicate values? (Yes.)
        2. Should the function handle cyclic lists? (No, assume no cycles.)
        3. How large can the list be? (Assume it fits in memory.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - This is a classic linked list manipulation problem.
        # - Use iterative traversal with three pointers:
        #   * `prev` to track the previous node.
        #   * `cur` to track the current node.
        #   * `nextNode` to track the next node.

        """
        P - Plan
        1. Handle the edge case where the list is empty (head is None).
        2. Initialize three pointers:
           - `prev` as None (to mark the end of the reversed list).
           - `cur` as the head of the list (to traverse through the list).
           - `nextNode` as None (to temporarily store the next node).
        3. Traverse the list iteratively:
           - Store `cur.next` in `nextNode` to avoid losing the next node.
           - Reverse the link by pointing `cur.next` to `prev`.
           - Move `prev` to `cur` and `cur` to `nextNode`.
        4. When the traversal ends, `prev` will point to the new head of the reversed list.
        5. Return `prev`.
        """

        # Handle edge case: If the list is empty, return None
        if not head:
            return None

        # Initialize pointers
        prev = None  # Previous node starts as None
        cur = head   # Current node starts at head

        # I - Implement
        while cur is not None:
            nextNode = cur.next  # Temporarily store the next node
            cur.next = prev      # Reverse the current node's pointer
            prev = cur           # Move `prev` to the current node
            cur = nextNode       # Move to the next node in the list

        # `prev` now points to the new head of the reversed list
        return prev

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: [1 -> 2 -> 3 -> 4 -> 5] -> Output: [5 -> 4 -> 3 -> 2 -> 1]
2. Input: [] -> Output: []
3. Input: [1] -> Output: [1]

Edge Cases:
1. Empty list -> Output: None
2. Single node list -> Output: Node itself
3. List with multiple nodes -> Output: Reversed list

Time Complexity:
- O(n): Each node is visited once.

Space Complexity:
- O(1): No additional memory is used, as the list is reversed in place.
"""

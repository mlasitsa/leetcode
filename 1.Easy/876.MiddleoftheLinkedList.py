# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        U - Understand the Problem
        --------------------------
        Problem Statement:
        - Given the head of a singly linked list, return the middle node.
        - If there are two middle nodes, return the second one.

        Clarifications / Constraints:
        - The list will contain at least one node.
        - Return a reference to the node, not the value.
        - Cannot use array or list conversion (O(n) space not preferred).

        Examples:
        Input: [1, 2, 3, 4, 5]       -> Output: Node with value 3
        Input: [1, 2, 3, 4, 5, 6]    -> Output: Node with value 4
        """

        """
        M - Match
        --------------------------
        This matches a **Two Pointers (Slow & Fast)** pattern.
        - Use one pointer that moves twice as fast as the other.
        - When the fast pointer reaches the end, the slow pointer will be at the middle.

        Pattern Works Best For:
        - Finding midpoints
        - Cycle detection (Floyd's algorithm)
        - Linked list length parity problems
        """

        # I - Implement
        if not head:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

        """
        P - Plan
        --------------------------
        1. Initialize two pointers, `slow` and `fast`, both at head.
        2. Traverse list:
           - Move `slow` by 1 step
           - Move `fast` by 2 steps
        3. When `fast` or `fast.next` is null, return `slow` (middle node).
        """

        """
        R - Review
        --------------------------
        Efficient traversal with O(1) space
        Works for even and odd number of nodes
        Does not modify the input list
        Returns a node reference (not just the value)
        """

        """
        E - Evaluate
        --------------------------
        Time Complexity:
        - O(n), where n is the number of nodes in the list

        Space Complexity:
        - O(1), uses constant space for two pointers

        Edge Cases:
        - List with one node        -> return that node
        - List with two nodes       -> return second node
        - List with odd/even count  -> correctly returns middle
        """

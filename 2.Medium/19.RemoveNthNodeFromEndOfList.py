# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given the head of a linked list, remove the nth node from the end of the list and return its head.
        - Ensure the list remains connected after the removal.

        Clarifications/Constraints:
        - The input list may have 1 to 30 nodes.
        - `n` is always valid (1 <= n <= length of the list).
        - The function should modify the list in-place.

        Examples:
        Input: head = [1, 2, 3, 4, 5], n = 2 -> Output: [1, 2, 3, 5]
        Input: head = [1], n = 1 -> Output: []
        Input: head = [1, 2], n = 1 -> Output: [1]

        Potential clarifying questions for an interview:
        1. Can the list be empty? (No, `n` is always valid.)
        2. What should the function return if the input list has one node? (Return `None` if the only node is removed.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use two pointers to efficiently find the node to remove:
        #   * A `fast` pointer moves `n` steps ahead.
        #   * A `slow` pointer starts at the head and follows `fast` until `fast` reaches the end.
        #   * `slow` will then point to the node just before the node to be removed.

        """
        P - Plan
        1. Handle the edge case where the list has one node and we need to remove it (return `None`).
        2. Traverse the list to calculate its length.
        3. If the length equals `n`, remove the head node and return the new head.
        4. Use two pointers:
           - `slow` starts at the head.
           - `fast` starts `n` steps ahead of `slow`.
        5. Traverse the list with both pointers until `fast` reaches the end:
           - Update `slow.next` to skip the nth node from the end.
        6. Return the modified head of the list.
        """

        # Step 1: Handle edge case for a single-node list
        if not head:
            return None

        # If there's only one node, and we need to remove it
        if not head.next and n == 1:
            return None

        # Step 2: Calculate the length of the linked list
        lenLL = 1
        cur = head
        while cur.next is not None:
            lenLL += 1
            cur = cur.next

        # Step 3: Handle edge case where we need to remove the head node
        if lenLL == n:
            return head.next

        # Step 4: Initialize slow and fast pointers
        slow = head
        fast = head.next
        count = 1  # Start count at 1 because `slow` starts at the first node

        # Step 5: Traverse the list with the pointers
        while fast is not None:
            if count == lenLL - n:  # Stop just before the node to be removed
                slow.next = fast.next  # Remove the nth node
                break
            count += 1
            slow = slow.next
            fast = fast.next

        # Step 6: Return the modified head
        return head

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: head = [1, 2, 3, 4, 5], n = 2 -> Output: [1, 2, 3, 5]
2. Input: head = [1], n = 1 -> Output: []
3. Input: head = [1, 2], n = 1 -> Output: [1]

Edge Cases:
1. List with one node -> Remove the only node, return `None`.
2. Removing the head node -> Correctly return the new head.
3. General case -> Correctly remove the nth node.

Time Complexity:
- O(n): Traverse the list twice (once for length, once for removal).

Space Complexity:
- O(1): In-place modification using pointers.
"""

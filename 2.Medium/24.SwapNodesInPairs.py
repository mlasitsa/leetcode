# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given the head of a linked list, swap every two adjacent nodes and return the modified list.
        - The list should be modified in-place, and you cannot just swap values.

        Clarifications/Constraints:
        - The input list may have an odd or even number of nodes.
        - If the list has an odd number of nodes, the last node remains unchanged.
        - The function should return the head of the modified list.

        Examples:
        Input: head = [1, 2, 3, 4] -> Output: [2, 1, 4, 3]
        Input: head = [] -> Output: []
        Input: head = [1] -> Output: [1]

        Potential clarifying questions for an interview:
        1. What should be returned if the list is empty? (Return `None`.)
        2. Should we handle both odd and even-length lists? (Yes.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use two pointers (`slow` and `fast`) to represent the pair of nodes to swap.
        # - Use a dummy node to simplify edge cases (e.g., swapping the first pair).

        """
        P - Plan
        1. Handle the edge case where the list has less than two nodes (return the original head).
        2. Create a dummy node to simplify the swapping process.
        3. Initialize pointers:
           - `slow` points to the first node in the current pair.
           - `fast` points to the second node in the current pair.
           - `prev` points to the node just before the current pair (starts at the dummy node).
        4. Traverse the list:
           - Swap the `slow` and `fast` nodes.
           - Update `prev.next` to point to the new first node in the pair.
           - Move `prev` to the end of the current swapped pair.
           - Move `slow` and `fast` pointers to the next pair.
        5. Return the modified list starting at `dummy.next`.
        """

        # Step 1: Handle the edge case for lists with less than two nodes
        if not head or not head.next:
            return head

        # Step 2: Create a dummy node
        dummy = ListNode(0)

        # Step 3: Initialize pointers
        slow = head
        fast = head.next
        prev = dummy

        # Step 4: Traverse and swap pairs
        while slow and fast:
            # Swap the slow and fast nodes
            slow.next = fast.next
            fast.next = slow
            
            # Connect the previous node to the new first node in the pair
            prev.next = fast
            
            # Move the `prev` pointer to the end of the current swapped pair
            prev = slow
            
            # Move `slow` and `fast` to the next pair
            slow = slow.next
            if slow:
                fast = slow.next

        # Step 5: Return the new head, which is `dummy.next`
        return dummy.next

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: head = [1, 2, 3, 4] -> Output: [2, 1, 4, 3]
2. Input: head = [] -> Output: []
3. Input: head = [1] -> Output: [1]

Edge Cases:
1. Empty list -> Output: None.
2. List with one node -> Output: The node itself.
3. List with an odd number of nodes -> Last node remains unchanged.

Time Complexity:
- O(n): Traverse the list once to swap nodes.

Space Complexity:
- O(1): Swapping is done in-place using pointers.
"""

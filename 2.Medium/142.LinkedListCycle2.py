# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a linked list, return the node where the cycle begins.
        - If there is no cycle, return `None`.

        Clarifications/Constraints:
        - Assume there are no duplicate nodes.
        - The input linked list may or may not contain a cycle.
        - If there is a cycle, the function should identify the first node of the cycle.

        Examples:
        Input: head = [3, 2, 0, -4], pos = 1 -> Output: Node with value 2
        Input: head = [1, 2], pos = 0 -> Output: Node with value 1
        Input: head = [1], pos = -1 -> Output: None

        Potential clarifying questions for an interview:
        1. Can the input list be empty? (Yes, return `None`.)
        2. Should the function handle both cyclic and non-cyclic cases? (Yes.)
        3. Can the cycle start at any position? (Yes.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use Floyd's Tortoise and Hare algorithm to detect the cycle.
        # - If a cycle is detected, use a pointer (`start`) to find the cycle's starting node.

        """
        P - Plan
        1. Use two pointers, `slow` and `fast`, initialized to the head of the list:
           - `slow` moves one step at a time.
           - `fast` moves two steps at a time.
        2. Traverse the list:
           - If `slow` and `fast` meet, a cycle exists.
           - If `fast` or `fast.next` becomes `None`, there is no cycle (return `None`).
        3. Once a cycle is detected:
           - Initialize a pointer `start` to the head of the list.
           - Move `start` and `slow` one step at a time until they meet.
           - The node where they meet is the start of the cycle.
        4. Return the node where the cycle begins or `None` if no cycle exists.
        """

        # Step 1: Initialize pointers
        slow = head
        fast = head
        start = head

        # Step 2: Detect cycle using Floyd's Tortoise and Hare algorithm
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # Cycle detected
            if slow == fast:
                # Step 3: Find the start of the cycle
                while start != slow:
                    start = start.next
                    slow = slow.next
                return slow  # The start of the cycle

        # Step 4: If no cycle is found
        return None

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: head = [3, 2, 0, -4], pos = 1 -> Output: Node with value 2
2. Input: head = [1, 2], pos = 0 -> Output: Node with value 1
3. Input: head = [1], pos = -1 -> Output: None

Edge Cases:
1. Empty list -> Output: None.
2. Single node pointing to itself -> Correctly return the node.
3. No cycle -> Output: None.

Time Complexity:
- O(n): Detect the cycle and find its starting node in linear time.

Space Complexity:
- O(1): Only uses pointers (constant space).
"""

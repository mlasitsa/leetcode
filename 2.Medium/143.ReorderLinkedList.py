# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        U - Understand the Problem
        Problem Statement:
        - Given the head of a singly linked list, reorder the list to achieve the pattern:
          L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
        - Do this in-place without altering node values.

        Clarifications/Constraints:
        - The list contains at least one node.
        - Reordering should be done in-place using the original structure.
        - The function modifies the list and does not return anything.

        Examples:
        Input: head = [1, 2, 3, 4] -> Output: [1, 4, 2, 3]
        Input: head = [1, 2, 3, 4, 5] -> Output: [1, 5, 2, 4, 3]

        Potential clarifying questions for an interview:
        1. Can the list be empty? (No, the list has at least one node.)
        2. Should we account for odd and even lengths? (Yes, both cases are handled.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use the two-pointer technique to split the list into two halves.
        # - Reverse the second half of the list.
        # - Merge the two halves alternately to achieve the required reordering.

        """
        P - Plan
        1. Use slow and fast pointers to find the middle of the list.
        2. Split the list into two halves at the middle:
           - First half starts from the head.
           - Second half starts from the middle node's `next`.
        3. Reverse the second half of the list.
        4. Merge the two halves:
           - Alternate between nodes from the first and reversed second half.
        5. Ensure the list is correctly reordered.
        """

        # Step 1: Find the middle of the list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split the list into two halves
        secondPortion = slow.next
        slow.next = None  # Break the connection to split the list

        # Step 3: Reverse the second half
        prev = None
        while secondPortion:
            temp = secondPortion.next
            secondPortion.next = prev
            prev = secondPortion
            secondPortion = temp
        second = prev  # The reversed second half

        # Step 4: Merge the two halves
        first = head
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        # The list is now reordered

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: head = [1, 2, 3, 4] -> Output: [1, 4, 2, 3]
2. Input: head = [1, 2, 3, 4, 5] -> Output: [1, 5, 2, 4, 3]

Edge Cases:
1. List with one node -> Output: The same node.
2. List with two nodes -> Output: The same list.
3. Odd vs. even-length lists -> Correctly reorder in both cases.

Time Complexity:
- O(n): Split, reverse, and merge the list in linear time.

Space Complexity:
- O(1): In-place reordering without additional data structures.
"""

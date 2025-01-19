# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given two sorted linked lists `list1` and `list2`, merge them into a single sorted linked list.
        - The result should maintain the sorted order.
        - The merged linked list should be constructed by splicing together nodes from the input lists.

        Clarifications/Constraints:
        - Either list can be empty.
        - The input lists are sorted in non-decreasing order.
        - The function should return the head of the merged linked list.

        Examples:
        Input: list1 = [1, 2, 4], list2 = [1, 3, 4] -> Output: [1, 1, 2, 3, 4, 4]
        Input: list1 = [], list2 = [] -> Output: []
        Input: list1 = [], list2 = [0] -> Output: [0]

        Potential clarifying questions for an interview:
        1. What should be returned if both lists are empty? (Return `None`.)
        2. Are the input lists guaranteed to be sorted? (Yes.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a dummy node to simplify the construction of the merged list.
        # - Compare nodes from both lists one by one and append the smaller node to the merged list.
        # - Use pointers to traverse and build the result list.

        """
        P - Plan
        1. Create a dummy node to act as the head of the merged linked list.
        2. Use a pointer `node` to traverse and build the merged list.
        3. Traverse both input lists:
           - Compare the current nodes of `list1` and `list2`.
           - Append the smaller node to the merged list and move its pointer forward.
        4. After traversal, append the remaining nodes from the non-empty list (if any).
        5. Return the merged list starting from `dummy.next`.
        """

        # Step 1: Initialize a dummy node and pointer for the merged list
        temp = ListNode()  # Dummy node
        node = temp  # Pointer to build the merged list

        # Step 2: Traverse both lists and merge them
        while list1 and list2:
            if list1.val > list2.val:
                node.next = list2  # Append the smaller node
                list2 = list2.next  # Move pointer in `list2`
            else:
                node.next = list1  # Append the smaller node
                list1 = list1.next  # Move pointer in `list1`
            node = node.next  # Move pointer in the merged list

        # Step 3: Append the remaining nodes (if any)
        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        # Step 4: Return the merged list (excluding the dummy node)
        return temp.next

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: list1 = [1, 2, 4], list2 = [1, 3, 4] -> Output: [1, 1, 2, 3, 4, 4]
2. Input: list1 = [], list2 = [] -> Output: []
3. Input: list1 = [], list2 = [0] -> Output: [0]

Edge Cases:
1. Both lists are empty -> Output: None.
2. One list is empty -> Output: The non-empty list.
3. Lists with all elements equal -> Correctly merge all nodes.

Time Complexity:
- O(n + m): Traverse both lists, where `n` and `m` are the lengths of `list1` and `list2`.

Space Complexity:
- O(1): The merged list is built in place using existing nodes.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        U - Understand the Problem
        Problem Statement:
        - Given two singly linked lists, find the node at which the two lists intersect.
        - If the two linked lists do not intersect, return `None`.

        Clarifications/Constraints:
        - Each linked list can potentially end at the same node, forming an intersection.
        - If there is no intersection, the linked lists terminate at different nodes.
        - The intersection is defined by reference, not by value.

        Examples:
        Input: headA = [4,1,8,4,5], headB = [5,6,1,8,4,5]
        Output: Reference to node with value 8.

        Input: headA = [2,6,4], headB = [1,5]
        Output: None.

        Potential clarifying questions for an interview:
        1. Can the two linked lists be empty? (Yes, return `None` if either is empty.)
        2. Are there any guarantees on the lengths of the two lists? (No, they can be different lengths.)
        3. Can the intersection node occur anywhere in the lists? (Yes.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use the lengths of the two lists to align their starting points.
        # - Traverse both lists together to find the first node where they intersect.

        """
        P - Plan
        1. Traverse both linked lists to calculate their lengths.
        2. Determine the difference in lengths.
        3. Align the starting points of both lists by advancing the pointer of the longer list by the length difference.
        4. Traverse both lists together and check for the first common node.
        5. Return the intersecting node, or `None` if no intersection exists.
        """

        # Step 1: Calculate lengths of both linked lists
        listA = headA
        listB = headB
        lenA = 0
        lenB = 0

        while listA is not None:
            lenA += 1
            listA = listA.next

        while listB is not None:
            lenB += 1
            listB = listB.next

        # Step 2: Align starting points of the lists
        listA = headA
        listB = headB
        diff = abs(lenA - lenB)

        if lenA > lenB:
            for _ in range(diff):
                listA = listA.next
        else:
            for _ in range(diff):
                listB = listB.next

        # Step 3: Traverse both lists to find the intersection
        while listA is not None and listB is not None:
            if listA == listB:  # Intersection found
                return listA
            listA = listA.next
            listB = listB.next

        # Step 4: If no intersection exists
        return None

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: headA = [4,1,8,4,5], headB = [5,6,1,8,4,5] -> Output: Node with value 8.
2. Input: headA = [2,6,4], headB = [1,5] -> Output: None.
3. Input: headA = [], headB = [] -> Output: None.

Edge Cases:
1. Both lists are empty -> Output: None.
2. Lists with no intersection -> Output: None.
3. Lists with intersection at the head node -> Correctly return the head node.

Time Complexity:
- O(n + m): Traverse both lists to compute lengths and find the intersection.

Space Complexity:
- O(1): No additional space is used.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
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

        listA = headA
        listB = headB

        diff = abs(lenA - lenB)

        if lenA > lenB:
            for _ in range(diff):
                listA = listA.next
        else:
            for _ in range(diff):
                listB = listB.next

        # Traverse both lists together until we find the intersection
        while listA is not None and listB is not None:
            if listA == listB:
                return listA  # Intersection found
            listA = listA.next
            listB = listB.next

        return None  # No intersection
            
        
        
        
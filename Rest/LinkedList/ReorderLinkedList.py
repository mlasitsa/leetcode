# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondPortion = slow.next
        # Need to set element from middle next as none
        slow.next = None
        prev = None

        while secondPortion:
            temp = secondPortion.next
            secondPortion.next = prev
            prev = secondPortion
            secondPortion = temp
        
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

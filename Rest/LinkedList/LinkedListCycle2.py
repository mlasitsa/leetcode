# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        Here I would assume that linkedlist doesnt have duplicates
        '''

        start = head

        slow = head
        fast = head
        count = 0

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next


            if slow == fast:
                while start != slow:
                    start = start.next
                    slow = slow.next
                return slow

        return None
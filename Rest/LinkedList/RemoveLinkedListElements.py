# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0)
        dummy = temp
        cur = head

        while cur is not None: 
            if cur.val != val:
                temp.next = cur
                temp = cur

            cur = cur.next
        temp.next = None
        return dummy.next


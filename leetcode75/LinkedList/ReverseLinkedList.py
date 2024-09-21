# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        '''

        [1 -> 2 -> 3 -> 4 -> 5]
        0 <- 1 <- 2 <- 3 <-4 <- 5
        '''

        if not head:
            return None

        prev = head
        cur = head.next
        prev.next = None

        while cur is not None:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
            
        return prev
            
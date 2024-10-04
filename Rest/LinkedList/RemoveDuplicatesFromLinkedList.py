# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        prev = head  # 'prev' will point to the last unique node
        cur = head.next  # 'cur' will traverse the list

        while cur is not None:
            # If prev and cur nodes have the same value, skip the cur node
            if prev.val == cur.val:
                prev.next = cur.next  # Remove the duplicate node
            else:
                prev = cur  # Move prev forward only when a unique node is found
            
            cur = cur.next  # Always move cur to the next node

        return head
        
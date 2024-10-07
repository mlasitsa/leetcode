# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None

        # If there's only one element and we are removing the only node
        if not head.next and n == 1:
            return None

        # Calculate the length of the linked list
        lenLL = 1
        cur = head
        while cur.next is not None:
            lenLL += 1
            cur = cur.next

        # Edge case: If we're removing the first node
        if lenLL == n:
            return head.next

        # Initialize slow and fast pointers
        slow = head
        fast = head.next
        count = 1  # Start count at 1 because `slow` is at the first node

        # Traverse until `count` reaches `lenLL - n`
        while fast is not None:
            if count == lenLL - n:  # When `slow` is at the node just before the one to be removed
                slow.next = fast.next  # Skip the `nth` node from the end
                break
            count += 1
            slow = slow.next
            fast = fast.next

        return head
                




        
        
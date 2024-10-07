# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        # Create a dummy node but do not assign it to head immediately
        dummy = ListNode(0)
        
        # Use slow and fast pointers to traverse the list
        slow = head
        fast = head.next
        
        # `prev` will point to the dummy node initially
        prev = dummy

        while slow and fast:
            # Swap slow and fast nodes
            slow.next = fast.next
            fast.next = slow
            
            # Connect the previous node (or dummy) to the new first node in the pair
            prev.next = fast
            
            # Move the prev pointer to the end of the current swapped pair
            prev = slow
            
            # Move slow and fast pointers to the next pair
            slow = slow.next
            if slow:
                fast = slow.next

        # Return the new head, which is `dummy.next`
        return dummy.next

        
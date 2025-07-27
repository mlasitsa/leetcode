# EASY LEVEL TYPE O(N) time and O(N) Space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head:
            return None

        arr = []
        cur = head

        while cur is not None:
            arr.append(cur.val)
            cur = cur.next

        left = 0 
        right = len(arr) - 1

        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1 
        return True
            



# MEDIUM TYPE O(N) time and O(1) Space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Use fast and slow pointer to find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev
        
        second_half = reverse(slow)

        # Step 3: Compare first half and reversed second half
        first = head
        second = second_half
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True



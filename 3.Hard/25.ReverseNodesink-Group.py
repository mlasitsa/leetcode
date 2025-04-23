# U - Understand the Problem
# Problem:
# - Given a linked list, reverse nodes in k-group.
# - If remaining nodes < k, leave them as is.
# - Return the new head of the list.

# Clarifications:
# - k ≥ 1
# - List can have any number of nodes
# - You must reverse nodes **in-place** without altering node values.

# M - Match
# - Reversing linked list in chunks → Two-pointer technique
# - In-place reversal with a dummy head to manage edge cases
# - Works similarly to reversing sublists (a common linked list pattern)

# P - Plan
# 1. Count the total number of nodes to determine how many full k-groups exist.
# 2. Use a dummy node to simplify edge connections.
# 3. For each group of k nodes:
#    - Reverse the sublist
#    - Connect the reversed group with the rest of the list
#    - Move the pointer forward to continue
# 4. If fewer than k nodes remain, stop.

# I - Implement

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def getListLength(node):
            # Helper to count total nodes in the list
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        length = getListLength(head)
        dummy = ListNode(0)
        dummy.next = head
        prevTail = dummy
        cur = head

        while length >= k:
            prev = None
            temp = cur  # Store start of current k-group (will become tail after reversal)

            # Reverse k nodes
            for _ in range(k):
                nextNode = cur.next
                cur.next = prev
                prev = cur
                cur = nextNode

            # Connect previous group to reversed part
            prevTail.next = prev
            temp.next = cur  # temp is now the tail of the reversed group
            prevTail = temp
            length -= k

        return dummy.next

# R - Review
# - temp is start of group → becomes the new tail
# - prev becomes the new head of the reversed sublist
# - cur always points to the start of the next group
# - prevTail keeps track of where the last group ended

# E - Evaluate
# Time Complexity: O(n)
# - We traverse each node once to reverse, so it's linear

# Space Complexity: O(1)
# - In-place reversal, no extra data structures

# Edge Cases:
# - k = 1 → no change
# - k > length of list → list remains the same
# - List is empty → return None


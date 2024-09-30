# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
         # Initialize a dummy node that will act as a placeholder for the result linked list.
        # The result will be built starting from dummyHead.next.
        dummyHead = ListNode(0)

        # Set `curr` as a pointer that will traverse and build the result linked list.
        curr = dummyHead

        # Initialize `carry` to store any overflow (carry) from adding digits that result in sums >= 10.
        carry = 0
        
        # The loop runs as long as there are still digits to process in `l1`, `l2`, or if there is a remaining carry.
        while l1 is not None or l2 is not None or carry != 0:
            
            # If `l1` is not None, retrieve its value. Otherwise, use 0.
            if l1 is not None:
                l1Val = l1.val
            else:
                l1Val = 0

            # If `l2` is not None, retrieve its value. Otherwise, use 0.
            if l2 is not None:
                l2Val = l2.val
            else:
                l2Val = 0

            # Calculate the sum of the two values from `l1`, `l2`, and the current carry.
            columnSum = l1Val + l2Val + carry

            # Determine the new carry value by dividing the sum by 10.
            # This gives the tens digit (i.e., if the sum is 15, the carry will be 1).
            carry = columnSum // 10

            # The current digit to store in the result linked list is the ones digit of the sum.
            # Use modulo to get the remainder when dividing the sum by 10 (i.e., if the sum is 15, this will be 5).
            currentDigit = columnSum % 10

            # Create a new node with the current digit and link it to the result linked list.
            newNode = ListNode(currentDigit)
            curr.next = newNode

            # Move the `curr` pointer to the newly created node, so the next node can be linked after it.
            curr = newNode

            # Move to the next node in `l1` if it exists, otherwise, it remains `None`.
            if l1 is not None:
                l1 = l1.next
            else:
                l1 = None

            # Move to the next node in `l2` if it exists, otherwise, it remains `None`.
            if l2 is not None:
                l2 = l2.next
            else:
                l2 = None
        
        # Return the result linked list, which starts after the dummy node (`dummyHead.next`).
        return dummyHead.next
        
        
            
        

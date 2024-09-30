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
        
        '''
        If you don want to do math with carry, 
        this is a solution for you 
        
        '''
        first = ""
        second = ""
        ans = []
        
        firstList = l1 
        secondList = l2
        
        while firstList: 
            first += str(firstList.val)
            firstList = firstList.next
            
        while secondList:
            second += str(secondList.val)
            secondList = secondList.next
            
        num1 = int(first[::-1])  # Reverse the string since the list is in reverse order
        num2 = int(second[::-1])

        # Sum the two numbers
        total = num1 + num2

        # Convert the sum back into a string and reverse it (to match the linked list reverse order)
        total_str = str(total)[::-1]

        # Create the resulting linked list
        temp = ListNode(0)  # Dummy node to start the linked list
        current = temp

        for digit in total_str:
            current.next = ListNode(int(digit))  # Create a new node for each digit
            current = current.next
        
        return temp.next  # Return the real head (dummy.next)
        
        
            
        
        
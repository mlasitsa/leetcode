# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        U - Understand the Problem
        Problem Statement:
        - Given two non-empty linked lists representing two non-negative integers.
        - The digits are stored in reverse order, and each node contains a single digit.
        - Add the two numbers and return the result as a linked list.

        Clarifications/Constraints:
        - Each input list represents a number in reverse order.
        - Neither number will have leading zeros except the number 0 itself.

        Examples:
        Input: l1 = [2, 4, 3], l2 = [5, 6, 4] -> Output: [7, 0, 8]
        Explanation: 342 + 465 = 807 (stored in reverse order).

        Input: l1 = [0], l2 = [0] -> Output: [0]
        Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9] -> Output: [8, 9, 9, 9, 0, 0, 0, 1]

        Potential clarifying questions for an interview:
        1. Can the numbers be of different lengths? (Yes.)
        2. Are the linked lists guaranteed to be non-empty? (Yes.)
        3. Should we handle carry-over for large numbers? (Yes, but this implementation avoids carry math.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use strings to concatenate digits from both linked lists.
        # - Convert strings to integers, sum them, and reverse the result to reconstruct the linked list.

        """
        P - Plan
        1. Initialize two empty strings (`first` and `second`) to store the digits of the linked lists.
        2. Traverse `l1` and `l2`, appending digits to their respective strings.
        3. Reverse the strings to form the actual numbers and convert them to integers.
        4. Compute the sum of the two integers.
        5. Reverse the resulting sum and convert it back to a linked list.
        6. Return the head of the new linked list.
        """

        first = ""  # String to store digits of the first number
        second = ""  # String to store digits of the second number

        # Step 2: Traverse the linked lists and collect digits
        firstList = l1
        secondList = l2

        while firstList:
            first += str(firstList.val)  # Append digit to `first`
            firstList = firstList.next

        while secondList:
            second += str(secondList.val)  # Append digit to `second`
            secondList = secondList.next

        # Step 3: Reverse the strings to form the actual numbers
        num1 = int(first[::-1])
        num2 = int(second[::-1])

        # Step 4: Sum the two integers
        total = num1 + num2

        # Step 5: Convert the sum back to a string and reverse it
        total_str = str(total)[::-1]

        # Step 6: Convert the reversed string to a linked list
        temp = ListNode(0)  # Dummy node
        current = temp

        for digit in total_str:
            current.next = ListNode(int(digit))  # Create a new node for each digit
            current = current.next

        # Step 7: Return the resulting linked list
        return temp.next  # Skip the dummy node and return the head of the list

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: l1 = [2, 4, 3], l2 = [5, 6, 4] -> Output: [7, 0, 8]
2. Input: l1 = [0], l2 = [0] -> Output: [0]
3. Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9] -> Output: [8, 9, 9, 9, 0, 0, 0, 1]

Edge Cases:
1. Different lengths of `l1` and `l2` -> Correct sum.
2. Carry-over from one digit to the next -> Ensure no truncation.
3. Single-element linked lists -> Output correct sum.

Time Complexity:
- O(n + m): Traverse both linked lists (n and m are their lengths).

Space Complexity:
- O(n + m): Space used to store the resulting linked list and intermediate strings.
"""

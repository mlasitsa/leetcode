# U - Understand the Problem
"""
Problem:
You are given a list of k linked lists, each sorted in ascending order.
Merge all the linked lists into one sorted linked list and return its head.

Constraints:
- Each of the k lists may be empty or contain 1+ nodes.
- The total number of nodes across all lists can be up to 10^4.
- All values are integers.
- You need to return a *new merged list* without modifying original lists in place.

Examples:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Edge Cases:
- All input lists are empty: return None.
- Some lists are empty: ignore them.
"""

# M - Match with Patterns
"""
Pattern:
- This is a **K-way merge problem**, common when merging multiple sorted arrays/lists.
- The optimal data structure for this is a **min-heap** to always extract the smallest current node among the k lists.
- Use tuple (value, index, node) to avoid comparison errors in heap when values are the same.
"""

# P - Plan
"""
1. Initialize a min-heap.
2. Loop through the list of linked lists:
   - If the list is not empty, push (node.val, index, node) into the heap.
3. Initialize a dummy node to help construct the new list.
4. While the heap is not empty:
   - Pop the smallest node from the heap.
   - Append it to the result list.
   - If the popped node has a next node, push that next node into the heap.
5. Return dummy.next (head of the new list).
"""

# I - Implement (Your Code)
from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []

        for i, item in enumerate(lists):
            if item:
                heapq.heappush(heap, (item.val, i, item))
        
        dummy = ListNode(-1)
        cur = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        return dummy.next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        '''
        can do traversals for each, and then order should stay the same
        can I recrusively compare two at the same time?
        '''

        def compare(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            left = compare(node1.left, node2.left)
            right = compare(node1.right, node2.right)

            return left and right
        
        return compare(p, q)
            

        
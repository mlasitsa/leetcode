# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        def helper(node, val, depthToInsertAt, startDepth):

            if not node:
                return

            if startDepth == depthToInsertAt - 1:
                nodeLeft = node.left
                nodeRight = node.right

                node.left = TreeNode(val)
                node.right = TreeNode(val)
                
                node.left.left = nodeLeft
                node.right.right = nodeRight
            

            helper(node.left, val, depthToInsertAt,startDepth + 1)
            helper(node.right, val, depthToInsertAt,startDepth + 1)

        helper(root,val,depth,1)
        return root
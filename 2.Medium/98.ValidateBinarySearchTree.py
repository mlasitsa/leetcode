class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        U - Understand the Problem
        -------------------------------------
        Problem:
        - You are given the root of a binary tree.
        - Determine if it is a valid Binary Search Tree (BST).
        - Rules:
            - Left child < current node
            - Right child > current node
            - This must hold for every node in the tree.

        Examples:
        Input: [2,1,3] => Output: True
        Input: [5,1,4,null,null,3,6] => Output: False

        M - Match with Patterns
        -------------------------------------
        - Binary tree validation problem.
        - Requires recursion with value range checks.
        - Key: Each node must lie within a valid range.

        P - Plan
        -------------------------------------
        1. Use a recursive helper function that takes:
            - the current node
            - a minimum bound
            - a maximum bound
        2. For each node:
            - Check if node.val is strictly between min and max
            - Recursively check left subtree with updated max = node.val
            - Recursively check right subtree with updated min = node.val
        3. Base case: if node is None → valid by default

        I - Implement
        -------------------------------------
        """

        def helper(node, minVal, maxVal):
            if not node:
                return True  # Base case: null node is valid
            
            if not (minVal < node.val < maxVal):
                return False  # If current node violates BST property
            
            left = helper(node.left, minVal, node.val)
            right = helper(node.right, node.val, maxVal)

            return left and right

        return helper(root, float('-inf'), float('inf'))

        """
        R - Review
        -------------------------------------
        - Correctly handles BST logic using value ranges.
        - Efficient recursive structure.
        - Maintains correct bounds at each level.

        E - Evaluate
        -------------------------------------
        Time Complexity: O(n)
            - Visit each node exactly once.

        Space Complexity: O(h)
            - Call stack height is proportional to tree height.

        Edge Cases:
        - Empty tree → True
        - One node → True
        - Duplicate values → False (BST requires unique values on each side)
        - Left child == parent → False
        """

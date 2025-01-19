# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Given the root of a binary tree, return its maximum depth.
        - The maximum depth is the number of nodes along the longest path from the root down to the farthest leaf node.

        Clarifications/Constraints:
        - The tree can be empty (root is `None`).
        - If the tree has only one node, the depth is 1.

        Examples:
        Input: root = [3, 9, 20, null, null, 15, 7]
        Output: 3

        Input: root = [] -> Output: 0
        Input: root = [1] -> Output: 1

        Potential clarifying questions for an interview:
        1. Can the input tree be empty? (Yes, return 0.)
        2. Should the depth be calculated recursively or iteratively? (This implementation uses recursion.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use Depth-First Search (DFS) or recursion to calculate the depth of each subtree.
        # - At each node, the maximum depth is the maximum of the depths of its left and right subtrees, plus 1 for the current node.

        """
        P - Plan
        1. Handle the base case where the tree is empty (return 0).
        2. For each node:
           - Recursively calculate the maximum depth of the left subtree.
           - Recursively calculate the maximum depth of the right subtree.
           - Return the greater of the two depths plus 1 (to include the current node).
        """

        # Step 1: Handle the base case where the tree is empty
        if not root:
            return 0

        # Step 2: Recursively calculate the maximum depth of the left and right subtrees
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        """
        Alternative Implementation for Better Understanding:
        
        def helper(node):
            if not node:
                return 0

            left = helper(node.left)  # Depth of the left subtree
            right = helper(node.right)  # Depth of the right subtree

            # Return the maximum of the two depths plus 1 for the current node
            return max(left, right) + 1

        return helper(root)
        """

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: root = [3, 9, 20, null, null, 15, 7]
   Output: 3
2. Input: root = [] -> Output: 0
3. Input: root = [1] -> Output: 1

Edge Cases:
1. Empty tree -> Output: 0.
2. Single node tree -> Output: 1.
3. Deep unbalanced tree -> Correctly calculate maximum depth.

Time Complexity:
- O(n): Traverse each node in the tree once.

Space Complexity:
- O(h): Recursive call stack depth (where `h` is the height of the tree).
"""

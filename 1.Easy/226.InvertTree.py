# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given the root of a binary tree, invert the tree and return its root.
        - Inverting a tree means swapping the left and right children of all nodes in the tree.

        Clarifications/Constraints:
        - The tree may be empty (root is `None`).
        - The function should modify the tree in place and return the root of the inverted tree.

        Examples:
        Input: root = [4, 2, 7, 1, 3, 6, 9]
        Output: [4, 7, 2, 9, 6, 3, 1]

        Input: root = [] -> Output: []
        Input: root = [1] -> Output: [1]

        Potential clarifying questions for an interview:
        1. Can the input tree be empty? (Yes, return `None`.)
        2. Should the function handle only binary trees? (Yes.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use Depth-First Search (DFS) or recursion to traverse the tree.
        # - Swap the left and right children of each node.

        """
        P - Plan
        1. Handle the edge case where the tree is empty (return `None`).
        2. For the current node:
           - Swap its left and right children.
           - Recursively invert the left and right subtrees.
        3. Return the root of the inverted tree.
        """

        # Step 1: Handle the edge case where the tree is empty
        if not root:
            return None

        # Step 2: Swap the left and right children
        root.left, root.right = root.right, root.left

        # Step 3: Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Step 4: Return the root of the inverted tree
        return root

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: root = [4, 2, 7, 1, 3, 6, 9]
   Output: [4, 7, 2, 9, 6, 3, 1]
2. Input: root = [] -> Output: []
3. Input: root = [1] -> Output: [1]

Edge Cases:
1. Empty tree -> Output: None.
2. Single node tree -> Output: The same tree.
3. Balanced vs. unbalanced trees -> Correctly invert all nodes.

Time Complexity:
- O(n): Traverse each node in the tree once.

Space Complexity:
- O(h): Recursive call stack depth (where `h` is the height of the tree).
"""

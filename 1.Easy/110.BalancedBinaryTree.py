# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a binary tree, determine if it is height-balanced.
        - A binary tree is balanced if:
          - The left and right subtrees of every node differ in height by at most 1.

        Clarifications/Constraints:
        - The tree can be empty (root = None), which should return True.
        - Tree nodes contain integer values.
        - The number of nodes (n) is at most 5000.
        - The depth of the tree could be large, requiring an efficient approach.
        - What should be returned? Boolean (True/False).

        Examples:
        Input:
            1
           / \
          2   3
         / \   
        4   5 
        Output: True (Balanced)

        Input:
            1
           /
          2
         /
        3
        Output: False (Unbalanced)

        """

        """
        M - Match with Patterns
        Observations:
        - We need to check the height of the left and right subtrees.
        - If the difference is more than 1 at any node, the tree is unbalanced.
        - A **Depth-First Search (DFS) traversal** is suitable here.
        - **Post-order traversal** (left -> right -> root) ensures that we calculate the height from bottom-up.
        - Instead of recomputing height multiple times, **we return height while checking balance**.

        Approach:
        - Use a recursive function `checkHeight(node)`.
        - Base case: If node is None, return height 0.
        - Recursively find left and right subtree heights.
        - If any subtree is unbalanced (`-1`), propagate `-1` upwards.
        - If left and right height difference is more than 1, return `-1` (unbalanced).
        - Otherwise, return `max(left, right) + 1` to keep track of height.
        """

        """
        P - Plan
        1. Define a helper function `checkHeight(node)`:
            - If node is None, return 0.
            - Recursively compute left and right subtree heights.
            - If either is `-1`, return `-1` (tree is unbalanced).
            - If height difference > 1, return `-1` (unbalanced).
            - Otherwise, return `max(left, right) + 1`.
        2. Call `checkHeight(root)` and check if it returns `-1` (unbalanced).
        3. Return True if the tree is balanced, otherwise return False
        """

        # I - Implement
        def checkHeight(node):
            if not node:
                return 0  # Base case: height of a null node is 0
            
            left = checkHeight(node.left)  # Get height of left subtree
            right = checkHeight(node.right)  # Get height of right subtree
            
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1  # Propagate unbalanced condition

            return max(left, right) + 1  # Return height of the current node

        return checkHeight(root) != -1  # If -1 is returned, tree is unbalanced

        """
        R - Review
        - Ensures each node checks its left and right subtree before returning height.
        - Uses **post-order traversal** (left-right-root) to ensure correctness.
        - If any subtree is unbalanced, propagates `-1` immediately, avoiding extra computations.
        - Efficiently calculates height in a **single pass** instead of repeated height calculations.

        """

        """
        E - Evaluate
        Time Complexity:
        - O(n): Each node is visited once in a DFS manner.

        Space Complexity:
        - O(h): Where `h` is the height of the tree (O(log n) for balanced, O(n) for skewed trees).
        - Recursion depth equals tree height in the worst case.

        Edge Cases:
        1. Empty tree (root = None) → Output: True
        2. Single node (root with no children) → Output: True
        3. Fully balanced tree → Output: True
        4. Deep unbalanced tree → Output: False

        Optimizations:
        - The approach **avoids repeated height calculations** (compared to a naïve approach).
        - Uses a **single traversal** (O(n) time), preventing redundant height computations.
        """

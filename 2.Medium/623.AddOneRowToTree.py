# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        U - Understand the Problem
        Problem Statement:
        - Given the root of a binary tree, add a row of nodes with value `val` at the specified depth `depth`.
        - If `depth == 1`, a new root node with value `val` should be created, and the original tree should be its left subtree.

        Clarifications/Constraints:
        - The tree can have between 1 and 10^4 nodes.
        - The value `val` can be any integer.
        - `depth` is always a valid positive integer.

        Examples:
        Input: root = [4, 2, 6, 3, 1, 5], val = 1, depth = 2
        Output: [4, 1, 1, 2, null, null, 6, 3, 1, 5]

        Input: root = [4, 2, null, 3, 1], val = 1, depth = 3
        Output: [4, 2, null, 1, 1, 3, null, null, 1]

        Potential clarifying questions for an interview:
        1. What should happen if the tree is empty? (If `depth == 1`, return a new root with the given value.)
        2. Can `depth` be greater than the height of the tree? (No, assume `depth` is valid.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a recursive helper function to traverse the tree and insert nodes at the specified depth.
        # - Handle the case for `depth == 1` separately.

        """
        P - Plan
        1. Handle the edge case where `depth == 1`:
           - Create a new root node with value `val` and set the original tree as its left subtree.
           - Return the new root.
        2. Define a recursive helper function:
           - Traverse the tree until the depth just before the target depth.
           - Insert new nodes with value `val` as the left and right children of the current node.
           - Set the original left and right children as the children of the new nodes.
        3. Return the modified tree.
        """

        # Step 1: Handle the edge case for depth == 1
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        # Step 2: Define a helper function for recursion
        def helper(node, val, depthToInsertAt, startDepth):
            if not node:
                return

            # When the current depth is just before the target depth
            if startDepth == depthToInsertAt - 1:
                nodeLeft = node.left
                nodeRight = node.right

                # Insert new nodes with value `val`
                node.left = TreeNode(val)
                node.right = TreeNode(val)

                # Connect the original children to the new nodes
                node.left.left = nodeLeft
                node.right.right = nodeRight
                return

            # Recur for left and right subtrees
            helper(node.left, val, depthToInsertAt, startDepth + 1)
            helper(node.right, val, depthToInsertAt, startDepth + 1)

        # Step 3: Call the helper function starting at the root
        helper(root, val, depth, 1)
        return root

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: root = [4, 2, 6, 3, 1, 5], val = 1, depth = 2 -> Output: [4, 1, 1, 2, null, null, 6, 3, 1, 5]
2. Input: root = [4, 2, null, 3, 1], val = 1, depth = 3 -> Output: [4, 2, null, 1, 1, 3, null, null, 1]
3. Input: root = [], val = 1, depth = 1 -> Output: [1]

Edge Cases:
1. Empty tree -> Output: New root with value `val`.
2. Adding at depth greater than the tree height -> Valid insertion.
3. Adding a row to a single-node tree -> Correctly insert nodes as children.

Time Complexity:
- O(n): Traverse each node in the tree once.

Space Complexity:
- O(h): Recursive call stack depth (where `h` is the height of the tree).
"""

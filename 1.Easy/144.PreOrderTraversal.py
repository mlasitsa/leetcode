# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given the root of a binary tree, return its pre-order traversal.
        - In pre-order traversal, nodes are visited in the order:
          Root -> Left Subtree -> Right Subtree.

        Clarifications/Constraints:
        - The tree can be empty (root is `None`).
        - Return the traversal as a list of node values.

        Examples:
        Input: root = [1, null, 2, 3]
        Output: [1, 2, 3]

        Input: root = [] -> Output: []
        Input: root = [1] -> Output: [1]

        Potential clarifying questions for an interview:
        1. Should the function handle an empty tree? (Yes, return an empty list.)
        2. Should the traversal use recursion or iteration? (This implementation uses recursion.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use Depth-First Search (DFS) with a recursive approach for pre-order traversal.
        # - Maintain a list to store the traversal order.

        """
        P - Plan
        1. Define a helper function `preorder`:
           - If the current node is `None`, return immediately.
           - Add the value of the current node to the result list.
           - Recursively call `preorder` on the left subtree.
           - Recursively call `preorder` on the right subtree.
        2. Call the helper function starting at the root.
        3. Return the result list containing the traversal order.
        """

        # Step 1: Initialize an empty list to store the traversal
        arr = []

        # Step 2: Define the recursive helper function
        def preorder(node):
            nonlocal arr  # Access the outer list
            if not node:  # Base case: if the node is `None`
                return 

            arr.append(node.val)  # Visit the root node
            preorder(node.left)  # Traverse the left subtree
            preorder(node.right)  # Traverse the right subtree

            return arr

        # Step 3: Perform pre-order traversal starting from the root
        return preorder(root)

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: root = [1, null, 2, 3]
   Output: [1, 2, 3]
2. Input: root = [] -> Output: []
3. Input: root = [1] -> Output: [1]

Edge Cases:
1. Empty tree -> Output: [].
2. Single node tree -> Output: [node value].
3. Deep unbalanced tree -> Correctly traverse in pre-order.

Time Complexity:
- O(n): Visit each node once.

Space Complexity:
- O(h): Recursive call stack depth (where `h` is the height of the tree).
"""

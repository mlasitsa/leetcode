# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given the root of a perfect binary tree, reverse the values of nodes at each odd level (starting from level 1).
        - A perfect binary tree is one in which all internal nodes have two children, and all leaves are at the same level.

        Clarifications/Constraints:
        - The root will always be present.
        - The tree is perfect, so for any level `k`, the number of nodes at that level is `2^k`.
        - Only the values at the odd levels should be reversed; the tree structure should remain unchanged.

        Examples:
        Input:
                  2
                /   \
               3     5
              / \   / \
             8  13 21  34
        Output:
                  2
                /   \
               5     3
              / \   / \
             8  13 21  34

        Potential clarifying questions:
        1. Are we guaranteed a perfect binary tree? (Yes.)
        2. Can we modify the tree structure? (No, only values can be reversed.)
        3. Should we handle an empty tree? (No, the root will always be present.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use a Breadth-First Search (BFS) approach to traverse the tree level by level.
        # - Maintain a queue to access nodes in each level.
        # - At odd levels, collect the values of the nodes, reverse them, and reassign them back to the nodes.

        """
        P - Plan
        1. Handle the edge case: If the root is None, return None.
        2. Use a queue to perform BFS on the tree.
        3. Maintain a `level` variable to track the current level.
        4. For each level:
           - Collect the nodes at that level.
           - If the level is odd, reverse the values of the nodes.
           - Add the children of the current level's nodes to the queue for the next level.
        5. Return the modified root.
        """

        from collections import deque

        # Step 1: Handle edge case
        if not root:
            return None

        # Step 2: Initialize the queue and level tracker
        q = deque([root])
        level = 0  # Start at level 0 (even)

        # Step 3: Perform BFS
        while q:
            level_size = len(q)  # Number of nodes at the current level
            nodes = []  # To store the nodes at this level

            # Collect nodes for the current level
            for _ in range(level_size):
                node = q.popleft()
                nodes.append(node)

                # Enqueue children for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Step 4: Reverse values at odd levels
            if level % 2 == 1:  # Odd level
                i, j = 0, len(nodes) - 1
                while i < j:
                    nodes[i].val, nodes[j].val = nodes[j].val, nodes[i].val  # Swap values
                    i += 1
                    j -= 1

            # Step 5: Increment level
            level += 1

        # Step 6: Return the root
        return root

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input:
           1
         /   \
        2     3
       / \   / \
      4   5 6   7
   Output:
           1
         /   \
        3     2
       / \   / \
      4   5 6   7

2. Edge Case:
   Input: Single node tree -> Output: Same tree.

Time Complexity:
- O(n): Each node is visited once.

Space Complexity:
- O(w): Queue space at the widest level of the tree.
"""

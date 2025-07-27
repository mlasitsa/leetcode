class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        U - Understand the Problem
        -------------------------------------
        Problem:
        - Given a non-empty binary tree, find the path with the maximum sum.
        - A path is any sequence of nodes from some starting node to any node 
          in the tree along the parent-child connections.
        - The path must contain at least one node and does not need to go through the root.

        Clarifications:
        - Paths can start and end at any node.
        - Path must be connected and cannot revisit nodes.

        Examples:
        Input: root = [-10,9,20,null,null,15,7]
        Output: 42 (Path: 15 → 20 → 7)

        M - Match with Patterns
        -------------------------------------
        Pattern:
        - Tree traversal
        - DFS with backtracking
        - Postorder traversal to calculate subtrees

        P - Plan
        -------------------------------------
        1. Use DFS to traverse all nodes.
        2. At each node:
            a. Calculate left and right max path sums.
            b. Ignore negative paths (max with 0).
            c. Calculate the **split path** through the node: left + node + right.
            d. Update global max with split path if it's better.
        3. Return the **max single-branch path** up to parent (no splits allowed going up).

        I - Implement
        -------------------------------------
        """

        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0

            # Recurse on left/right subtree and discard negatives
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            # Local path includes split
            currentPathSum = node.val + leftMax + rightMax
            maxSum = max(maxSum, currentPathSum)

            # Return max single path going up
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return maxSum

        """
        R - Review
        -------------------------------------
        - Function returns max gain path from child to parent.
        - Global max keeps track of best split path at any node.
        - Discarding negative subtrees ensures we don’t reduce total path sum.

        E - Evaluate
        -------------------------------------
        Time Complexity: O(n)
            - Each node is visited once.

        Space Complexity: O(h)
            - h = height of the tree (O(log n) balanced, O(n) skewed).
        
        Edge Cases:
        - All negative nodes: return the largest (least negative) value.
        - One-node tree: return root.val.
        """

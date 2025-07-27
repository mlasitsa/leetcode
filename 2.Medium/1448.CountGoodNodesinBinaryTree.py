class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        U - Understand the Problem
        -------------------------------------
        Problem:
        - Given a binary tree, count the number of "good" nodes.
        - A node X is "good" if there are no nodes with a value greater than X 
          on the path from the root to X (inclusive).

        Constraints:
        - All node values are integers.
        - The root is always a good node.
        - Must traverse the whole tree.

        Examples:
        Input: [3,1,4,3,null,1,5] → Output: 4
        Explanation: Good nodes = 3, 3, 4, 5

        M - Match with Patterns
        -------------------------------------
        Pattern:
        - DFS traversal (Preorder or Postorder)
        - At each node, keep track of the max value seen on the path so far.

        P - Plan
        -------------------------------------
        1. Use DFS to traverse the binary tree.
        2. At each node:
            a. If node.val >= maxVal seen so far → it's a good node, increment count.
            b. Update maxVal to be max(maxVal, node.val)
        3. Recurse to left and right child.
        4. Return final count.

        I - Implement
        -------------------------------------
        """

        count = 0

        def helper(node, maxVal):
            nonlocal count
            if not node:
                return

            if node.val >= maxVal:
                count += 1
                maxVal = node.val  

            helper(node.left, maxVal)
            helper(node.right, maxVal)

        helper(root, root.val)
        return count

        """
        R - Review
        -------------------------------------
        - Good use of nonlocal to track state without returning values.
        - DFS traversal ensures every node is visited once.
        - maxVal is passed down to compare current path's max.

        E - Evaluate
        -------------------------------------
        Time Complexity: O(n)
            - Every node is visited once.
        Space Complexity: O(h)
            - h is the height of the tree (O(log n) for balanced, O(n) worst case).

        Edge Cases:
        - Tree with only one node → output = 1
        - All increasing or decreasing paths → output = total nodes (if increasing), 1 (if decreasing)
        """

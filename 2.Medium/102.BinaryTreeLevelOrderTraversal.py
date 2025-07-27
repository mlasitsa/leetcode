# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        U - Understand the Problem
        Problem Statement:
        - Given the root of a binary tree, return the level-order traversal of its nodes' values as a list of lists.
        - In level-order traversal, nodes are visited level by level from left to right.

        Clarifications/Constraints:
        - If the tree is empty, return an empty list.
        - Each level of the tree should be represented as a list in the output.

        Examples:
        Input: root = [3, 9, 20, null, null, 15, 7]
        Output: [[3], [9, 20], [15, 7]]

        Input: root = [] -> Output: []
        Input: root = [1] -> Output: [[1]]

        Potential clarifying questions for an interview:
        1. What should be returned if the tree is empty? (Return an empty list.)
        2. Should the traversal include null values for missing nodes? (No, only include actual node values.)
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Use Breadth-First Search (BFS) to traverse the tree level by level.
        # - Maintain a queue to store nodes at each level and iterate over them.

        """
        P - Plan
        1. Handle the edge case where the tree is empty (return an empty list).
        2. Initialize a queue with the root node.
        3. Traverse the tree level by level:
           - For each level:
             - Iterate over all nodes in the current level (use the length of the queue to determine the level size).
             - Append their values to the current level's result list.
             - Add their children (if any) to the queue for the next level.
           - Append the current level's result list to the final result.
        4. Return the final result.
        """

        # Step 1: Handle the edge case where the tree is empty
        if not root:
            return []

        # Step 2: Initialize the queue and final result
        q = deque()
        q.append(root)
        final = []  # To store the level-order traversal

        # Step 3: Perform BFS
        while q:
            res = []  # To store nodes' values for the current level
            for i in range(len(q)):  # Iterate over the current level's nodes
                node = q.popleft()  # Remove the node from the queue
                res.append(node.val)  # Add the node's value to the current level's result

                # Add the node's children to the queue for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Append the current level's result to the final result
            final.append(res)

        # Step 4: Return the final result
        return final

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: root = [3, 9, 20, null, null, 15, 7]
   Output: [[3], [9, 20], [15, 7]]
2. Input: root = [] -> Output: []
3. Input: root = [1] -> Output: [[1]]

Edge Cases:
1. Empty tree -> Output: [].
2. Single node tree -> Output: [[node value]].
3. Deep unbalanced tree -> Correctly process all levels.

Time Complexity:
- O(n): Visit each node exactly once.

Space Complexity:
- O(w): Maximum width of the tree (queue size at the widest level).
"""

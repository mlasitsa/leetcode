# U - Understand the Problem
"""
Problem:
You are given two arrays:
- preorder: The preorder traversal of a binary tree.
- inorder: The inorder traversal of the same binary tree.

Your task is to reconstruct the original binary tree and return its root.

Constraints / Assumptions:
- All node values are unique.
- Both arrays are of the same length and represent a valid binary tree.
- The tree contains no duplicate values.

Examples:
Input:
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

Output:
    Tree structured like:
          3
         / \
        9  20
           / \
          15  7
"""

# M - Match with Patterns
"""
Pattern:
- Recursive Tree Construction.
- Use preorder to get the root at each level.
- Use inorder to find left/right subtree boundaries.

Preorder: [Root | Left Subtree | Right Subtree]
Inorder: [Left Subtree | Root | Right Subtree]
=> Use a global index for preorder traversal.
=> Use a hashmap for fast lookup in inorder array.
"""

# P - Plan
"""
1. Use a hashmap to store the indices of elements in the inorder list for O(1) lookup.
2. Use a `preorder_index` pointer to keep track of the current root node in preorder.
3. Define a recursive `helper(left, right)` function:
   - If left > right, return None (no subtree to build).
   - Pick the value at `preorder[preorder_index]` as the root.
   - Increment `preorder_index`.
   - Use the hashmap to find the index of the root in the inorder array.
   - Recursively build:
     * Left subtree from `inorder[left:index-1]`
     * Right subtree from `inorder[index+1:right]`
4. Call helper(0, len(inorder) - 1) to construct the full tree.
"""

# I - Implement
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build hashmap of value -> index for inorder
        inorder_index_map = {}
        for i in range(len(inorder)):
            inorder_index_map[inorder[i]] = i

        preorder_index = 0  # Global index tracker

        def helper(left, right):
            nonlocal preorder_index
            if left > right:
                return None

            # Pick the current root from preorder
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)

            # Move the index forward for the next recursive call
            preorder_index += 1

            # Get the index of the root in inorder
            index = inorder_index_map[root_val]

            # Recursively build left and right subtree
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)

            return root

        return helper(0, len(inorder) - 1)

# R - Review
"""
- This implementation is clean and efficient.
- The use of a hashmap avoids repeated scanning of the inorder array.
- Recursive decomposition is optimal for tree problems.
- Uses `nonlocal` for tracking state across recursive calls.
"""

# E - Evaluate
"""
Time Complexity: O(n)
- Each node is processed exactly once.

Space Complexity: O(n)
- Hashmap stores n elements.
- Recursion stack may go up to O(n) in skewed trees.

This is an optimal and correct solution for FAANG-level interviews.
"""

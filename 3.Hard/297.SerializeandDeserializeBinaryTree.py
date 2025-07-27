# U - Understand the Problem
"""
Problem:
You are asked to serialize and deserialize a binary tree.

- `serialize` turns the tree into a string format (for storage/transmission).
- `deserialize` converts that string back into the original tree structure.

Constraints / Clarifications:
- Tree can have null nodes.
- Structure must be preserved exactly.
- You may assume no duplicate node values (though your code will still work with them).
- The output of `deserialize(serialize(tree))` should be structurally identical to the original tree.

Example:
Input Tree:     1
              /   \
             2     3
                  / \
                 4   5

Serialized: "1,2,3,null,null,4,5"
Deserialized: Reconstructs the same structure
"""

# M - Match with Patterns
"""
Pattern:
- Tree serialization/deserialization.
- Use BFS to preserve structure, including `None` placeholders.
- Common approach: Level-order traversal using a queue.
"""

# P - Plan
"""
1. Serialization:
   - Use a queue (BFS) to traverse the tree level by level.
   - Append each node’s value to the result list.
   - Use `"null"` for missing children.

2. Deserialization:
   - Use the tokenized string to rebuild the tree.
   - Use a queue to track nodes to which we need to assign children.
   - For each node, assign `left` and `right` from the token list if not "null".
"""

# I - Implement
from collections import deque

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                arr.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                arr.append(None)
        print(arr)
        return ",".join("null" if x is None else str(x) for x in arr)
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data == "null":
            return None

        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        q = deque([root])
        
        i = 1

        while q and i < len(tokens):
            node = q.popleft()

            if tokens[i] != "null":
                node.left = TreeNode(int(tokens[i]))
                q.append(node.left)
            i += 1

            if i < len(tokens) and tokens[i] != "null":
                node.right = TreeNode(int(tokens[i]))
                q.append(node.right)
            i += 1

        return root

# R - Review
"""
- The code correctly performs level-order serialization and deserialization.
- Handles null children properly.
- Edge case `root = None` is managed upfront.
"""

# E - Evaluate
"""
Time Complexity:
- Serialize: O(n), where n is the number of nodes.
- Deserialize: O(n)

Space Complexity:
- O(n) for both serialization result list and queue during traversal.

Notes:
- Clean and efficient BFS approach.
- Preserves the structure faithfully.
- You correctly use `deque` for BFS, and handle `null` nodes.

This is a solid FAANG-level solution for this problem.
"""

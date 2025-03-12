"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        U - Understand the Problem
        Problem Statement:
        - Given a **reference node** of a connected **undirected graph**, return a **deep copy** of the graph.
        - Each node contains:
          - `val`: Unique integer label for the node.
          - `neighbors`: A list of other nodes (edges).
        - The graph is represented as an adjacency list.

        Constraints:
        - The input graph is connected (all nodes are reachable).
        - The number of nodes is in the range `[0, 100]`.

        Clarifications:
        - What if `node` is `None`? ➝ Return `None` (Edge case).
        - What if `node` has no neighbors? ➝ Return a single-node graph.
        - Are node values unique? ➝ Yes, each node has a distinct integer value.
        - Should we preserve input graph structure? ➝ Yes, the cloned graph should **not** share references with the original.

        Examples:
        Input:
        ```
        1 -- 2
        |    |
        4 -- 3
        ```
        Output:
        ```
        1 -- 2
        |    |
        4 -- 3
        ```
        (Deep copy, preserving structure but with new node objects)
        """

        # M - Match with Patterns
        """
        - The problem involves **graph traversal** and **copying nodes**, which suggests:
          - **Breadth-First Search (BFS)** (iterative)
          - **Depth-First Search (DFS)** (recursive or iterative)
        - Since we need to map old nodes to their copies, **HashMap (Dict)** is useful.
        - BFS is suitable because it **iteratively processes each level**, ensuring we copy nodes **in order**.
        """

        # P - Plan
        """
        1. **Edge Case:** If `node` is `None`, return `None`.
        2. **Initialize Data Structures:**
            - `oldToCopy`: A hashmap `{original_node: cloned_node}` to store mappings.
            - `q`: A queue (for BFS traversal).
        3. **BFS Traversal:**
            - Start from `node`, create its copy, and store it in `oldToCopy`.
            - While the queue is not empty:
                - Dequeue a node.
                - Iterate over its neighbors:
                    - If a neighbor is not yet copied:
                        - Create a new copy and store it in `oldToCopy`.
                        - Enqueue the neighbor.
                    - Append the cloned neighbor to the copied node’s neighbor list.
        4. **Return the copied starting node** (`oldToCopy[node]`).
        """

        if not node:
            return None  # Edge case: Empty graph
        
        oldToCopy = {}  # HashMap to store original -> cloned node mappings
        oldToCopy[node] = Node(node.val)  # Clone the first node
        q = deque([node])  # Initialize BFS queue with the start node

        # BFS Traversal
        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if nei not in oldToCopy:  # If neighbor isn't copied yet
                    oldToCopy[nei] = Node(nei.val)  # Clone the neighbor
                    q.append(nei)  # Add neighbor to queue for traversal
                
                # Append the copied neighbor to the current node’s clone
                oldToCopy[curr].neighbors.append(oldToCopy[nei])
        
        return oldToCopy[node]  # Return the cloned graph's starting node

        """
        I - Implement
        ✅ Uses **Breadth-First Search (BFS)** for traversal.
        ✅ Ensures **all nodes are copied** without modifying the original graph.
        ✅ HashMap `oldToCopy` efficiently maps original nodes to their clones.

        R - Review
        ✅ Each node is visited **only once**.
        ✅ Ensures no duplicate copies of nodes.
        ✅ Preserves original graph structure in the deep copy.

        E - Evaluate
        Time Complexity: **O(N + E)**
        - We visit **each node once** and process **each edge once**.
        - Since it's an **undirected graph**, each edge is visited **twice** (once for each endpoint).

        Space Complexity: **O(N)**
        - We use:
          - `oldToCopy` HashMap storing **N nodes**.
          - `q` (BFS queue) storing **up to N nodes** in worst case.
        - No extra recursion stack since it's BFS.

        Alternative Approach:
        - **DFS (Recursive)**:
          - Instead of BFS, use a recursive DFS traversal.
          - Slightly more concise but risks hitting recursion limits for large graphs.
        - **DFS (Iterative)**:
          - Uses an explicit stack instead of recursion.

        Edge Cases:
        1. Empty graph (`node = None`) ➝ Return `None`.
        2. Single node with no edges ➝ Return a single cloned node.
        3. Graph with cycles ➝ Ensure nodes are **only cloned once**.
        """

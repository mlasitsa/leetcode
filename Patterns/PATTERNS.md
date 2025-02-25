## ✅ Recognizing Problem Types & Matching Patterns
For each topic, here’s how problems might be framed and the corresponding techniques to solve them.

---

### ✅ 1. If the input array is sorted, then:
#### ✨ How the problem might look like:
- Find a target element efficiently.
- Find a pair or triplet whose sum equals a given number.
- Count occurrences of an element.

#### 🔧 Common Techniques:
- **Binary Search** → "Find target in sorted array in O(log N)"
- **Two Pointers** → "Find two numbers whose sum is X"
- **Sliding Window** → "Find longest subarray meeting a condition"

---

### ✅ 2. If asked for all permutations/subsets, then:
#### ✨ How the problem might look like:
- "Generate all valid permutations of a string or numbers."
- "Find all subsets of a given array."
- "Return all valid arrangements."

#### 🔧 Common Techniques:
- **Backtracking** → "Explore all possibilities efficiently."
- **Bitmasking** → "Use bitwise operations to generate subsets."
- **Heap/Priority Queue** → "Find lexicographically smallest/largest permutations."

---

### ✅ 3. If given a tree, then:
#### ✨ How the problem might look like:
- "Find the depth/height of a binary tree."
- "Find the lowest common ancestor of two nodes."
- "Check if a tree is balanced or symmetric."

#### 🔧 Common Techniques:
- **DFS (Recursion/Stack)** → "Traverse tree deeply (preorder, inorder, postorder)."
- **BFS (Queue)** → "Level-order traversal (shortest path in an unweighted tree)."
- **Binary Search Tree (BST)** → "Use ordered properties for quick lookups."

---

### ✅ 4. If given a graph, then:
#### ✨ How the problem might look like:
- "Find if two nodes are connected."
- "Find the shortest path in a network."
- "Detect cycles in a graph."

#### 🔧 Common Techniques:
- **DFS** → "Explore all paths and backtrack if needed."
- **BFS** → "Use queue for shortest path search."
- **Dijkstra’s Algorithm** → "Find shortest weighted path."
- **Union-Find (Disjoint Set)** → "Detect cycles, connected components."

---

### ✅ 5. If given a linked list, then:
#### ✨ How the problem might look like:
- "Find the middle node of a linked list."
- "Detect and remove a cycle."
- "Reverse a linked list."

#### 🔧 Common Techniques:
- **Two Pointers (Fast/Slow)** → "Detect cycles, find the middle."
- **HashMap (Set for visited nodes)** → "Cycle detection without modifying list."
- **Stack** → "Reverse traversal, palindrome check."

---

### ✅ 6. If recursion is banned, then:
#### ✨ How the problem might look like:
- "Implement a function without recursion."
- "Convert a recursive DFS to an iterative one."
- "Process function calls manually."

#### 🔧 Common Techniques:
- **Stack** → "Simulate recursion manually."
- **Iterative Traversal** → "Use while loops instead of recursion."
- **Dynamic Programming (Bottom-Up)** → "Break recursion dependency."

---

### ✅ 7. If must solve in-place, then:
#### ✨ How the problem might look like:
- "Modify the input array without using extra space."
- "Swap elements efficiently."
- "Find the next permutation without extra memory."

#### 🔧 Common Techniques:
- **Swap Values** → "Rearrange elements without extra memory."
- **Two Pointers** → "Rearrange elements efficiently."
- **Floyd’s Cycle Detection** → "Find cycles in O(1) space."

---

### ✅ 8. If asked for maximum/minimum subarray/subset/options, then:
#### ✨ How the problem might look like:
- "Find the maximum sum subarray."
- "Find the longest increasing subsequence."
- "Find the minimum number of coins to make a value."

#### 🔧 Common Techniques:
- **Kadane’s Algorithm** → "Find max subarray sum in O(N)."
- **Sliding Window** → "Find optimal subarray with conditions."
- **Dynamic Programming** → "Solve overlapping subproblems (e.g., knapsack, LIS)."

---

### ✅ 9. If asked for top/least K items, then:
#### ✨ How the problem might look like:
- "Find the K most frequent elements."
- "Find the Kth largest/smallest element."
- "Return the top K closest points to the origin."

#### 🔧 Common Techniques:
- **Heap (Priority Queue)** → "Maintain a top K elements efficiently."
- **QuickSelect** → "Find Kth element in O(N) average time."
- **Bucket Sort** → "If values are in a limited range."

---

### ✅ 10. If asked for common strings, then:
#### ✨ How the problem might look like:
- "Find the longest common prefix."
- "Check if a word is present in a dataset efficiently."
- "Return the most frequent words."

#### 🔧 Common Techniques:
- **HashMap (Dictionary)** → "Track frequency or presence."
- **Trie (Prefix Tree)** → "Efficient prefix-based searching."
- **Rolling Hash (Rabin-Karp) / KMP Algorithm** → "Pattern matching."




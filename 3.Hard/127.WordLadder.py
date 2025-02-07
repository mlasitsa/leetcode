class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        U - Understand:
        - Problem: Given `beginWord`, `endWord`, and `wordList`, transform `beginWord` into `endWord` by changing exactly **one letter at a time**, ensuring:
          1. Each transformed word must exist in `wordList`.
          2. Find the **shortest** transformation sequence from `beginWord` to `endWord`.
          3. If no valid transformation exists, return `0`.

        - Key Observations:
          1. Each word is of equal length (`len(beginWord) == len(endWord)`).
          2. This is a **graph traversal** problem where words form nodes and edges exist if words differ by one letter.
          3. **BFS (Breadth-First Search)** is best for finding the shortest path.

        Example:
        - Input:
          ```
          beginWord = "hit", endWord = "cog"
          wordList = ["hot","dot","dog","lot","log","cog"]
          ```
        - Output: `5`
          ```
          "hit" -> "hot" -> "dot" -> "dog" -> "cog" (5 steps)
          ```

        - Edge Cases:
          1. If `endWord` is not in `wordList`, return `0`.
          2. `beginWord` and `endWord` may be different lengths (not in constraints).
          3. No valid transformation path.

        M - Match:
        - **Graph Traversal (BFS)**
          - Treat words as **nodes**.
          - An edge exists if two words **differ by exactly one letter**.
          - Use BFS to find the **shortest transformation path**.

        - **Graph Representation:**
          - Instead of checking all words for one-letter differences (O(n * m)), **use a wildcard pattern to group words efficiently**.
          - Example: Convert `"hot"`, `"dot"`, `"lot"` into:
            ```
            {'*ot': ['hot', 'dot', 'lot'], 
             'h*t': ['hot'], 
             'ho*': ['hot'], 
             'd*t': ['dot'], 
             'do*': ['dot', 'dog'], 
             '*og': ['dog', 'log', 'cog'], 
             'd*g': ['dog'], 
             'l*t': ['lot'], 
             'lo*': ['lot', 'log'], 
             'l*g': ['log'], 
             'c*g': ['cog'], 
             'co*': ['cog']}
            ```
          - This allows quick lookup of words that differ by one character.

        P - Plan:
        1. **Build the wildcard graph**:
           - Replace each character in every word with `"*"` to create wildcard patterns.
           - Store all words that match each pattern in a **hashmap**.

        2. **Use BFS to find the shortest transformation**:
           - Start with `beginWord` in a queue.
           - At each step, replace one letter at a time using the wildcard graph.
           - If `endWord` is reached, return the step count.
           - If no path exists, return `0`.

        I - Implement:
        '''
        if len(beginWord) != len(endWord) or endWord not in wordList:
            return 0

        graph = {}
        
        # Building the wildcard graph
        for word in wordList:
            for i in range(len(word)):
                wildCard = word[:i] + "*" + word[i + 1:]

                if wildCard in graph:
                    graph[wildCard].append(word)
                else:
                    graph[wildCard] = [word]
                
        '''
        Example Graph:
        {'*ot': ['hot', 'dot', 'lot'], 
         'h*t': ['hot'], 
         'ho*': ['hot'], 
         'd*t': ['dot'], 
         'do*': ['dot', 'dog'], 
         '*og': ['dog', 'log', 'cog'], 
         'd*g': ['dog'], 
         'l*t': ['lot'], 
         'lo*': ['lot', 'log'], 
         'l*g': ['log'], 
         'c*g': ['cog'], 
         'co*': ['cog']}
        '''

        def bfs():
            seen = set()
            q = deque()
            q.append((beginWord, 1))  # (word, count)
            seen.add(beginWord)

            while q:
                for _ in range(len(q)):
                    word, count = q.popleft()

                    for i in range(len(word)):
                        combo = word[:i] + "*" + word[i + 1:]
                        
                        if combo in graph:
                            for nei in graph[combo]:
                                if nei == endWord:
                                    return count + 1  # Found shortest path
                                elif nei in seen:
                                    continue
                                else:
                                    q.append((nei, count + 1))
                                    seen.add(nei)
            return 0

        return bfs()

    '''
    Alternative Solution: Bidirectional BFS
    - Instead of a single BFS from `beginWord`, perform **Bidirectional BFS**:
      - One BFS from `beginWord`.
      - One BFS from `endWord`.
      - Stop when both meet.

    P - Plan:
    1. Start BFS from both `beginWord` and `endWord`.
    2. Expand the **smaller** frontier first (reduces search space).
    3. Stop when both searches overlap.
    4. Return step count.

    I - Implement:
    '''
    def ladderLengthBidirectional(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = {}
        for word in wordList:
            for i in range(len(word)):
                wildCard = word[:i] + "*" + word[i + 1:]
                graph.setdefault(wildCard, []).append(word)
        
        # Two sets for bidirectional BFS
        front, back = {beginWord}, {endWord}
        seen = set()
        step = 1
        
        while front and back:
            if len(front) > len(back):
                front, back = back, front  # Expand smaller set
            
            newFront = set()
            for word in front:
                for i in range(len(word)):
                    combo = word[:i] + "*" + word[i + 1:]
                    for nei in graph.get(combo, []):
                        if nei in back:
                            return step + 1
                        if nei not in seen:
                            newFront.add(nei)
                            seen.add(nei)
            
            front = newFront
            step += 1
        
        return 0

# Example Usage:
'''
E - Evaluate:
1. Input:
   beginWord = "hit", endWord = "cog"
   wordList = ["hot","dot","dog","lot","log","cog"]
   Output: 5
   Explanation:
   "hit" -> "hot" -> "dot" -> "dog" -> "cog"

2. Input:
   beginWord = "hit", endWord = "cog"
   wordList = ["hot","dot","dog","lot","log"]
   Output: 0
   Explanation:
   - "cog" is not in the wordList, so return `0`.

Time Complexity:
- **Single BFS:** `O(N * M^2)`, where:
  - `N` is the number of words in `wordList`.
  - `M` is the length of each word (for generating wildcard patterns).
- **Bidirectional BFS:** `O(N * M)`, reduces search space by half.

Space Complexity:
- **O(N * M)**: Stores the wildcard graph and BFS queue.

'''

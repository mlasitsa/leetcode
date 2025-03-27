class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        ✅ U - Understand:
        -----------------
        - You are given a lock represented as a string of 4 digits "0000" to "9999".
        - You can turn each dial up (+1) or down (-1) to move to the next/previous digit.
        - You are given a list of `deadends` (invalid positions).
        - Starting from "0000", find the minimum number of moves to reach `target`.
        - If impossible (stuck in deadend), return -1.

        Clarifying Examples:
        - deadends = ["0201", "0101", "0102", "1212", "2002"], target = "0202"
          Output: 6
        - deadends = ["8888"], target = "0009"
          Output: 1

        Edge Cases:
        - If "0000" in deadends → instantly return -1
        - If target is "0000" → return 0

        ✅ M - Match:
        --------------
        - Graph traversal problem where each node is a lock state (string)
        - BFS is optimal here since we want the shortest number of moves (unweighted graph)

        ✅ P - Plan:
        ------------
        1. Define a `children` function to generate all valid next states (8 moves per state)
        2. Use BFS starting from "0000"
        3. Use a `visit` set to track visited nodes (including deadends)
        4. For each state:
            - If it equals target → return number of moves
            - Else, generate its children and add unvisited ones to the queue

        ✅ I - Implementation:
        -----------------------
        """

        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = int(lock[i])
                for move in [-1, 1]:
                    new_digit = (digit + move + 10) % 10  # Wrap around using mod
                    res.append(lock[:i] + str(new_digit) + lock[i+1:])
            return res

        from collections import deque
        q = deque()
        q.append(["0000", 0])  # (lock state, number of turns)
        visit = set(deadends)
        visit.add("0000")

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1])
        return -1

        """
        ✅ R - Review:
        -----------------
        - BFS ensures we explore all shortest paths first.
        - children() generates all possible next states.
        - Visit set ensures no cycles or revisits.

        ✅ E - Evaluate:
        -----------------
        Time Complexity:
        - At most 10,000 states (0000 to 9999)
        - Each node has 8 neighbors (4 wheels × 2 directions)
        - Total: O(N × 8) where N = number of unique states

        Space Complexity:
        - O(N) for queue and visited set

        ✅ Summary:
        - Classic shortest path BFS problem on an implicit graph.
        - Clean solution with constant branching factor.
        """

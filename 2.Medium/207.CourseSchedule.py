from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        '''
        - numCourses: Number of courses available
        - prerequisites: A list where each pair [a, b] means you must complete course `b` before course `a`.

        Example:
        numCourses = 2, prerequisites = [[1, 0]]
        - To take course 1, you must first take course 0.
        - Return True because it's possible.

        Example:
        numCourses = 2, prerequisites = [[1, 0], [0, 1]]
        - This creates a cycle: 0 → 1 → 0.
        - Return False.
        '''

        # Step 1: Build the adjacency list (graph)
        graph = {}

        for i in range(len(prerequisites)):
            take, needToBeDone = prerequisites[i]
            if take in graph:
                graph[take].append(needToBeDone)
            else:
                graph[take] = [needToBeDone]

        # Step 2: Create two sets for tracking visited and currently visiting nodes
        visited = set()    # Fully processed nodes
        visiting = set()   # Nodes currently being visited (cycle detection)

        # Step 3: Perform DFS Cycle Detection
        def dfs(node):
            if node in visiting:  
                return False  # Cycle detected!
            if node in visited:  
                return True  # Already processed successfully
            
            visiting.add(node)

            # Explore all prerequisites for this course
            if node in graph:  
                for nei in graph[node]:  
                    if not dfs(nei):  
                        return False  # Cycle detected in recursive call
            
            visiting.remove(node)  # Remove from visiting set after processing
            visited.add(node)  # Mark as fully processed
            return True

        # Step 4: Check for cycles in all courses
        for key in range(numCourses):
            if key in graph:  # Only run DFS if the course has dependencies
                if not dfs(key):  
                    return False  # If any course is part of a cycle, return False

        return True  # No cycle detected, courses can be completed

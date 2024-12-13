class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        U - Understand the Problem
        Problem Statement:
        - Compare two version numbers `version1` and `version2`.
        - Return:
          * -1 if `version1 < version2`.
          * 1 if `version1 > version2`.
          * 0 if they are equal.
        - Version numbers consist of digits and periods (e.g., "1.01", "1.001", "1.0").

        Clarifications/Constraints:
        - Extra leading zeros in a version number should be ignored (e.g., "1.01" == "1.1").
        - If version numbers have different lengths, treat missing segments as 0.
        - Valid version strings are non-empty and contain only digits and dots.

        Examples:
        Input: version1 = "1.01", version2 = "1.001"
        Output: 0

        Input: version1 = "1.0", version2 = "1.0.0"
        Output: 0

        Input: version1 = "0.1", version2 = "1.1"
        Output: -1

        Input: version1 = "1.2", version2 = "1.10"
        Output: -1
        """

        # M - Match with Patterns
        # Pattern Identified:
        # - Split the version strings by dots.
        # - Compare each segment as integers, treating missing segments as 0.

        """
        P - Plan
        1. Split the version strings by the dot delimiter into segments.
        2. Use two pointers to traverse the segments of both versions.
        3. Convert each segment to an integer and compare:
           - If a segment of `version1` is greater than `version2`, return 1.
           - If a segment of `version1` is less than `version2`, return -1.
        4. Treat missing segments in either version as 0.
        5. If all segments are equal, return 0.
        """

        # Step 1: Split the version strings
        segments1 = version1.split(".")
        segments2 = version2.split(".")
        
        # Step 2: Initialize pointers
        p1, p2 = 0, 0

        # Step 3: Traverse both version segments
        while p1 < len(segments1) or p2 < len(segments2):
            # Get the current segment or default to 0 if out of bounds
            num1 = int(segments1[p1]) if p1 < len(segments1) else 0
            num2 = int(segments2[p2]) if p2 < len(segments2) else 0

            # Compare the two segments
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1

            # Move to the next segment
            p1 += 1
            p2 += 1

        # Step 4: If all segments are equal, return 0
        return 0

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: version1 = "1.01", version2 = "1.001" -> Output: 0
2. Input: version1 = "1.0", version2 = "1.0.0" -> Output: 0
3. Input: version1 = "0.1", version2 = "1.1" -> Output: -1
4. Input: version1 = "1.2", version2 = "1.10" -> Output: -1

Edge Cases:
1. Different lengths -> Treat missing segments as 0.
2. Leading zeros in segments -> Ignore them (e.g., "001" == "1").
3. Single-segment version numbers -> Handle normally.

Time Complexity:
- O(max(n, m)): Traverse the longer version string.

Space Complexity:
- O(n + m): Space for the split version strings.
"""

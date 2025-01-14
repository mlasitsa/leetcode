class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        '''
        U - Understand:
        - Problem: Given two 0-indexed integer permutations A and B of length n:
          A prefix common array `C` of A and B is an array where:
          - `C[i]` is equal to the count of numbers that are present at or before index `i` in both A and B.
        - Clarifications:
          1. A and B are permutations, so each integer from 1 to n appears exactly once in each array.
          2. We must calculate `C[i]` efficiently without redundantly counting matches.

        Examples:
        - Input: A = [1, 3, 2, 4], B = [3, 1, 2, 4]
          Output: [0, 2, 3, 4]
          Explanation:
          - At index 0, no common numbers: C[0] = 0.
          - At index 1, common numbers: {1, 3} → C[1] = 2.
          - At index 2, common numbers: {1, 2, 3} → C[2] = 3.
          - At index 3, all numbers are common: {1, 2, 3, 4} → C[3] = 4.

        M - Match:
        - Use two sets `setA` and `setB` to keep track of numbers seen so far in A and B.
        - For each index `i`:
          1. Add the current numbers `A[i]` and `B[i]` to their respective sets.
          2. Check if the numbers at `A[i]` and `B[i]` are in the opposite set.
          3. Update `C[i]` based on the count of common elements.

        P - Plan:
        1. Initialize two sets `setA` and `setB` to keep track of numbers seen so far in A and B.
        2. Create an array `C` initialized with zeros.
        3. Iterate through the indices of A and B:
           - If `A[i]` is in `setB`, increment `C[i]`.
           - If `B[i]` is in `setA`, increment `C[i]`.
           - If `A[i] == B[i]`, increment `C[i]`.
           - Add `A[i]` to `setA` and `B[i]` to `setB`.
        4. Return the array `C`.

        I - Implement:
        '''
        setA = set()
        setB = set()
        C = [0] * len(A)

        for i in range(len(A)):
            if i > 0:
                C[i] += C[i - 1]
            if A[i] == B[i]:
                C[i] += 1
            if A[i] in setB:
                C[i] += 1
            if B[i] in setA:
                C[i] += 1

            setA.add(A[i])
            setB.add(B[i])

        return C

# Example Usage:
'''
E - Evaluate:
1. Input: A = [1, 3, 2, 4], B = [3, 1, 2, 4]
   Output: [0, 2, 3, 4]
   Explanation:
   - At index 0: No common elements.
   - At index 1: Common elements are {1, 3}.
   - At index 2: Common elements are {1, 2, 3}.
   - At index 3: Common elements are {1, 2, 3, 4}.

2. Input: A = [1, 2, 3], B = [3, 2, 1]
   Output: [0, 1, 3]

3. Edge Case: A = [1], B = [1]
   Output: [1]

Time Complexity:
- O(n): We iterate through the arrays once and perform O(1) operations for each index.

Space Complexity:
- O(n): Two sets are used to track seen elements in A and B.
'''

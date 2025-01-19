class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        U - Understand the Problem
        Problem Statement:
        - You are given a list of strings `words` and a list of queries.
        - Each query consists of two indices `[l, r]`.
        - For each query, determine how many words between indices `l` and `r` (inclusive) start and end with a vowel.

        Clarifications/Constraints:
        - `words[i]` consists of lowercase English letters.
        - A "vowel" is one of {'a', 'e', 'i', 'o', 'u'}.
        - 1 <= len(words) <= 10^5 and 1 <= len(queries) <= 10^5.
        - The solution should be efficient.

        Examples:
        Input: words = ["apple", "orange", "idea", "cat"], queries = [[0, 2], [1, 3]]
        Output: [2, 1]

        Potential clarifying questions:
        1. Are single-character words possible? (Yes.)
        2. Are all queries guaranteed to have valid indices? (Yes, per constraints.)
        3. What if there are no words starting and ending with vowels in a range? (Return 0 for that query.)
        """

        """
        M - Match with Patterns
        Pattern Identified:
        - Use a **prefix sum array** to efficiently count the number of words that start and end with vowels in a range.
        - Compute the prefix sum in O(n) time and use it to answer each query in O(1) time.
        """

        """
        P - Plan
        1. Precompute a prefix sum array where:
           - `prefix_sum[i]` = Number of vowel-strings in `words` from index 0 to i-1.
           - If a word at index `i` starts and ends with a vowel, increment the count.
        2. Answer each query `[l, r]` in O(1) time using:
           - `prefix_sum[r+1] - prefix_sum[l]`
           - This gives the count of vowel-strings in the range `[l, r]`.
        3. Return the list of answers.
        """

        # Step 1: Precompute prefix sum
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)
        prefix_sum = [0] * (n + 1)  # One extra space for easier calculations

        for i in range(n):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:  # Check if the word starts and ends with a vowel
                prefix_sum[i + 1] = prefix_sum[i] + 1
            else:
                prefix_sum[i + 1] = prefix_sum[i]

        # Step 2: Answer each query in O(1) time
        answer = []
        for l, r in queries:
            count = prefix_sum[r + 1] - prefix_sum[l]
            answer.append(count)

        return answer

# Example Usage:
"""
E - Evaluate
Test the solution with examples:
1. Input: words = ["apple", "orange", "idea", "cat"], queries = [[0, 2], [1, 3]]
   Output: [2, 1]
   Explanation:
   - Query [0, 2]: "apple" and "idea" start and end with vowels, count = 2.
   - Query [1, 3]: Only "idea" starts and ends with vowels, count = 1.

2. Edge Case: No vowel-strings in the range.
   Input: words = ["dog", "cat", "ball"], queries = [[0, 2]]
   Output: [0]

Time Complexity:
- Precomputing the prefix sum: O(n)
- Answering all queries: O(m), where m = len(queries)
- Total: O(n + m)

Space Complexity:
- Prefix sum array: O(n)
"""

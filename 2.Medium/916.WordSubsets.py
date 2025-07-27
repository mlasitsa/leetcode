class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        U - Understand:
        - Problem: Given two lists of words, find the "universal" words in `words1` that satisfy all conditions defined by `words2`.
          A word in `words1` is "universal" if for every word in `words2`, it contains all the characters with at least the same frequency.
        - Clarifications/Constraints:
          1. Each character in `words2` must appear in a universal word in `words1` with at least the required frequency.
          2. All words contain only lowercase English letters.
        - Examples:
          Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
          Output: ["facebook","google","leetcode"]
          Explanation:
          - Universal words satisfy:
            * "e" appears at least once.
            * "o" appears at least once.

        M - Match:
        - This is a **frequency counting problem**. Use dictionaries to track character frequencies:
          1. Combine frequency requirements for all words in `words2` into a single dictionary (`countFreq`).
          2. Check each word in `words1` to see if it satisfies the requirements in `countFreq`.

        P - Plan:
        1. Create a `countFreq` dictionary to store the maximum frequency of each character across all words in `words2`.
        2. For each word in `words2`, count character frequencies and update `countFreq` with the maximum required frequencies.
        3. For each word in `words1`, count its character frequencies and compare against `countFreq`.
        4. If a word in `words1` meets all the frequency requirements, add it to the result list.
        5. Return the result list.

        I - Implement:
        """
        # Step 1: Create a dictionary to store the maximum frequency of each character in words2
        countFreq = {}
        for word in words2:
            localFreq = {}
            for ch in word:
                localFreq[ch] = localFreq.get(ch, 0) + 1
            for ch in localFreq:
                countFreq[ch] = max(countFreq.get(ch, 0), localFreq[ch])

        # Step 2: Check each word in words1 against the countFreq requirements
        final = []
        for word in words1:
            wordFreq = {}
            for ch in word:
                wordFreq[ch] = wordFreq.get(ch, 0) + 1
            
            # Verify if the word in words1 satisfies the frequency requirements in countFreq
            isUniversal = all(wordFreq.get(ch, 0) >= countFreq[ch] for ch in countFreq)
            if isUniversal:
                final.append(word)
        
        return final

# Example Usage:
"""
E - Evaluate:
1. Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
   Output: ["facebook","google","leetcode"]

2. Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
   Output: ["apple","google","leetcode"]

3. Edge Case: words1 = ["abc"], words2 = ["z"]
   Output: []
   Explanation: No word in `words1` contains "z".

Time Complexity:
- Constructing `countFreq`: O(len(words2) * avg_len_word2).
- Checking `words1`: O(len(words1) * avg_len_word1).
- Total: O(n * m), where `n` is the total length of `words2` and `m` is the total length of `words1`.

Space Complexity:
- Storing frequency dictionaries: O(26) = O(1) for lowercase English letters.
"""

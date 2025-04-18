class Solution:
    def partition(self, s: str) -> List[List[str]]:

        '''
        U - Understand the Problem

        Problem:
        - Given a string `s`, partition it such that every substring of the partition is a palindrome.
        - Return all possible palindrome partitioning of `s`.

        Clarifications:
        - All characters in the string are lowercase.
        - A partition must include *all characters*, i.e., it is not about selecting but splitting.
        - Each substring in a valid partition must itself be a palindrome.

        Example:
        Input: s = "aab"
        Output: [["a","a","b"],["aa","b"]]

        Edge Cases:
        - Empty string => return [[]]
        - All characters same => exponential combinations of repeated single characters and combinations
        '''
        ans = []
        part = []

        def backtrack(start):
            if start >= len(s):
                ans.append(list(part))  # Deep copy to store one valid partition
                return
            
            for i in range(start, len(s)):
                if self.isPalindrome(s, start, i):
                    part.append(s[start:i + 1])  # Include current palindrome
                    backtrack(i + 1)             # Recurse for the rest
                    part.pop()                   # Backtrack to try another cut
        
        backtrack(0)
        return ans
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

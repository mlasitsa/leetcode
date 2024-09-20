class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        char1 = list(word1)
        char2 = list(word2)
        one = 0
        two = 0

        while (one < len(char1) or  two < len(char2)):
            if one < len(char1):
                merged.append(char1[one])
                one += 1
            if two < len(char2):
                merged.append(char2[two])
                two += 1
        return ''.join(merged)

sol = Solution()  
res = sol.mergeAlternately("abc", "pqr")

if res == "apbqcr":
    print("Success")
else:
    print("Failed")


'''

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        smallestWord = strs[0]
        answer = ""

        for word in strs:
            if len(word) < len(smallestWord):
                smallestWord = word
        

        for i in range(len(smallestWord)):
            for word in strs:
                if smallestWord[i] != word[i]:
                    return answer
            answer += smallestWord[i]
        
        return answer

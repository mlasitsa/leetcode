class Solution:
    def reverseVowels(self, s: str) -> str:
        hmap = {'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u'}

        if len(s) == 0:
            return "None"

        if len(s) == 1:
            return s[0]

        word = list(s)
        left = 0 
        right = len(s) - 1

        while left < right:
            if word[left].lower() in hmap and word[right].lower() in hmap:
                word[left], word[right] = word[right], word[left]
                left += 1 
                right -= 1
            elif word[right].lower() not in hmap:
                right -= 1
            elif word[left].lower() not in hmap :
                left += 1
        return "".join(word)

sol = Solution()
res = sol.reverseVowels("IceCreAm")

if res == "AceCreIm":
    print("Good Job")
else:
    print('Try again')

    
class Solution:
    def reverseWords(self, s: str) -> str:
        right = len(s) - 1
        stack = []
        answer = []

        while right >= 0:
            # Skip spaces
            while right >= 0 and s[right] == " ":
                right -= 1
            
            # If we are out of bounds, break
            if right < 0:
                break
            
            # Collect characters of the current word
            while right >= 0 and s[right] != " ":
                stack.append(s[right])
                right -= 1
            
            # Append the collected word in correct order
            while stack:
                answer.append(stack.pop())
            
            # Skip spaces to check if there are more words
            while right >= 0 and s[right] == " ":
                right -= 1
            
            # Add a space if there are more words to process
            if right >= 0:
                answer.append(" ")

        return "".join(answer)
        
sol = Solution()
res = sol.reverseWords("the sky is blue")

if res == "blue is sky the":
    print("Good Job!")
else:
    print("Try Again...")
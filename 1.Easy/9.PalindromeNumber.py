# The easiest way is to convert it into string and do TWO pointer
# If you want you can try yourself without converting it into string using division and mod operator (I think to get left and right to compare)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        digist = str(x)
        left = 0 
        right = len(digist) - 1

        if len(digist) == 1 or len(digist) == 0:
            return True
        
        while left < right:
            if digist[left] != digist[right]:
                return False
            elif digist[left] == digist[right]:
                left += 1
                right -= 1
        return True
                
            
        
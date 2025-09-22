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


# Another optimal solution (without converting into a string)

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        div = 1
        while x >= 10 * div:
            div *= 10
        
        while x:
            right = x % 10
            left = x // div

            if left != right:
                return False
            
            x = (x % div) // 10
            div =  div / 100
        return True
        
                
            
        
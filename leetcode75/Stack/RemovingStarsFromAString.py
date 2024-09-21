class Solution:
    def removeStars(self, s: str) -> str:

        '''
        Initial approach I think here is to use stack, we can append an element, then if we hit a star
        we need to pop an element and skip this star ? 
        we need to skip stars
        we need to be careful with popping
        also we are given a string, so careful straversal

        THis can also be done with two pointers approach, but doesnt really make sense 
        since we need to convert it into a list since string are immutable in python
        '''

        # leet**cod*e
        stack = []  

        for ch in s:
            # here since we dont need to append a star, we need to make a check
            # what if it starts with *, then we can skip it

            if ch == "*" and not stack:
                continue 
            elif ch == "*" and stack:
                stack.pop()
            else:
                stack.append(ch)    

        return "".join(stack)

sol = Solution()
res = sol.removeStars("leet**cod*e")

if res == 'lecoe':
    print("Good Job")
else:
    print("Try Again...")
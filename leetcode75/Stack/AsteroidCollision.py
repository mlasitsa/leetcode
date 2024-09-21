class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        '''
        So in this problem, we need to use stack since we need to compare an element that is in the stack
        with an element that is going to pushed on to stack
        Since we are only comparing when we have positvie and next negative, since this is when collision
        happens.
        If we have negative value and then positive - IT DOESNT MATTER since THEY ARE GOING DIFFERENT     
        DIRECTIONS

        traverse through asteroids
        check if we have collision - if so we compare top of stack with curent asteroind
        now we can compare either sum < 0 or not or if abs value is > then top of stack [-1]
        we need to do while loop since our value could be greater twice or more
        if they are equal we pop element (Example of 8 and -8), then we break cuz both explode
        else we would just break since it means that our top is greater than asteroid
        if we dont have collision then we just append

        '''

        stack = []  # Stack to store surviving asteroids
        
        for asteroid in asteroids:
            # Handle the case of collisions with a negative asteroid
            while stack and asteroid < 0 and stack[-1] > 0:
                # Compare the top of the stack with the current asteroid
                if abs(asteroid) > stack[-1]:  # Current asteroid is larger (it destroys the one on the stack)
                    stack.pop()  # Remove the top of the stack (destroyed)
                    continue  # Keep checking for further collisions
                elif abs(asteroid) == stack[-1]:  # Both asteroids are the same size
                    stack.pop()  # Destroy both asteroids
                    break  # No further collisions to handle
                else:  # The top of the stack asteroid is larger
                    break  # Current asteroid is destroyed, stop the loop
            else:
                # No collision or asteroid moves in the same direction
                stack.append(asteroid)
        
        return stack



sol = Solution()
res = sol.asteroidCollision([5,10,-5])
answer = [5,10]

if res == answer:
    print("Good Job")
else: 
    print("Try Again...")
    
 


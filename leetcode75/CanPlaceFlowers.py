class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        '''
        so here we have an array and what if all of them are 0? 
        we place and then we need to move + 2 since we are not allowed to plant next to each other
        here I can see a pointer approach when we move pointer to 2 times if we see one 
        or if we plant
        and we would decrement our n
        we also need to check if n == 0 then we would return right away, if not, we continue
        do while loop probably so we can break from the loop
        edge case could be if an array is empty, then return False
        our return statement could be False
        '''
        
        if len(flowerbed) == 0:
            return False

        if n == 0:
            return True

        pointer = 0

        while pointer < len(flowerbed):
            # If current spot is empty
            if flowerbed[pointer] == 0:
                # Check if we can plant here (next to empty or end of array)
                nextTo = pointer + 1
                prevTo = pointer - 1

                # Check if the previous and next positions are empty or out of bounds
                if (pointer == 0 or flowerbed[prevTo] == 0) and (nextTo == len(flowerbed) or flowerbed[nextTo] == 0):
                    # Plant a flower
                    flowerbed[pointer] = 1
                    n -= 1
                    # Move pointer by 2 as we can't plant adjacent flowers
                    pointer += 2
                else:
                    # Move to the next position
                    pointer += 1
            else:
                # If we see a flower, move the pointer by 2
                pointer += 2

            # Check if we have placed all required flowers
            if n == 0:
                return True

        # If we are out of the loop and still have flowers to place, return False
        return False

sol = Solution()
res = sol.canPlaceFlowers([1,0,0,0,1], 1)

if res == True:
    print("Sucess")
else:
    print("Fail...")
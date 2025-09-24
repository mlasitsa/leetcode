class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        sorted in non decresasing order, return array of squares of each number
        I need to find O(n) that doesnt use sorting

        so for negaive values, I can technically remove them I think ???
        I can create an array and then add all positive elements ?
        Well something I can also do is to implement bucket sort technically
        or technically here

        [-4,-1,0,3,10]
         0 pivot
         left < less
         right > more
        
        well bucket sort techincally won work well here, but I can try
        NOT THE BEST SOLUTION, BUT WORKS
        '''

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = nums[i] * -1
        
        maxVal = float('-inf')
        for num in nums:
            maxVal = max(maxVal, num)
        
        print(nums)
        buckets = [0] * (maxVal + 1)
        for num in nums:
            buckets[num] += 1
        
        final = []
        for i in range(len(buckets)):
            while buckets[i] > 0:
                final.append(i * i)
                buckets[i] -= 1
        
        return final
        

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''

        [-4,-1,0,3,10]
         0 pivot
         left < less
         right > more
 

        TWO POINTER
        '''

        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        
        final = list(nums)
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1
        while left <= right:
            if nums[left] >= nums[right]:
                final[index] = nums[left]
                left += 1
            else:
                print(index)
                final[index] = nums[right]
                right -= 1
            index -= 1
        
        return final

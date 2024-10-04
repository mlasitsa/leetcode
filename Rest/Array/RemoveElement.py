class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer to keep track of valid elements
        
        # Iterate through each element in nums
        for i in range(len(nums)):
            # If the element is not equal to val, move it to the front
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        # Return the number of valid elements (not equal to val)
        return k
        
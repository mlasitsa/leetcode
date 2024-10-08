class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hmap = {}
        arr = []

        n = len(nums)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] in hmap:
                    hmap[nums[i][j]] += 1
                else:
                    hmap[nums[i][j]] = 1
        
        for key, value in hmap.items():
            if value == len(nums):
                arr.append(key)
        
        arr.sort()
        return arr



        
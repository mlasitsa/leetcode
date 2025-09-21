class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in hmap:
                return [hmap[remaining], i]
            else:
                hmap[nums[i]] = i 
        return None

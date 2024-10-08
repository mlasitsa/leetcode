class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hmap = {}
        arr = []

        for num in nums1:
            if num in hmap:
                hmap[num] += 1
            else: 
                hmap[num] = 1
        
        for num in nums2:
            if num in hmap and hmap[num] > 0:
                arr.append(num)
                hmap[num] -= 1
        
        return arr
        
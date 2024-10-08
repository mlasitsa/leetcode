class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        arr = set()
        store = set()

        for num in nums1:
            if num not in store:
                store.add(num)

        for num in nums2:
            if num in store:
                arr.add(num)
        return list(arr)




        
        
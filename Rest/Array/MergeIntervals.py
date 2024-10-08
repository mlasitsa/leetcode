class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        arr = []

        intervals.sort(key = lambda x: x[0], reverse= False)

        for interval in intervals:
            if not arr or interval[0] > arr[-1][1]:
                arr.append(interval)
            else:
                arr[-1][1] = max(arr[-1][1], interval[1])
        return arr
        
        
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]

        Also could tried to use binary search since array is sorted, 
        but for simplicity decided to do iterative approach
        """

        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
                
            pointer = i + 1

            while pointer < len(numbers):
                if numbers[i] + numbers[pointer] == target:
                    return [i + 1, pointer + 1]
                else:
                    pointer += 1
        
        
      
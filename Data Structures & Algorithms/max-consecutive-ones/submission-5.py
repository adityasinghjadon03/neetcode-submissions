class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for i in nums:
            if i == 1:
                count += 1
            
            elif i == 0:
                result = max(result, count)
                count = 0
        if count > result:
            result = count
        return result
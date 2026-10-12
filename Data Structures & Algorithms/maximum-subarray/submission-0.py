class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxsum = nums[0]
        for n in nums:
            cursum = max(cursum, 0)
            cursum += n
            maxsum = max(maxsum, cursum)
        return maxsum
        
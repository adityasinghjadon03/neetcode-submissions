class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        add = 0
        length = float('inf')
        for R in range(len(nums)):
            add += nums[R]
            while add >= target:
                length = min(R - L + 1, length)
                add -= nums[L]
                L += 1
        return length if length != float('inf') else 0
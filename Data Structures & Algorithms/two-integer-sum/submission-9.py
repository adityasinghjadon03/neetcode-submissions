class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = [(value, index) for index, value in enumerate(nums)]
        num.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            add = num[i][0] + num[j][0]
            if add == target:
                res = [num[i][1], num[j][1]]
                res.sort()
                return res
            elif add > target:
                j -= 1
            else:
                i += 1
        return -1
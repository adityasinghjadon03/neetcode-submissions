class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            hashmap[value] = index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap and hashmap[diff] != i:
                return [i, hashmap[diff]]
        return[]
        
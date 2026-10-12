class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        cumsum = 0
        res = 0
        for i in range(len(nums)):
            cumsum += nums[i]
            required = cumsum - k
            if required in hashmap:
                res += hashmap[required]
            hashmap[cumsum] = hashmap.get(cumsum, 0) + 1
        return res
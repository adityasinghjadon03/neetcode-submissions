class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        res = 0
        hashmap = {}
        for R in range(len(s)):
            hashmap[s[R]] = hashmap.get(s[R], 0) + 1
            while (R - L + 1) - max(hashmap.values()) > k:
                hashmap[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
        return res
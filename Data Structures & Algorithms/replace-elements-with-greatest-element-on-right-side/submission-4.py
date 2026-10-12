class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        inMax = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(inMax, arr[i])
            arr[i] = inMax
            inMax = newMax
        return arr